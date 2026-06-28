# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev, current = head, head.next

        while current is not None:
            prev.val, current.val = current.val, prev.val
            if not current.next:
                break
            prev = current.next
            current = prev.next

        return head