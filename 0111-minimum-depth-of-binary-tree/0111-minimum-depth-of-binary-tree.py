# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if not root:
                return 0

            left_call = helper(root.left)
            right_call = helper(root.right)

            if (root.left and not root.right) or (root.right and not root.left):
                return 1 + max(left_call, right_call)

            return 1 + min(left_call, right_call)

        return helper(root)