# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        val = preorder[0]
        root = TreeNode(val)

        if len(postorder) == 1:
            return root

        left_root_val = preorder[1]
        left_size = postorder.index(left_root_val) + 1

        left_preorder = preorder[1:left_size + 1]
        right_preorder = preorder[left_size + 1:]
        left_postorder = postorder[0:left_size]
        right_postorder = postorder[left_size:-1]

        root.left = self.constructFromPrePost(left_preorder, left_postorder)
        root.right = self.constructFromPrePost(right_preorder, right_postorder)

        return root