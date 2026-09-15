class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        i = 0
        for key in (0, 1, 2):
            for _ in range(count.get(key, 0)):
                nums[i] = key
                i += 1



        # low, i, high = 0, 0, len(nums) - 1

        # while i <= high:
        #     if nums[i] == 0:
        #         nums[low], nums[i] = nums[i], nums[low]
        #         low += 1
        #         i += 1
        #     elif nums[i] == 2:
        #         nums[i], nums[high] = nums[high], nums[i]
        #         high -= 1
        #     else:
        #         i += 1