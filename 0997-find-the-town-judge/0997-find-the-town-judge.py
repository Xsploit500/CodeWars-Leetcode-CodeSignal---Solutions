class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        marked = [0] * (n + 1)

        for src, dst in trust:
            marked[src] -= 1
            marked[dst] += 1

        for index, value in enumerate(marked):
            if value == n - 1:
                return index

        return -1