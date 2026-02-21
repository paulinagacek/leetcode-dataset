class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i,j=head, head
        for k in range(n):
            j = j.next
        #now i and j will be at difference n
        if j == None: #Only happens when we are supposed to remove the first element
            return head.next
        while j.next != None:
            i = i.next
            j = j.next
        i.next = i.next.next
        return head