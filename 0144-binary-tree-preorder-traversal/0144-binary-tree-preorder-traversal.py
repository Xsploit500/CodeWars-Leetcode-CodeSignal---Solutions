# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root, values):
            if not root:
                return
            values.append(root.val)
            helper(root.left, values)
            helper(root.right, values)

        values = []
        helper(root, values)
        return values



        # Iterative
        # stack = [root]
        # result = []
        
        # if not root:
        #     return []

        # while stack:
        #     current = stack.pop()
        #     result.append(current.val)

        #     if current.right:
        #         stack.append(current.right)

        #     if current.left:
        #         stack.append(current.left)

        # return result