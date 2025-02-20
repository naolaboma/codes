# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-101)
        dummy.next = head
        curr = dummy
        while curr.next and curr.next.next:
            if curr.next.val == curr.next.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next
