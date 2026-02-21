class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head==None:
            return None
        
        dummy=ListNode(0)
        dummy.next=head
        
        cur=head
        prev=dummy
        
        dup=0
        
        while cur!=None and cur.next!=None:
            if cur.val==cur.next.val:
                cur=cur.next
                dup=1
            else:
                if dup==1:
                    prev.next=cur.next
                    cur=cur.next
                    dup=0
                else:
                    prev=cur
                    cur=cur.next
        if dup==1:
            prev.next=cur.next
            cur=cur.next
            
        return dummy.next