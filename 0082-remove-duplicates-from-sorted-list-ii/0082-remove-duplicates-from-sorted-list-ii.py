# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hmap = {}

        if not head:
            return None

        current = head

        while current:
            if current.val not in hmap:
                hmap[current.val] = 0
            hmap[current.val] += 1

            current = current.next

        current2 = head
        dummy = ListNode(None)
        tail = dummy

        while current2:
            if hmap[current2.val] == 1:
                node_val = ListNode(current2.val)
                tail.next = node_val
                tail = tail.next
            current2 = current2.next

        return dummy.next

        