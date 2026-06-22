# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root, values):
            if not root:
                return
            
            helper(root.left, values)
            helper(root.right, values)
            values.append(root.val)

        values = []
        helper(root, values)
        return values