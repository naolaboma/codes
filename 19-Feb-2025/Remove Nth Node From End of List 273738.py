# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        first = dummy
        second = dummy
        for _ in range(n + 1):
            first = first.next
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next
    def to_linked_list(lst):
        dummy = ListNode()
        current = dummy
        for value in lst:
            current.next = ListNode(value)
            current = current.next
        return dummy.next
    def to_list(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result