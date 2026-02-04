# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        prev = dummy

        while prev.next:
            if prev.next.val != val:
                prev = prev.next
            else:
                prev.next = prev.next.next
        return dummy.next

# Runtime: 4 ms Beats 20.77 %
# Memory: 22.56 MB Beats 21.40 %
