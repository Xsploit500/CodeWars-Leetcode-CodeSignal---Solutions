class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        marked = defaultdict(int)

        for src, dst in trust:
            marked[src] -= 1
            marked[dst] += 1

        for i in range(1, n + 1):
            if marked[i] == n - 1:
                return i

        return -1