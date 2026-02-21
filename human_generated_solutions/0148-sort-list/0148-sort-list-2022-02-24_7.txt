class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = head
        while count:
            itr = head
            while itr.next:
                if itr.val > itr.next.val: 
                    itr.val, itr.next.val = itr.next.val, itr.val
                itr = itr.next
            count = count.next
        return head