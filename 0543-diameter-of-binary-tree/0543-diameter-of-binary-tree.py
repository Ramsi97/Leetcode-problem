# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = 0
    def maxlength(self, root):
        if not root:
            return -1
        left = 1 + self.maxlength(root.left)
        right = 1 + self.maxlength(root.right)
        self.result = max(self.result, left+right)
        return max(left, right)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        self.maxlength(root)
        return self.result