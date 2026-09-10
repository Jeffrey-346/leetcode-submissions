class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # create a graph. We will need bfs since we are looking for
        # shortest distance
        # connect each word to all possible adjacent word
        # traverse from the first word to the last, trace path with map

        wordList.append(beginWord)
        adj = [[] for i in range(len(wordList))]
        start_index = len(wordList) - 1
        end_index = None
        for i in range(len(wordList)):
            if wordList[i] == endWord:
                end_index = i
            for j in range(len(wordList)):
                different = 0
                if i == j:
                    continue
                for k in range(len(wordList[0])):
                    if wordList[i][k] != wordList[j][k]:
                        different += 1
                if different == 1:
                    adj[i].append(j)

        if end_index is None:
            return 0

        parent = {}
        parent[start_index] = -1
        queue = deque()
        queue.append(start_index)
        while queue:
            index = queue.popleft()
            if index == end_index:
                break
            for neighbor in adj[index]:
                if neighbor not in parent:
                    queue.append(neighbor)
                    parent[neighbor] = index
        if end_index not in parent:
            return 0
        path = 1
        curr = end_index
        while curr != start_index:
            path += 1
            curr = parent[curr]
        return path








                


        