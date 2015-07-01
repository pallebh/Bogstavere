from collections import deque
from collections import namedtuple


class Trie(object):
    def __init__(self , root = None ) :
        self.root = root if root else list()

    def get_root(self):
        return self.root

    def __str__(self):
        return str(self.root)

    def load(self, words):
        stack = deque()

        for word in words:
            stack.append([word, self.root, True, None, 0])

            while stack:
                word_part, node, last, move, count = stack.pop()

                nl = len(word_part)

                for n in node:
                    ol = len(n[0])

                    m = ol if ol < nl else nl
                    index = 0
                    while index < m:
                        if not word_part[index] == n[0][index]:
                            break
                        index += 1

                    if index == 0:
                        continue

                    if index < ol:
                        move = n[1]
                        n[1] = list()
                        stack.append([n[0][index:], n[1], n[2], move, 0])  # suffix_old
                        n[0] = n[0][0:index]  # prefix
                        n[2] = False

                    if index < nl:
                        stack.append([word_part[index:], n[1], True, None, 0])

                    break

                else:
                    if not move: move = list()
                    node.insert(0, [word_part, move, last, 0])


    def step( self , letter , nodeIndex = None , wordPartIndex = None ):
        if nodeIndex == None :
            for nodeIndex , node in enumerate( self.root ) :
                if letter == node[0] :
                    wordPartIndex = 0
                    break
            else :
                return None , None , None

        n = self.root[ nodeIndex ]
        if ( wordPartIndex+1) > ( len( n[ 0 ] ) - 1 ) :
            return Trie( n[1] ), nodeIndex, wordPartIndex

        if wordPart[ wordPartIndex ] == letter :
            return None, nodeIndex, wordPartIndex

        #return None , None , None

    def walk(self, deeped=0, maxDeeped=0):
        wordStack = []
        word = ""
        return self.__walk(self.root, word, wordStack, deeped, maxDeeped)

    def __walk(self, node, word, wordStack, deeped=0, maxDeeped=0):
        for n in node:
            wordPart, nextLevel, last, count = n
            tmpDeeped = deeped


            if last:
                suffix = "".join( word.lower() + wordPart.lower() )
                count =  self.__count( nextLevel )
                tmp =[  suffix , count ]
                wordStack.append( tmp )
                if maxDeeped:
                    tmpDeeped = tmpDeeped + 1

            if ( maxDeeped == 0 ) or ( tmpDeeped < maxDeeped ):
                self.__walk(nextLevel, word + wordPart, wordStack, tmpDeeped, maxDeeped)

        return wordStack


    def __count(self, node, count=0):
        for n in node:
            next_level = n[1]
            last = n[2]
            if last:
                count += 1
            self.__count(next_level, count)
        return count