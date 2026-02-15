class Solution:
    def judgeSquareSum(self, c: int) -> bool:
	    # If we take two integers a and b and we check if the sum of their squares equals c.
		# a and b lie within range (0, c**0.5) so we look in this range.
        l = 0
        r = int(c**0.5) # exponent to get the square root
        while l<=r:
            total = (l*l + r*r)
            if total == c:
                return True
            elif total > c:
                r-=1
            else:
                l+=1
        return False