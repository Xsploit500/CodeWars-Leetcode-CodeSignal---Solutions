class Solution:
    def fib(self, n: int) -> int:
        memo = [0, 1]

        while len(memo) < n + 1:
            memo.append(memo[-1] + memo[-2])

        return memo[-1]