# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        if not root:
            return 0
        
        lh = self.maxheight(root)
      
        
        return self.result

    
    def maxheight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        left = self.maxheight(root.left)
        right = self.maxheight(root.right)
        self.result = max(self.result, left + right)

        return 1 + max(left , right)