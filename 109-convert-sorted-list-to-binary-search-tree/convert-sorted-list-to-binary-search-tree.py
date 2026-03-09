
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        def findMiddle(head):
            prev = None
            slow = fast = head

            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            
            if prev:
                prev.next = None
            
            return slow

        if not head:
            return None
            
        if head and not head.next:
            return TreeNode(head.val)

        mid = findMiddle(head)
        root = TreeNode(mid.val)

        root.left = self.sortedListToBST(head if mid != head else None)
        root.right = self.sortedListToBST(mid.next)

        return root
        