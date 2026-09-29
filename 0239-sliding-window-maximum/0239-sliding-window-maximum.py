class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        from collections import deque

        queue = deque()
        result = []
        
        for i, num in enumerate(nums):
            while queue and nums[queue[-1]] <= num:
                queue.pop()
            queue.append(i)

            if queue[0] <= i - k:
                queue.popleft()

            if i >= k - 1:
                result.append(nums[queue[0]])

        return result



        # left, right = 0, k
        # current_max = max(nums[0:k])
        # output = [current_max]

        # while right < len(nums):
        #     if nums[left] == current_max:
        #         current_max = max(nums[left + 1:right + 1])
        #     elif nums[right] > current_max:
        #         current_max = nums[right] 
            
        #     output.append(current_max)
        #     left += 1
        #     right += 1

        # return output



        # left, right = 0, k
        # output = []

        # while right <= len(nums):
        #     local_max = max(nums[left:right])
        #     output.append(local_max)
        #     left += 1
        #     right += 1

        # return output

