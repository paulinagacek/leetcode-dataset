class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head
        
    def getRandom(self) -> int:
        reservoir = self.head.val
        
        i = 2
        next = self.head.next
        while next:
            if random.random() < 1/i:
                reservoir = next.val
                
            i += 1
            next = next.next
            
        return reservoir