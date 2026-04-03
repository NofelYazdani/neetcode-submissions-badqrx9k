# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        answer = []
        def dfs(node):
            if not node:
                answer.append("null")
                return
            answer.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(answer)
        

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        newdata = data.split(",")
        self.counter = 0
        def dfs():
            if newdata[self.counter] == "null":
                self.counter += 1
                return None
            node = TreeNode(int(newdata[self.counter]))
            self.counter += 1
            node.left = dfs()
            node.right = dfs()
            return node
        tree = dfs()
        return tree

