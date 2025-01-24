class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        count_remove = 0
        previous_end = float('-inf')

        for start, end in intervals:
            if start < previous_end:
                count_remove += 1
            else:
                previous_end = end

        return count_remove