# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        status = True # first cycle occurs
        fast = head
        slow = head

        while fast != slow or status:
            if not fast or not fast.next: # 代表沒有cycle
                return None
               
            fast = fast.next.next
            slow = slow.next
            status = False
        
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        
        return fast

# Runtime: 50 ms Beats 61.59 %
# Memory: 22.53 MB Beats 18.89 %
