# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        lst = []
        self.getTraversal(root, lst)
        return lst[k - 1]
    
    def getTraversal(self, root, lst):
        if not root:
            return
        self.getTraversal(root.left, lst)
        lst.append(root.val)
        self.getTraversal(root.right, lst)
        
        