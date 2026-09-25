class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        # eat away s:
        # add s to frontier
        # for each word in wordDict, check if it can fit into s
        # if it can, add the mutated s to the frontier
        # if we ever get empty string return true
        # otherwise if the search ends, return false
        frontier = deque()
        frontier.append(s)
        visited = set()

        while frontier:
            food = frontier.popleft()
            for word in wordDict:
                match = True
                if len(word) > len(food):
                    continue
                for i in range(len(word)):
                    if food[i] != word[i]:
                        match = False
                        break
                if match:
                    if not food[len(word):]:
                        return True
                    if food[len(word):] not in visited:
                        frontier.append(food[len(word):])
                        visited.add(food[len(word):])
        return False






        