class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        import heapq
        import math

        maxheap = [-val for val in piles]
        heapq.heapify(maxheap)

        for _ in range(k):
            largest = -heapq.heappop(maxheap)
            new_val = largest - math.floor(largest / 2)
            heapq.heappush(maxheap, -new_val)

        return -sum(maxheap)



        

        def pushtoheap(piles):
            maxheap = []

            for val in piles:
                heapq.heappush(maxheap, -val)

            return maxheap

        heapified = pushtoheap(piles)

        while k > 0:
            popped_val = -heapq.heappop(heapified)
            result = popped_val - math.floor(popped_val / 2)
            heapq.heappush(heapified, -result)
            k -= 1

        return -sum(heapified)

        
        