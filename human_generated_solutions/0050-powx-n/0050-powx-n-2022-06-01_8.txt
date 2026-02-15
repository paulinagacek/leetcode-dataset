class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: #if n is zero then result is always 1
          return(1.0)
        res = 1 # initializing res to 1
        t = abs(n) #storing n in a temporary variable to preserve its value
        while t != 0: #loop till t becomes zero
            if t%2 == 1: #checking if t is odd then we multiply res with x as discussed above in step (a).
                res *= x
            t >>= 1 #right shifting t so it will divide t by 2.
            x = x*x # calculating sq of x
       #Finally checking if n<0 (negative) then we return 1/res else res
	   if n < 0:
            return 1/res
        else:
            return res