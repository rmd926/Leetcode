# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        result = []
        while head:
            result.append(head.val)
            head = head.next
        if result == result[::-1]:
            return True
        else:
            return False
        
        return

# Runtime: 10 ms Beats 98.44 %
# Memory: 39.39 MB Beats 68.00 %       
