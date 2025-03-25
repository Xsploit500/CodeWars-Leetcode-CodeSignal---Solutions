class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        import heapq
        import math

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

        
        