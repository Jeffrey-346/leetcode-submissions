# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # we just want to find the path to each node and check that path,
        # updating the LCA until they diverge
        # but how do we get a path (a set of nodes) of ancestors
        p_anc = self.getAncestors(root, [], p)
        q_anc = self.getAncestors(root, [], q)

        if len(p_anc) < len(q_anc):
            count = len(p_anc)
        else: count = len(q_anc)

        for i in range(count):
            if p_anc[i] != q_anc[i]:
                return p_anc[i - 1]
        return p_anc[count - 1]

    def getAncestors(self, root, ancestors, target):
        if root == None:
            return
        ancestors.append(root)
        if root == target:
            return ancestors
        res = self.getAncestors(root.left, ancestors, target)
        if res:
            return ancestors
        res = self.getAncestors(root.right, ancestors, target)
        if res:
            return ancestors
        ancestors.pop()
        