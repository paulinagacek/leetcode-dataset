# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head # firstly we are assigning heads to our pointers slow and fast. 
        while fast and fast.next:# Checking if head exixt or not as fast is head as we assigned earlier and by "fast.next" we are checking if we have some other element in the linked list or not. If we wont have then we are returing slow as it contains the head as well.
            slow = slow.next # Slow pointer is getting inceremented one by one & we are assiging immediate next value in it.
            fast = fast.next.next  # Fast pointer is getting incremented by 2 & we are assiging second next value to it.
            if fast == slow: # as described in the approach above.
                return True # If both pointer meet, implies there is a cycle.
        return False # If both pointer does meet, implies there is no cycle.