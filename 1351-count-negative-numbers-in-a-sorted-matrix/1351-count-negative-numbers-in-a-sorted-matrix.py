class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        def helper(arr):
            left, right = 0, len(arr) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] < 0:
                    index = mid
                    right = mid - 1
                else:
                    left = mid + 1

            if index != -1:
                return len(arr) - index
            else:
                return 0

        for array in grid:
            count += helper(array)

        return count

