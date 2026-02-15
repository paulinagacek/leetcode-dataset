def isHappy(self, n: int) -> bool:
        
        def getNext(n):
            tsum = 0
            while n>0:
                n,digit = divmod(n,10)
                tsum += digit**2
            return tsum
        
        slow = n
        fast = getNext(n)
        while fast!=1 and slow!=fast:
            slow = getNext(slow)
            fast = getNext(getNext(fast))
            
        return fast==1