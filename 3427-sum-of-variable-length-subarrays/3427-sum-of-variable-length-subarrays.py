class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        output = nums[0]

        for i in range(1, len(nums)):
            start = max(0, i - nums[i])
            subarr = []
            for j in range(start, i + 1):
                subarr.append(nums[j])
            output += sum(subarr)

        return output

