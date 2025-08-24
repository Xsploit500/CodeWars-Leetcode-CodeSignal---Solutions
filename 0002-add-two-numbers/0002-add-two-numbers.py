# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        traverse1, traverse2 = "", ""

        curr1 = l1

        while curr1:
            traverse1 += str(curr1.val)
            curr1 = curr1.next

        curr2 = l2

        while curr2:
            traverse2 += str(curr2.val)
            curr2 = curr2.next
        
        digit1, digit2 = int(traverse1[::-1]), int(traverse2[::-1])

        total = list(str(digit1 + digit2))

        # Building back the linkedlist

        if not total:
            return None

        outputhead = ListNode(int(total[len(total) - 1]))
        current = outputhead

        for i in range(len(total) - 2, -1, -1):
            current.next = ListNode(int(total[i]))
            current = current.next

        return outputhead
