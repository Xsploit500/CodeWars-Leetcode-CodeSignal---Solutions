class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
        
        count = sorted(count.items(), key=lambda x: x[1], reverse=True)

        output = []

        for i in range(k):
            output.append(count[i][0])

        return output

        
        
        # count = {}
        # for num in nums:
        #     count[num] = count.get(num, 0) + 1

        # buckets = [[] for _ in range(len(nums) + 1)]
        # for val, freq in count.items():
        #     buckets[freq].append(val)

        # result = []
        # for freq in range(len(buckets) - 1, 0, -1):
        #     for val in buckets[freq]:
        #         result.append(val)
        #         if len(result) == k:
        #             return result

        # return result        