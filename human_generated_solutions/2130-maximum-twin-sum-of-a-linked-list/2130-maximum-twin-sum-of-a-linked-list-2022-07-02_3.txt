class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        stack = []
        while fast:
            stack.append(slow.val)            
            slow = slow.next
            fast = fast.next.next
            
        result = -math.inf
        while slow:
            result = max(result, stack.pop() + slow.val)
            slow = slow.next
            
        return result