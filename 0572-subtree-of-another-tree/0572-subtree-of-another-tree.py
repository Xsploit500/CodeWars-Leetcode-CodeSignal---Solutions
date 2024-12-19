# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(value):
            if not value:
                return ["null"]

            stack, values = [value], []

            while stack:
                current = stack.pop()

                if current:
                    values.append(current.val)
                    stack.append(current.left)
                    stack.append(current.right)
                
                else:
                    values.append('null')

            return values
        
        rootValues, subrootValues = dfs(root), dfs(subRoot)

        length = len(subrootValues)

        left, right = 0, length

        while right <= len(rootValues):
            
            if rootValues[left:right] == subrootValues:
                return True
            
            left += 1
            right += 1
        
        return False
        