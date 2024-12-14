class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        HashMap = {}

        for num in nums:
            if num % 2 == 0:
                if num not in HashMap:
                    HashMap[num] = 1
                else:
                    HashMap[num] += 1

        output, count = -1, 0
        
        for key, val in HashMap.items():
            if key > output and val > count:
                output, count = key, val

        return output
