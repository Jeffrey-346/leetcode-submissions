# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # definitely recursive structure: 
        # the limitation is that we can only have one "pivot"
        # so we want to compare recursively:
        # - suppose we split on current root
        # find the max if we never split in left child and never split
        # on right child
        # compare to maxPathSum on left and right child
        res = [root.val]
        
        def dfs(root):
            if not root:
                return 0
            
            leftMax = max(0, dfs(root.left))
            rightMax = max(0, dfs(root.right))
            
            res[0] = max(res[0], root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)
        dfs(root)
        return res[0]

    
    
        