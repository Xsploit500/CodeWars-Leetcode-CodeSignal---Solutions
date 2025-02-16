class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum, rightSum, output = [0], [0], []

        for i in range(0, len(nums) - 1):
            leftSum.append(nums[i] + leftSum[-1])

        for i in range(len(nums) - 1, 0, -1):
            rightSum.append(nums[i] + rightSum[-1])

        rightSum = rightSum[::-1]

        for i in range(len(nums)):
            output.append(abs(leftSum[i] - rightSum[i]))

        return output