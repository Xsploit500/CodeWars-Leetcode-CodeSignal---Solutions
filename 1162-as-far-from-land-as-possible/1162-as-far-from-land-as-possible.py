class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        N = len(grid)

        q = deque()

        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    q.append([r, c])

        result = -1
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while q:
            r, c = q.popleft()

            result = grid[r][c]
            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                if (min(newR, newC) >= 0 and max(newR, newC) < N and grid[newR][newC] == 0):
                    q.append([newR, newC])
                    grid[newR][newC] = grid[r][c] + 1

        return result - 1 if result > 1 else -1