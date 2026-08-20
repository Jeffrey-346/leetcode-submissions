class Solution:
    def isValid(self, s: str) -> bool:
        # seems like need a stack
        # if we encounter an open, add it to the stack
        # if we encounter a closed, check the top of the stack
        pairs = {"(" : ")", "{" : "}", "[" : "]"}
        stack = []
        if len(s) % 2 != 0:
            return False
        # assume even
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            if c == ")" or c == "]" or c == "}":
                if not stack:
                    return False
                partner = stack.pop()
                if partner not in pairs.keys() or pairs[partner] != c:
                    return False
        if stack:
            return False
        return True




        