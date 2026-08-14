class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # setting up map/processing first string
        s_map  = defaultdict(int)
        for char in s:
            s_map[char] += 1
        # process second string
        for char in t:
            if s_map[char] == 0:
                return False
            s_map[char] -= 1
        # confirm that map is zeroed
        for key in s_map.keys():
            if s_map[key] != 0:
                return False
        return True
        
        