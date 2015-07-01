class Node(object):

    def __init__(self, trie=None, nodeIndex=None, wordPartIndex=None):
        self.trie = trie
        self.nodeIndex = nodeIndex
        self.wordPartIndex = wordPartIndex

    def update( self, nodeIndex = None, wordPartIndex = None ) :
        if nodeIndex != None :
            self.nodeIndex = nodeIndex

        if wordPartIndex != None :
            self.wordPartIndex = wordPartIndex

    def __str__(self):
        return "nodeIndex:{0} wordIndexPart:{1}".format( self.nodeIndex , self.wordPartIndex )