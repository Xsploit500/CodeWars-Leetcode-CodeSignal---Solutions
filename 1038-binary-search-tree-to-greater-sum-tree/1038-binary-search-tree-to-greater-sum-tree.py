# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return []

        stack = []
        running_sum = 0
        current = root

        while current != None:
            stack.append(current)
            current = current.right

        while stack:
            node = stack.pop()
            original_value = node.val
            node.val += running_sum
            running_sum += original_value

            current = node.left
            while current != None:
                stack.append(current)
                current = current.right

        return root
