# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inOrderTraversal(node):
            if not node:
                return []
            return inOrderTraversal(node.left) + [node.val] + inOrderTraversal(node.right)

        sortedValues = inOrderTraversal(root)

        return sortedValues[k - 1]




        from collections import deque
        import heapq

        def bfs(root):
            if not root:
                return []

            queue, values = deque([root]), []

            while len(queue) > 0:
                current = queue.popleft()

                values.append(current.val)

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

            return values

        minheap, traversal = [], bfs(root)

        for val in traversal:
            heapq.heappush(minheap, val)

        for _ in range(k):
            popped = heapq.heappop(minheap)

        return popped