class Node:
    def __init__(self, letter=None):
        self.children = [None] * 26 # list of nodes, one for each letter
        self.isWord = False

class PrefixTree:
    # seems like each level of the tree is a letter

    def __init__(self):
        self.root = Node() # set of nodes
        
    def insert(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            letter = word[i]
            index = ord(letter) - ord('a')
            if not curr.children[index]:
                curr.children[index] = Node()
            curr = curr.children[index]
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for i in range(len(word)):
            letter = word[i]
            index = ord(letter) - ord('a')
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        if curr.isWord:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in range(len(prefix)):
            letter = prefix[i]
            index = ord(letter) - ord('a')
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        return True
        
        