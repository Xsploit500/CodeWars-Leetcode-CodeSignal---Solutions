class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = []

        for i in nums:
            smaller = 0

            for j in nums:
                if j < i:
                    smaller += 1
            
            output.append(smaller)

        return output
        