# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        sub_head = prev.next
        curr = sub_head

        sub_prev = None
        for _ in range(right - left + 1):
            next_node = curr.next
            curr.next = sub_prev
            sub_prev = curr
            curr = next_node

        prev.next = sub_prev
        sub_head.next = curr

        return dummy.next

                
        