class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            if curr.val == val:  # cases 1-3
                if prev:  # cases 1-2
                    prev.next = curr.next
                else:  # case 3
                    head = curr.next
                curr = curr.next  # for all cases
            else:  # case 4
                prev, curr = curr, curr.next
        return head