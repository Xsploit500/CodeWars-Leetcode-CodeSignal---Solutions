class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        elements = [i for i in nums if i != 0]

        return len(set(elements))

        


        count = 0

        while sum(nums) > 0:
            x = float('inf')

            for i in range(len(nums)):
                if nums[i] != 0 and nums[i] < x:
                    x = nums[i]
            
            for i in range(len(nums)):
                if nums[i] > 0:
                    nums[i] = nums[i] - x
                else:
                    nums[i] = 0
            count += 1

        return count




        import heapq

        minheap = []

        count = 0

        def pushtoheap(minheap, arr):
            for i in arr:
                if i > 0:
                    heapq.heappush(minheap, i)

        pushtoheap(minheap, nums)

        while sum(nums) > 0:

            popped = heapq.heappop(minheap)

            for i in range(len(nums)):
                if nums[i] > 0:
                    nums[i] -= popped
            
            count += 1

            minheap = []
            
            pushtoheap(minheap, nums)

        return count