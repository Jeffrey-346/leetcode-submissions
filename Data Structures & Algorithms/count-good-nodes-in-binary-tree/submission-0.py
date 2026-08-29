# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.helper(root, float("-infinity"))
    
    def helper(self, root, max_value):
        if not root:
            return 0
        if root.val >= max_value:
            return 1 + self.helper(root.left, root.val) + self.helper(root.right, root.val)
        else:
            return self.helper(root.left, max_value) + self.helper(root.right, max_value)

        