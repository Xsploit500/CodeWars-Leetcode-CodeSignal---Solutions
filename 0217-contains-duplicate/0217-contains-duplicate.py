class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_nums = nums.sort()

        left, right = 0, 1

        while right < len(nums):
            if nums[left] == nums[right]:
                return True
                break
            left += 1
            right += 1

        return False



        return len(nums) != len(set(nums))
        