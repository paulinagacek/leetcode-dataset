def isHappy(self, n: int) -> bool:
              
        # to keep track of already seen digits
        seen = set()
        
        # keep the loop untill n is not already in seen
        # or a cycle is detected
        while (n not in seen):
            
            # add n to seen set
            seen.add(n)
            
            # variable to find the new number
            new = 0
            
            # iterate over each element of string(n)
            for ele in str(n):
                
                # add the square of each element
                new += int(ele) ** 2
                
            # check if new number found is 1 then return True
            if new == 1: return True
            
            # assign new number to n
            n = new
            
        # if the loop breaks then return False
        return False