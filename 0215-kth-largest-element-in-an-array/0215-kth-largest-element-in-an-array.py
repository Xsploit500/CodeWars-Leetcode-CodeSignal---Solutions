class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        maxheap = []

        for num in nums:
            heapq.heappush(maxheap, -num)

        for _ in range(k):
            popped = -heapq.heappop(maxheap)

        return popped