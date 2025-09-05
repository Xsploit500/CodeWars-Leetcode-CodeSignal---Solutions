class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        import math

        count = {}

        for val in nums:
            if val not in count:
                count[val] = 1
            else:
                count[val] += 1

        for key, val in count.items():
            if val > math.floor((len(nums) / 2)):
                return key