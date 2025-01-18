class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)

        maximum = max(nums)

        if maximum <= 0:
            return 1
        
        for i in range(1, maximum + 2):
            if i not in nums:
                return i
        
        
        
        
        
        # nums = set(nums)

        # minimum = 1

        # while minimum in nums:
        #     minimum += 1
        
        # if minimum not in nums:
        #     return minimum