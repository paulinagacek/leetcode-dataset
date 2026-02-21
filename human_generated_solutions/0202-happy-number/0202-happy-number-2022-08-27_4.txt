def isHappy(self, n: int) -> bool:
        seen = set() # to store all the sum of square if digits
        while n != 1:
            sums = sum([int(digit)**2 for digit in str(n)]) # sum of square of digits
            if sums in seen: # if the sums in present in seen then it will be a endless loop
                return False
            n = sums
            seen.add(n)
        
        return True