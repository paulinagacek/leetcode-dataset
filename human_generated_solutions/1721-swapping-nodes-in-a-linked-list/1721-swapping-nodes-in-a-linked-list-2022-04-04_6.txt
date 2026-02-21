# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        front, last = head,head
        while k>1:
            front = front.next
            k-=1
        left = front
        while left.next!=None:
            left = left.next
            last = last.next
        front.val, last.val = last.val, front.val
        return head