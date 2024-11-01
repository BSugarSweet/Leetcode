# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = head
        ans = head
        count = 0

        if head == None or head.next == None:
            return None

        while ans:
            count += 1
            ans = ans.next

        if count == n:
            return dummy.next

        ans = head
        for i in range(1, count - n):
            ans = ans.next

        if ans.next != None:
            ans.next = ans.next.next

        return dummy
        
            
        
