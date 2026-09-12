class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for word in words for c in word}
        in_degree = {c: 0 for c in adj}

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            
            for j in range(len(w1)):
                if j >= len(w2):
                    print("hello?")
                    return ""
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    break
        
        queue = deque()
        for c in in_degree:
            if in_degree[c] == 0:
                queue.append(c)
                
        res = ""
        while queue:
            c = queue.popleft()
            res += c

            for neighbor in adj[c]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(res) != len(adj):
            return ""
        else:
            return res


        