class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:  # Time: O(n) and Space: O(1)
        prev, cur = None, head
        while cur:               # let cur 3 
            temp = cur.next      # nxt = 4
            cur.next = prev      # 3 -> 2
            prev = cur           # prev = 3
            cur = temp           # 5 <- cur(4) <- 3(prev) -> 2 -> 1 -> Null
        return prev