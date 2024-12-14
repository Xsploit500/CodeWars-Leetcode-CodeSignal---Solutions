class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # from collections import Counter

        # nums = Counter(nums)

        # for key, value in nums.items():
        #     if value == 1:
        #         return key



        if len(nums) == 1:
            return nums[0]

        left, right = 0, 1

        length = len(nums)

        while right < length:
            if nums[left] == nums[right]:
                left += 2
                right += 2
            else:
                return nums[left]
        
        return nums[left]