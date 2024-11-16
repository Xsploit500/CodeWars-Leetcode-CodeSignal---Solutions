class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        for _ in range(k):
            minimum = min(nums)
            index = nums.index(minimum)
            nums[index] = minimum * multiplier

        return nums



        
        import heapq

        minheap = nums[:]

        heapq.heapify(minheap)

        while k > 0:
            minimum = heapq.heappop(minheap)

            new_val = minimum * multiplier

            heapq.heappush(minheap, new_val)

            for i in range(len(nums)):
                if nums[i] == minimum:
                    nums[i] = new_val
                    break

            k -= 1

        return nums




        import heapq

        minheap = []

        def pushtoheap(minheap, elements):
            for i in nums:
                heapq.heappush(minheap, i)

        pushtoheap(minheap, nums)

        while k > 0:
            minimum = heapq.heappop(minheap)

            for i in range(len(nums)):
                if nums[i] == minimum:
                    nums[i] = minimum * multiplier
                    break
                          
            minheap = []
            pushtoheap(minheap, nums)

            k -= 1

        return nums