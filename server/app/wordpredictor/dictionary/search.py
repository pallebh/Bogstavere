class Node(object):

    def __init__(self, trie_node=None, list_index=None, word_part_index=None):
        self.trieNode = trie_node
        self.listIndex = list_index
        self.wordPartIndex = word_part_index

    def __str__(self):
        return "node {0} li {1} wi {2}".format(self.trieNode, self.listIndex, self.wordPartIndex)

    def wordPart(self):
        return self.trieNode[0][0:wordPartIndex+1]

class Path(object):
    def __init__(self):
        self.nodes = []

    def __iter__(self):
        return iter(self.nodes)

    def __len__(self):
        return len(self.nodes)

    def append(self, trieNode):
        pathNode = node(trieNode, listIndex, wordPartIndex)
        self.nodes.append(pathNode)

    def __getitem__(self, key):
        self.nodes.__silce__(key)

    def update(self, listIndex, wordPartIndex):
        self.nodes[-1].listIndex = listIndex
        self.nodes[-1].wordPartIndex = wordPartIndex