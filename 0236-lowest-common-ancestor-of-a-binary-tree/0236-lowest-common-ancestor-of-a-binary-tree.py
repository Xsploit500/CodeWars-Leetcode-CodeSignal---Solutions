# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find_path(root, target):
            if not root:
                return None

            if root.val == target:
                return [root]

            left_path = find_path(root.left, target)

            if left_path:
                left_path.append(root)
                return left_path

            right_path = find_path(root.right, target)

            if right_path:
                right_path.append(root)
                return right_path

        path1 = find_path(root, p.val)
        path2 = find_path(root, q.val)

        path2_vals = set(node.val for node in path2)

        for node in path1:
            if node.val in path2_vals:
                return node


        