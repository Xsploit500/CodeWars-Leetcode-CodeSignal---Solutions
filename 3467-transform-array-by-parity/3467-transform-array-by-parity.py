class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[i] % 2 > 0:
                nums[i] = 1
            else:
                nums[i] = 0
        
        return sorted(nums)