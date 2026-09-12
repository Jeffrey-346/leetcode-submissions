class Solution:
    def climbStairs(self, n: int) -> int:
        # really only need last two
        if n == 1:
            return 1
        if n == 2:
            return 2
        steps = [0, 0]
        steps[0] = 1
        steps[1] = 2
        for i in range(3, n + 1):
            save = steps[1]
            steps[1] = steps[0] + steps[1]
            steps[0] = save
        return steps[1]
        