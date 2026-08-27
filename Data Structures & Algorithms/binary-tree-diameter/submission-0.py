# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # find depth of left and depth of right, add them together
        # that gives the diameter of a given node
        # return max diameter found in left and right children (might not be through root)
        if not root:
            return 0
        return max(self.depth(root.left) + self.depth(root.right), self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

    def depth(self, root):
        if not root:
            return 0
        return max(1 + self.depth(root.left), 1 + self.depth(root.right))
        