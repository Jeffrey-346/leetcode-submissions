# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # we could do breadth first search but only append the last item
        # to be popped for each level

        if not root:
            return []

        res = []
        q = deque()
        q.append(root)

        while q:
            # append rightside value for this level
            res.append(q[-1].val)
            level = deque()
            # add entire level at once
            while q:
                curr = q.popleft()
                if curr.left:
                    level.append(curr.left)
                if curr.right:
                    level.append(curr.right)
            q = level

        return res


        