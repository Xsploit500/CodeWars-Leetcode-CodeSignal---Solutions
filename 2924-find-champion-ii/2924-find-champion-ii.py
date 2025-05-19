class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        marker = [0] * n

        for src, dst in edges:
            marker[dst] += 1

        champions = []

        for index, marked in enumerate(marker):
            if marked == 0:
                champions.append(index)

        return champions[0] if len(champions) == 1 else -1