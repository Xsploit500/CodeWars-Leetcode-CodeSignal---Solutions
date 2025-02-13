class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        Map = {}

        difference = 0

        for index, char in enumerate(s):
            Map[char] = index

        for index2, char2 in enumerate(t):
            difference += abs(index2 - Map[char2])

        return difference
        