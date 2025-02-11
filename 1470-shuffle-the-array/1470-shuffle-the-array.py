class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        finalarr = []

        left, right = 0, len(nums) // 2

        while right < len(nums):
            finalarr.append(nums[left])
            finalarr.append(nums[right])

            left += 1
            right += 1

        return finalarr

