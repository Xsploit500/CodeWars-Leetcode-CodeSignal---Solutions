# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        from collections import deque

        level = 0

        queue, leftVals = deque([(root, level)]), []

        while len(queue) > 0:
            current, level = queue.popleft()

            if len(leftVals) == level:
                leftVals.append(current.val)

            if current.left:
                queue.append((current.left, level + 1))

            if current.right:
                queue.append((current.right, level + 1))

        return leftVals[-1]