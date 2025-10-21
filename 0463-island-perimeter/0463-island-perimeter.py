class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()

        count = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return self.dfs(grid, row, col, visited)

        return 0

    def dfs(self, grid, row, col, visited):
        valid_row = 0 <= row < len(grid)
        valid_col = 0 <= col < len(grid[0])

        if not valid_row or not valid_col:
            return 1

        if grid[row][col] == 0:
            return 1

        position = (row, col)

        if position in visited:
            return 0

        visited.add(position)

        count = 0

        count += self.dfs(grid, row + 1, col, visited)
        count += self.dfs(grid, row - 1, col, visited)
        count += self.dfs(grid, row, col + 1, visited)
        count += self.dfs(grid, row, col - 1, visited)

        return count

        
        