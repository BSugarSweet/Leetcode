# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        dummy = ans

        stk = []
        while head:
            stk.append(head.val)
            head = head.next
        while stk:
            ans.next = ListNode(stk.pop())
            ans = ans.next
        return dummy.next