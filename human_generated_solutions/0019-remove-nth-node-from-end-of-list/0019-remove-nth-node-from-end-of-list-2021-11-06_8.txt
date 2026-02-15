class Solution:
    def getLengthOfLL(self, head: Optional[ListNode]) -> int:
        length = 0
        
        while head:
            length += 1
            head = head.next
            
        return length
            
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        length = self.getLengthOfLL(temp)
        if n == length:
            return head.next
        
        if length == 1:
            return None
        
        i = 1
        
        while temp and i < (length - n):
            temp = temp.next
            i += 1
        
        temp.next = temp.next.next        
        return head