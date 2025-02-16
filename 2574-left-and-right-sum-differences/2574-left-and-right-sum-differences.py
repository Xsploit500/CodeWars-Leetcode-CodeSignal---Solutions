class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)

        leftSum, rightSum, output = [0], [total - nums[0]], []

        total = sum(nums)

        for i in range(0, len(nums) - 1):
            leftSum.append(nums[i] + leftSum[-1])
            rightSum.append(rightSum[-1] - nums[i + 1])

        for i in range(len(nums)):
            output.append(abs(leftSum[i] - rightSum[i]))

        return output