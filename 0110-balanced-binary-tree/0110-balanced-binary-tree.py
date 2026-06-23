# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root:
                return 0

            left_call = helper(root.left)
            if left_call == -1:
                return -1
            right_call = helper(root.right)
            if right_call == -1:
                return -1

            if abs(left_call - right_call) > 1:
                return -1
            else:
                return 1 + max(left_call, right_call)

        return helper(root) != -1


        