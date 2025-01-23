class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        first_case = nums[0] * nums[1] * nums[2]
        second_case = nums[0] * nums[-1] * nums[-2]

        return max(first_case, second_case)