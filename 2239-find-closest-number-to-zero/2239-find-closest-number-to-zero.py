class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        distances = []

        for num in nums:
            distances.append(abs(num))

        minimum = min(distances)

        distances = set([distance for distance in distances if distance == minimum])

        output = float('-inf')

        for num in nums:
            if num > output and abs(num) == list(distances)[0]:
                output = num

        return output

        # distance, number = float('inf'), float('-inf')

        # for num in nums:
        #     if abs(num) <= distance or (abs(num) <= distance and num >= number):
        #         distance = abs(num)
        #         number = num

        # return num