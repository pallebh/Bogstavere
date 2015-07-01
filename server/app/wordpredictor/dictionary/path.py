from node import Node

class Path(object):

    def __init__(self):
        self.nodes = []

    def __iter__(self):
        return iter(self.nodes)

    def __len__(self):
        return len(self.nodes)

    def append(self, trieNode):
        pathNode = Node( trieNode, 0, 0 )
        self.nodes.append(pathNode)

    def __getitem__(self, key):
        print "key " , key
        #print dir( self.nodes )
        return self.nodes[key]

    def update(self, listIndex, wordPartIndex):
        self.nodes[-1].listIndex = listIndex
        self.nodes[-1].wordPartIndex = wordPartIndex