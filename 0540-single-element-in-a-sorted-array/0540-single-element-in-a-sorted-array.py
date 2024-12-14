class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        from collections import Counter

        nums = Counter(nums)

        for key, value in nums.items():
            if value == 1:
                return key



        # if len(nums) == 1:
        #     return nums[0]

        # if len
        # left, right = 0, 1

        # length = len(nums)

        # while right < length:
        #     if nums[left] > nums[left - 1] and nums[left] < nums[right]:
        #         return nums[left]
        #     left += 1
        #     right += 1