# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        trav = []
        self.getTraversal(root, trav)
        for i in range(len(trav) - 1):
            if trav[i] >= trav[i + 1]:
                return False
        return True
    
    def getTraversal(self, root, trav):
        # we can also just recursively traverse the tree and check
        # to make sure that the traversal is in order
        if not root:
            return
        self.getTraversal(root.left, trav)
        trav.append(root.val)
        self.getTraversal(root.right, trav)



        