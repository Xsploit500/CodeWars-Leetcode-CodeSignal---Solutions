# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(root):
            stack, values = [root], []

            while stack:
                current = stack.pop()

                if current is None:
                    values.append("null")

                else:
                    values.append(current.val)
                    stack.append(current.left)
                    stack.append(current.right)

            return values

        return dfs(p) == dfs(q)




        if not p and not q:
            return True
        if p and not q or not p and q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)