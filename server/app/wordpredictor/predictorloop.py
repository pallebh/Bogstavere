import queue
from . import book
from . import dictionary
import operator
import keyboard
from itertools import groupby
import collections

class PredictorLoop(object):
    def __init__(self, event_queue, result_queue):
        words = book.read("../content/books/words-da.bwb")
        self.dictionary = dictionary.Dictionary(words)
        print("done building dictionary")
        k90words = book.read_k90("../content/books/k90-ord.txt")
        self.wordsWeight = self.buildwordsWeight(words, k90words)
        self.event_queue = event_queue
        self.result_queue = result_queue
        self.writer = keyboard.writer.Writer()
        self.lastWordList = []
        
    def buildwordsWeight(self, words, k90s):
        wordweight = {}
        for word in words:
            try:
                wordweight[word] = k90s[word]
            except:
                wordweight[word] = 0
        return wordweight

    def keyisdigit(self, key):
        key = int(key)
        self.dictionary.addInt()
        self.writer.keypress( "\x08" )
        wordList = self.dictionary.wordList()

        if key > len( self.lastWordList ) - 1:
            return

        print("word to print {0}".format( wordList.suffixes[key][0] ) )

        for letter in wordList.suffixes[key][0]:
            wordList = self.dictionary.keypress(letter)
            self.writer.keypress(letter)

            if not wordList.suffixes:
                print("found end for word")

        self.writer.keypress(" ")

        self.buildWordlist(wordList)

    def foundEndOfWord(self, wordList):
        if len(wordList.suffixes) == 1:
            if wordList.suffixes[0][1] == 0:
                print("fousd word end")
                self.writer.keypress(" ")

    def buildWordlist(self, wordList):
        wl = [[sf[1], wordList.prefix + sf[0]] for sf in wordList.suffixes]
        #wl2 = []
        #for ww in wl:
        #    if ww[1] in self.wordsWeight:
        #        wl2.append((self.wordsWeight[ww[1]], ww[1]))
        #    else:
        #        wl2.append((0, ww[1]))

        #wl = sorted(wl2, key=operator.itemgetter(0), reverse=True)
        return wl
        
    def keyisdigit(self, key):
        key = int(key)
        self.dictionary.addInt()
        self.writer.keypress( "\x08" )
        wordList = self.lastWordList
        
        for letter in wordList.suffixes[key][0]:
            self.writer.keypress( letter )
            self.keyisletter( letter )
            
    def keyisletter(self, key):
        print("keyisletter")
        wordList = self.dictionary.keypress(key)
        print( wordList )
        
        #if len( wordList.suffixes ) == 1 :
        #    suffix = wordList.suffixes[0][0]
        #    for s in suffix :
        #        self.writer.keypress(s)

        tmpList = self.buildWordlist( wordList )
        self.lastWordList = wordList
        self.result_queue.put( tmpList )


    def run(self):

        while True:
            try:
                keypress = self.event_queue.get(timeout=0.1)
                key = keypress["keypress"]

                if key.isdigit():
                    self.keyisdigit(key)
                else:
                    self.keyisletter(key)

            except queue.Empty:
                pass

            except KeyboardInterrupt:
                break
