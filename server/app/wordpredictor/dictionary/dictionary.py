from . trie import Trie
from . node import Node

import codecs

class Dictionary(object):
    def __init__(self, words ):
        
        self.trie = Trie()
        self.words = words
        self.__load_words()
        self.path = []
        self.reset()
        self.lastWasInteger = False

    def reset(self):
        self.path = []
        self.path.append(Node(self.trie))

    def __load_words(self):
        self.trie.load(self.words)

    def __prefix(self):
        prefix = ""
        for pn in self.path[0:-1]:
            node_index = pn.nodeIndex
            prefix += pn.trie.root[node_index][0]
        return prefix

    def addInt(self):
        self.lastWasInteger = True

    def keypress( self, key ) :

        if key == "space":
            self.reset()
            return self.wordList()

        if key == "backspace":
            if self.path and not self.lastWasInteger :
                self.path.pop()

            if self.lastWasInteger :
                self.lastWasInteger = False

            if not self.path:
                self.reset()
            return self.wordList()


        return self.search( key )

    def search(self, letter):
        path_node = self.path[-1]
        trie = path_node.trie

        node_index = path_node.nodeIndex
        word_part_index = path_node.wordPartIndex

        next, node_index, word_part_index = trie.step( letter , node_index , word_part_index )
        print( next , node_index , word_part_index )

        self.path[-1].update(node_index, word_part_index )
        if next :
            self.path.append( Node( next ) )

        return self.wordList()
        

    def wordList(self):
        import collections
        WordList = collections.namedtuple( "WordList" , [ "prefix" , "suffixes" ] )

        path_node = self.path[-1]
        prefix = self.__prefix()
        suffixes = path_node.trie.walk(0,1)

        return WordList( prefix , suffixes )
