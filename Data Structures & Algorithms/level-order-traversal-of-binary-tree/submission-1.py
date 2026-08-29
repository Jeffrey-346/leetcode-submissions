# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # get the depth of the tree
        # create a list with depth sublists
        # make a helper that takes current depth as in input
        # append to the correct sublist and call recursively
        depth = self.getDepth(root)
        res = [[] for _ in range(depth)]
        self.fillList(root, 0, res)
        return res

    def fillList(self, root, depth, res):
        if not root:
            return
        res[depth].append(root.val)
        self.fillList(root.left, depth + 1, res)
        self.fillList(root.right, depth + 1, res)


    def getDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.getDepth(root.left), self.getDepth(root.right))
        