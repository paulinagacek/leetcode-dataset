class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return 
        ret = pre = ListNode(0)
        ret.next = cur = head
        while(cur.next):
            nxt = cur.next
            if cur.val == nxt.val:
                while(nxt.next and nxt.val == nxt.next.val):
                    nxt = nxt.next
                pre.next = cur = nxt.next
                if not cur: return ret.next
            else:
                pre,cur,nxt = cur,nxt,nxt.next
            
            
        return ret.next