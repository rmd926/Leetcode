# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        status = True

        while fast != slow or status:
            if not fast or not fast.next:
                return False
            
            fast = fast.next.next
            slow = slow.next
            status = False

        return True

# Runtime: 43 ms Beats 91.84 %
# Memory: 22.70 MB Beats 39.87 %
