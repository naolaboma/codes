# Problem: Reverse Linked List II - https://leetcode.com/problems/reverse-linked-list-ii/description/

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for _ in range(left - 1):
            pre = pre.next
        start = pre.next
        then = start.next
        for _ in range(right - left):
            start.next = then.next
            then.next = pre.next
            pre.next = then
            then = start.next
        return dummy.next