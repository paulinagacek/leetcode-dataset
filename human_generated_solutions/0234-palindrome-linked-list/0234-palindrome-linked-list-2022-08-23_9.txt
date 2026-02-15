class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(node):
            prev = None
            while node:
                next_node = node.next
                node.next = prev 
                prev, node = node, next_node
                
            return prev
        
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        n1 = head
        n2 = reverse(slow.next)
        while n2:
            if n1.val != n2.val:
                return False
            
            n1 = n1.next
            n2 = n2.next
            
        return True