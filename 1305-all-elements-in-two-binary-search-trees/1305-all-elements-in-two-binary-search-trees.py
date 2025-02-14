# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        def traverse(root):
            if not root:
                return 0

            stack = [root]

            values = []

            while len(stack) != 0:
                current = stack.pop()

                values.append(current.val)

                if current.left:
                    stack.append(current.left)
                if current.right:
                    stack.append(current.right)

            return values

        tree1 = traverse(root1)
        tree2 = traverse(root2)

        if tree1 and tree2:
            return sorted(tree1 + tree2)
        elif tree1 and not tree2:
            return sorted(tree1)
        else:
            return sorted(tree2)