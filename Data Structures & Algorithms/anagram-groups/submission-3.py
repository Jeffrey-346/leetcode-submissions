class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                index = ord(char) - ord("a") 
                count[index] += 1
            my_dict[tuple(count)].append(s)
        res = []
        for value in my_dict.values():
            res.append(value)
        return res
        