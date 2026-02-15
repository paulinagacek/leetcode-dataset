def hasCycle(self, head):
        if not head or not head.next:
            return False
        
        slow = head # slow mover pointer
        fast = head.next # fast mover pointer
        
        while fast != None and fast.next != None: # since the fast pointer is the leader; if there is an end it would be the fast who would hit the end first
            if slow == fast: # if they are equal the fast finsh the cycle and has catch the slow --> there is a cycle
                return True
            else:  # else just move slow one step and fast two step at a time
                slow = slow.next
                fast = fast.next.next
        return False # if the fast hit the end, there is no cycle