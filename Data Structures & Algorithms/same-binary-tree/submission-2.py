# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p and q:
            return False
        if p and not q:
            return False

        if type(p.left) == type(q.left):
            left = self.isSameTree(p.left, q.left)
        else:
            left = False
        if type(p.right) == type(q.right):
            right = self.isSameTree(p.right, q.right)
        else:
            right = False
        
        if p.val == q.val:
            return left and right and True
        else:
            return False
        