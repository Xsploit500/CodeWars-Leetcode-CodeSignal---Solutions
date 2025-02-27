class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        result = 0

        unique = set(nums)

        for num in nums:
            if (num + diff) in unique and (num + (diff * 2)) in unique:
                result += 1

        return result



        # count = 0

        # for i in range(0, len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j + 1, len(nums)):
        #             if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
        #                 count += 1

        # return count