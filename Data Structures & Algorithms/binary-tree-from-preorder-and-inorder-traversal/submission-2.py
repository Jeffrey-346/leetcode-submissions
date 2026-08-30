# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        dic = {}
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        return self.helper(preorder, inorder, dic, 0, len(preorder), 0, len(preorder))
        
    def helper(self, preorder, inorder, dic, pre_start, pre_end, in_start, in_end):
        if pre_start == pre_end:
            return None
        root = TreeNode(preorder[pre_start])
        left_size = dic[root.val] - in_start
        root.left = self.helper(preorder, inorder, dic, pre_start + 1,  pre_start + 1 + left_size, in_start, dic[root.val])
        root.right = self.helper(preorder, inorder, dic, pre_start + 1 + left_size, pre_end, dic[root.val] + 1, in_end)
        return root
            


        
        