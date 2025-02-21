# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(-100)
        currn = dummy
        currn2 = dummy
        curro = head
        while curro:
            if curro.val < x:
                currn.next = ListNode(curro.val)
                currn = currn.next
            curro = curro.next
        curro = head
        while curro:
            if curro.val >= x:
                currn.next = ListNode(curro.val)
                currn = currn.next
            curro = curro.next
        return dummy.next