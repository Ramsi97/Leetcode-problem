# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def construct(left, right):
            if left > right:
                return None
            mid = left + (right-left)//2 
            root = TreeNode(nums[mid])
            root.left = construct(left, mid-1)
            root.right = construct(mid+1, right)
            return root
        return construct(0, len(nums)-1)
