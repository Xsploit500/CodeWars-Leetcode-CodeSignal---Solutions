class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        from collections import Counter
        
        output = []

        occurences = Counter(nums)

        for key, value in occurences.items():
            if value > 1:
                output.append(key)

        return output