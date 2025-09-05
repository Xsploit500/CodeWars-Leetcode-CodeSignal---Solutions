# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Iterative DFS
        if not root:
            return True

        stack = [(root, float('-inf'), float('inf'))]

        while stack:
            node, min_val, max_val = stack.pop()

            if node.val <= min_val or node.val >= max_val:
                return False
            
            if node.right:
                stack.append((node.right, node.val, max_val))
            
            if node.left:
                stack.append((node.left, min_val, node.val))

        return True

        # # Recursive Solution
        # def validate(node, min_val, max_val):
        #     if not node:
        #         return True
        #     if node.val <= min_val or node.val >= max_val:
        #         return False
        #     return (validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val))

        # return(validate(root, float("-inf"), float("inf")))