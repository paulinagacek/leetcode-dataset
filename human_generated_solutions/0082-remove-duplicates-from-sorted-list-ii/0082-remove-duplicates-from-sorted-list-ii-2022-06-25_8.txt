# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode()
        prev.next = head
        pv = prev
        hd = head
        while(hd and hd.next):
            if(hd.val==hd.next.val):
                while(hd):
                    if( hd.next==None or hd.val!=hd.next.val):
                        hd = hd.next
                        break
                    hd = hd.next
                prev.next = hd
            else:
                prev = prev.next
                hd = hd.next
        return pv.next