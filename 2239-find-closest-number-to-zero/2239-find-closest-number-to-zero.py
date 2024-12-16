class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        minimum = min([abs(num) for num in nums])

        output = [num for num in nums if abs(num) == abs(minimum)]
        
        return max(output)

        # min_dist = float('inf')

        # for i in range(len(nums)):
        #     if abs(nums[i]) <= min_dist:
        #         min_dist = abs(nums[i])

        # max_num, output = min_dist, float('-inf')

        # for num in nums:
        #     if num >= output and abs(num) == max_num:
        #         output = num

        # return output





        # distances = []

        # for num in nums:
        #     distances.append(abs(num))

        # minimum = min(distances)

        # distances = set([distance for distance in distances if distance == minimum])

        # output = float('-inf')

        # for num in nums:
        #     if num > output and abs(num) == list(distances)[0]:
        #         output = num

        # return output