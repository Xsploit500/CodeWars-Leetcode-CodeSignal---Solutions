# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [root]

        total = 0

        while stack:
            current = stack.pop()

            if current.val % 2 == 0:
                if current.left:
                    if current.left.left:
                        total += current.left.left.val
                    if current.left.right:
                        total += current.left.right.val
                if current.right:
                    if current.right.left:
                        total += current.right.left.val
                    if current.right.right:
                        total += current.right.right.val
            
            if current.left:
                stack.append(current.left)

            if current.right:
                stack.append(current.right)

        return total