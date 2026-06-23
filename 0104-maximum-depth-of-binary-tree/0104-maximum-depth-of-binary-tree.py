# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0

        # depth = 1

        # stack = [(root, depth)]

        # while stack:
        #     current, max_depth = stack.pop()

        #     if max_depth > depth:
        #         depth = max_depth

        #     if current.left:
        #         stack.append((current.left, max_depth + 1))

        #     if current.right:
        #         stack.append((current.right, max_depth + 1))

        # return depth






        if not root:
            return 0

        from collections import deque

        depth = 1

        queue = deque([(root, 1)])

        while len(queue) != 0:
            current, max_depth = queue.popleft()

            if max_depth > depth:
                depth = max_depth

            if current.left:
                queue.append((current.left, max_depth + 1))

            if current.right:
                queue.append((current.right, max_depth + 1))

        return depth

        
        
        
        
        # def helper(root):
        #     if not root:
        #         return 0

        #     left_call = helper(root.left)
        #     right_call = helper(root.right)

        #     return 1 + max(left_call, right_call)

        # return helper(root)