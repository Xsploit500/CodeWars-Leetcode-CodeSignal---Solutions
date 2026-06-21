# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root, values):
            if not root:
                return

            helper(root.left, values)
            values.append(root.val)
            helper(root.right, values)

        values = []
        helper(root, values)
        return values





        # Iterative
        # stack = []
        # current = root
        # result = []

        # while current or stack:
        #     while current:
        #         stack.append(current)
        #         current = current.left

        #     current = stack.pop()
        #     result.append(current.val)
        #     current = current.right

        # return result