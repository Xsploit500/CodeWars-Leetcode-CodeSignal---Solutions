class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 1, 2

        length = len(nums)

        while right < length:
            if nums[left] > nums[left - 1] and nums[left] < nums[right]:
                return nums[left]
            left += 1
            right += 1