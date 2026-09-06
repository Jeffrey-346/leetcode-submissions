class TrieNode:
    def __init__(self):
        self.children = {} # dictionary from character to a tree node
        self.isWord = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True
        
    def search(self, word: str) -> bool:
        def dfs(i, curr):
            if i == len(word):
                return curr.isWord
            if word[i] in curr.children:
                return dfs(i + 1, curr.children[word[i]])
            if word[i] == '.':
                for c in curr.children:
                    if dfs(i + 1, curr.children[c]):
                        return True
            return False

        return dfs(0, self.root)
            


        
