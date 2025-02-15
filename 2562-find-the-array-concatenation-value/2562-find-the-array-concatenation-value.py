class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        output = 0

        left, right = 0, len(nums) - 1

        while left <= right:
            if left == right:
                output += int(nums[left])
            else:
                string_form = str(nums[left]) + str(nums[right])
                output += int(string_form)

            left += 1
            right -= 1

        return output