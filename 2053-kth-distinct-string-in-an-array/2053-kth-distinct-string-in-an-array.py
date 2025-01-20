class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        occurences, distinct = {}, []

        for char in arr:
            if char not in occurences:
                occurences[char] = 1
            else:
                occurences[char] += 1

        for key, value in occurences.items():
            if value == 1:
                distinct.append(key)

        return "" if len(distinct) < k else distinct[k - 1]