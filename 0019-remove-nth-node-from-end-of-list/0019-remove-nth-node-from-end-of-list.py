# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverse_list(head, prev=None):
            if not head:
                return prev
            next = head.next
            head.next = prev
            return reverse_list(next, head)
        
        def remove_node(head):
            head = reverse_list(head, None)

            count = n - 1
            prev, current = None, head
            while current:
                if count == 0:
                    if prev is None:
                        head = current.next
                    else:
                        prev.next = current.next
                    break
                prev = current
                current = current.next
                count -= 1
            return head

        output = reverse_list(remove_node(head))
        return output

