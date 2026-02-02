# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        dummy = ListNode(0, head) # 先在Linked list前面先加一個dummy node，雙指針slow走一步，fast走兩步
        slow = dummy
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next
        return dummy.next # 把dummy node略過去

# Runtime: 62 ms Beats 66.99 %
# Memory: 63.66 MB Beats 6.39 %
