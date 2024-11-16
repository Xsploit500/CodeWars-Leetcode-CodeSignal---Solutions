class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
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