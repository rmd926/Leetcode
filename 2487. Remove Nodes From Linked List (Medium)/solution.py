# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        
        stack = []
        for num in nums:
            while stack and stack[-1] < num:
                stack.pop()
            stack.append(num)
        
        dummy = ListNode()
        head = dummy
        for num in stack:
            head.next = ListNode(num)
            head = head.next
        
        return dummy.next

# Runtime: 139 ms Beats 29.01 %
# Memory: 73.28 MB Beats 5.40 %
