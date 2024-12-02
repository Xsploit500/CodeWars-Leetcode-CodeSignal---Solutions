class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        import heapq
        
        cols, rows = len(grid[0]), len(grid)

        maxheap = [[] for _ in range(rows)]

        row_count = 0

        while row_count < len(grid):
            for arr in grid:
                for val in arr:
                    maxheap[row_count].append(-val)
                row_count += 1

        for array in maxheap:
            heapq.heapify(array)

        count, total = 0, 0

        maximums = []

        while count < len(grid[0]):
            for array in maxheap:
                popped = -heapq.heappop(array)
                maximums.append(popped)
            count += 1
            total += max(maximums)
            maximums.clear()

        return total