# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        if not root:
            return 0
        q.append(root)
        count = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                print(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            count+= 1
        return count

