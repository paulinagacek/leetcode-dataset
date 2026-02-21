def using_two_pointers(self, head):
        if not head: return False
        slow = head
        fast = head.next
        while slow and fast and fast != slow and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow == fast
    
    
    def using_dict(self, head):
        mem = {}
        temp = head
        while temp:
            if temp in mem: return True
            else: mem[temp]= True
            temp = temp.next
        return False