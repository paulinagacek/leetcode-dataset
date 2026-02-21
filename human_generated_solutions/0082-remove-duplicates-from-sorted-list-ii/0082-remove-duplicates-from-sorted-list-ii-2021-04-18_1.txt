def deleteDuplicates(self, head: ListNode) -> ListNode:
        # Base case
        if not head or not head.next:
            return head
        
        # Recursive case
        
        # No duplicate in the first part
        if head.next.val != head.val: 
            head.next = self.deleteDuplicates(head.next)
            return head
        
        # Duplicates exist in the first part
        cur = head
        while cur.next and cur.next.val == cur.val:
            cur = cur.next
        return self.deleteDuplicates(cur.next)