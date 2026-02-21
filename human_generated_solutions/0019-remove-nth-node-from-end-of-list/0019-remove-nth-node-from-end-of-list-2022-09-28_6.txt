class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        sz, ptr = 0, head
        
        while ptr:
            ptr = ptr.next
            sz+=1

        if n==sz:
            return head.next

        sz -= n+1
        ptr = head 
          
        while sz > 0:
            ptr = ptr.next
            sz-=1
            
        ptr.next = ptr.next.next   
        
        return head