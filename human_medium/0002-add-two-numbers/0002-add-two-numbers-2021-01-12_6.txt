class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        carry = 0
        curr = dummyHead
        
        while l1 or l2:
            if l1:
                l1_val = l1.val
            else:
                l1_val = 0
            if l2:
                l2_val = l2.val
            else:
                l2_val = 0
            
            sum_ = l1_val + l2_val + carry
            
            curr.next = ListNode(sum_ % 10)
            curr = curr.next
            carry = sum_ // 10
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry:
            curr.next = ListNode(carry)
        
        return dummyHead.next
