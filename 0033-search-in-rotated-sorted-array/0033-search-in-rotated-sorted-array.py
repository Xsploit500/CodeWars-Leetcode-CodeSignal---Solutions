class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_min_index(nums):
            low, high = 0, len(nums) - 1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] < nums[high]:
                    high = mid
                elif nums[mid] > nums[high]:
                    low = mid + 1
                else:
                    return mid

        def binary_search(nums, target, left, right):
            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return -1

        min_index = find_min_index(nums)
        left_half = binary_search(nums, target, 0, min_index - 1)
        right_half = binary_search(nums, target, min_index, len(nums) - 1)

        if left_half != -1:
            return left_half
        elif right_half != -1:
            return right_half
        else:
            return -1





    # def search(self, nums: List[int], target: int) -> int:
    #     left, right = 0, len(nums) - 1

    #     while left <= right:
    #         mid = (left + right) // 2
    #         if nums[mid] == target:
    #             return mid
    #         if nums[left] <= nums[mid]:
    #             if nums[left] <= target < nums[mid]:
    #                 right = mid - 1
    #             else:
    #                 left = mid + 1
    #         else:
    #             if nums[mid] < target <= nums[right]:
    #                 left = mid + 1
    #             else:
    #                 right = mid - 1

    #     return -1