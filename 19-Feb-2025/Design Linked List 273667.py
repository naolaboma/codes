# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class MyLinkedList:
    def __init__(self):
        self.head = None  
    def get(self, index: int) -> int:
        if index < 0:
            return -1
        current = self.head
        ind = 0
        while current:
            if ind == index:
                return current.val
            current = current.next
            ind += 1
        return -1  
    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return
        if index == 0:
            self.addAtHead(val)
            return
        new_node = ListNode(val)
        current = self.head
        ind = 0
        while current and ind < index - 1:
            current = current.next
            ind += 1
        if not current:
            return  
        new_node.next = current.next
        current.next = new_node
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or not self.head:
            return
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        ind = 0
        while current.next and ind < index - 1:
            current = current.next
            ind += 1
        if not current.next:
            return 
        current.next = current.next.next
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)