class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        Map = {}

        for num in nums:
            if num not in Map:
                Map[num] = 0
                Map[num] += 1
            else:
                Map[num] += 1

        result = 0

        for key, val in Map.items():
            result += (val * (val - 1)) // 2

        return result

        # output = []

        # for i in range(0, len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j] and i != j:
        #             output.append((i, j))

        # return len(output)
        