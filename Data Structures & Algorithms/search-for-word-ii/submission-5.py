class TrieNode:
    def __init__(self):
        self.children = {} # maps character to TrieNode
        self.isWord = False
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # trie structure populated with the list of words
        # then for each letter in board: hey, is this in the root's
        # keys? (i.e. is this the first letter of any word)
        # Then check:
        # Are any of curr's keys next to curr index?
        # if they are, then go in that direction
        # if not, return

        def makeTrie():
            root = TrieNode()
            for word in words:
                curr = root
                for c in word:
                    if c not in curr.children:
                        curr.children[c] = TrieNode()
                    curr = curr.children[c]
                curr.isWord = True
            return root

        def dfs(row, col, curr):
            letter = board[row][col]
            if letter in curr.children and (row, col) not in seen:
                s.append(letter)
                seen.add((row,col))
            else: return
            curr = curr.children[letter]
            if curr.isWord:
                res.add("".join(s))
            if row > 0: # up
                dfs(row - 1, col, curr)
            if row < n_rows - 1: # down
                dfs(row + 1, col, curr)
            if col > 0: # left  
                dfs(row, col - 1, curr)
            if col < n_cols - 1: # right
                dfs(row, col + 1, curr)
            seen.remove((row, col))
            s.pop()
            return
        
        root = makeTrie()
        res = set()  
        n_rows = len(board)
        n_cols = len(board[0])

        for row in range(n_rows):
            for col in range(n_cols):
                s = []
                seen = set() # set of already seen indices
                dfs(row, col, root)
        return list(res)







