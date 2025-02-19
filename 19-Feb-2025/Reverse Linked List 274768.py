# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        res = res[::-1]
        dummy = ListNode()
        curr = dummy
        for valu in res:
            curr.next = ListNode(valu)
            curr = curr.next
        return dummy.next