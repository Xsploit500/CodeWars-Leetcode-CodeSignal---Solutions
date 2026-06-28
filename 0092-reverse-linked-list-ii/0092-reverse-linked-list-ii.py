# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse_list(head):
            if not head:
                return None
            prev, current = None, head
            while current is not None:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node

            return prev

        dummy = ListNode(0, head)
        prev_left = dummy
        l_val = head

        for _ in range(left - 1):
            prev_left = l_val
            l_val = l_val.next

        r_val = head
        for _ in range(right - 1):
            r_val = r_val.next

        node_after_right = r_val.next

        r_val.next = None

        reversed_sublist = reverse_list(l_val)
        prev_left.next = reversed_sublist

        l_val.next = node_after_right

        return dummy.next









        # dummy = ListNode(0, head)
        # prev = dummy

        # for _ in range(left - 1):
        #     prev = prev.next

        # sub_head = prev.next
        # curr = sub_head

        # sub_prev = None
        # for _ in range(right - left + 1):
        #     next_node = curr.next
        #     curr.next = sub_prev
        #     sub_prev = curr
        #     curr = next_node

        # prev.next = sub_prev
        # sub_head.next = curr

        # return dummy.next

                
        