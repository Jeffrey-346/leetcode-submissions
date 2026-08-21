class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # maintain a stack of indicies
        # the stack must be decreasing
        # if a index is added whose value is greater than stack[-1]
        # pop until the invariant is restored
        # at each pop, use the popped index to set in the same index of
        # the results list the difference between the popped index and
        # the current index

        decreasing_stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while decreasing_stack and temperatures[i] > temperatures[decreasing_stack[-1]]:
                index = decreasing_stack.pop()
                res[index] = i - index
            decreasing_stack.append(i)
        return res


        