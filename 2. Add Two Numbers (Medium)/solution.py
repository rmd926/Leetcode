# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        result = ListNode((l1.val + l2.val) % 10)
        result.next = self.addTwoNumbers(l1.next, l2.next)

        if l1.val + l2.val >= 10:
            result.next = self.addTwoNumbers(result.next, ListNode(1))
        
        return result

# Runtime: 7 ms Beats 29.71 %
# Memory: 19.52 MB Beats 16.73 %
