# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        from collections import deque

        depth = 1

        queue = deque([(root, depth)])

        while queue:
            current, depth = queue.popleft()

            if not current.left and not current.right:
                return depth

            if current.left:
                queue.append((current.left, depth + 1))

            if current.right:
                queue.append((current.right, depth + 1))


                


        # def helper(root):
        #     if not root:
        #         return 0

        #     left_call = helper(root.left)
        #     right_call = helper(root.right)

        #     if (root.left and not root.right) or (root.right and not root.left):
        #         return 1 + max(left_call, right_call)

        #     return 1 + min(left_call, right_call)

        # return helper(root)