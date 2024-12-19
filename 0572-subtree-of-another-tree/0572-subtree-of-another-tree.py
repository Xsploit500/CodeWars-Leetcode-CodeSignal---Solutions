# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(value):
            stack, values = [value], []

            while stack:
                current = stack.pop()

                values.append(current.val)

                if current.left:
                    stack.append(current.left)
                if current.right:
                    stack.append(current.right)

            return values
        
        rootValues, subrootValues = dfs(root), dfs(subRoot)

        length = len(subrootValues)

        left, right = 0, length

        while right < len(rootValues) + 1:
            if rootValues[left:right] == subrootValues:
                return True
            left += 1
            right += 1
        return False
        