# DOUBLY LINKED LIST SOLUTION:
class ListNode:
    def __init__(self, val=0, nextNode=None, prevNode=None):
        self.val = val
        self.next = nextNode
        self.prev = prevNode

        
class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        # Time: O(1)
        # Space: O(1)

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        
        if index <= self.size // 2:
            curr = self.head
            for _ in range(index + 1):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.prev
        return curr.val
        # Time: O(n) where n is the max distance between index and the beginning or end of the list
        # Space: O(1)
        
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        # Time: O(1)
        # Space: O(1)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
        # Time: O(1)
        # Space: O(1)
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        
        if index <= self.size // 2:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next
        else:
            succ = self.tail
            for _ in range(self.size - index):
                succ = succ.prev
            pred = succ.prev
        newNode = ListNode(val)
        newNode.prev = pred
        newNode.next = succ
        pred.next = newNode
        succ.prev = newNode
        self.size += 1
        # Time: O(n) where n is the max distance between index and the beginning or end of the list
        # Space: O(1)
        
    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        
        if index <= self.size // 2:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next.next
        else:
            succ = self.tail
            for _ in range(self.size - index - 1):
                succ = succ.prev
            pred = succ.prev.prev
        pred.next = succ
        succ.prev = pred
        self.size -= 1
        # Time: O(n) where n is the max distance between index and the beginning or end of the list
        # Space: O(1)