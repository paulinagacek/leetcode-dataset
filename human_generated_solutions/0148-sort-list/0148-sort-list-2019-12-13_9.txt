# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def merge(self, plist1: ListNode, list1: ListNode, plist2: ListNode, list2: ListNode, n, n2: int):
        elist1 = list2
        pres = res = None
        pfirst = plist1
        first = list1
        n21 = n2
        while list1 != elist1 or n2 > 0:
            if list1 != elist1 and (n2 == 0 or list1.val <= list2.val):
                plist1 = list1
                list1 = list1.next
                if n2 == 0 and list1 == elist1:
                    pres = plist1
                    res = list1                  
            else:
                if list1 != elist1:
                    if not plist1 is None:
                        plist1.next = list2
                    if first == list1:
                        first = list2
                    plist1 = list2
                    if elist1 == list2:
                        elist1 = list2.next
                    plist2.next = list2.next
                    list2.next = list1
                    list2 = plist2.next
                else:
                    plist2 = list2
                    list2 = list2.next
                n2 -= 1
        return (first, plist2, list2) if pres is None else (first, pres, res)
                
    def sortList(self, head: ListNode) -> ListNode:
        n = 1
        l = 0
        if head is None or head.next is None:
            return head
        while l == 0 or n <= l // 2:
            pleft = None
            left = head
            pright = left
            right = head
            it = 0
            n2 = n
            while not left is None and not right is None:
                for j in range(n):
                    pright = right
                    right = right.next
                it += 2 * n
                if l > 0:
                    if l - it < 2 * n:
                        left, pright, right = self.merge(pleft, left, pright, right, n, n2)    
                        if pleft is None:
                            head = left
                        n2 = l - it                  
                elif not right.next is None and right.next.next is None:
                    n2 += 1
                    it += 1
                    if right.next.val < right.val:
                        right.next.next = right
                        pright.next = right.next
                        right.next = None
                        right = pright.next
                
                pright, right, left = self.merge(pleft, left, pright, right, n, n2)
                if pleft is None:
                    head = pright
                pleft = right
                right = left
            if l == 0:
                l = it
            n *= 2
        return head