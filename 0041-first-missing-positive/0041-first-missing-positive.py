class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)

        minimum = 1

        while minimum in nums:
            minimum += 1
        
        if minimum not in nums:
            return minimum