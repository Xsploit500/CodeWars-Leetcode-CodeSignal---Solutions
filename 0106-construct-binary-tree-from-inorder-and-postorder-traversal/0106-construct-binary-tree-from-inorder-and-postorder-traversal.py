# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None

        val = postorder[-1]
        root = TreeNode(val)
        mid = inorder.index(val)
        left_inorder = inorder[:mid]
        right_inorder = inorder[mid + 1:]
        left_postorder = postorder[:len(left_inorder)]
        right_postorder = postorder[len(left_inorder): -1]
        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)

        return root
        