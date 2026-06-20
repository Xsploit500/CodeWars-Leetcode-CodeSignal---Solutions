# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        connected_components = 0

        nums = set(nums)

        current = head

        while current:
            if current.val in nums:
                if current.next is None or current.next.val not in nums:
                    connected_components += 1

            current = current.next

        return connected_components