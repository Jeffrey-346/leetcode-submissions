# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # let's pretend the string is a list and fill it out
        # specifically if the node has no child put "none"
        res = []
        def getDepth(root):
            if not root:
                return 0
            return 1 + max(getDepth(root.left), getDepth(root.right))
        depth = getDepth(root)
        curr = 0
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val) + ",")
                q.append(node.left)
                q.append(node.right)

            else:
                res.append("null,")
        print("".join(res))
        return "".join(res)
            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        lst = data.split(",")
        lst.pop()
        nodes = []
        for elm in lst:
            if elm == "null":
                nodes.append(None)
            else:
                new_node = TreeNode(int(elm))
                nodes.append(new_node)
        sub = 0
        for i in range(len(nodes)):
            # calculate children positions:
            node = nodes[i]
            left_idx = i * 2 + 1 + sub
            right_idx = i * 2 + 2 + sub
            if not node:
                sub -= 2
            else:
                if left_idx < len(nodes):
                    node.left = nodes[left_idx]
                if right_idx < len(nodes):
                    node.right = nodes[right_idx]
        return nodes[0]
            
            

