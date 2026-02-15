#Baraa
class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        Good Example to check: 
        [8, 4, 2, 1, 3, 6, 7, 9, 5]
        
        STEP 1: we compare each number with number before it
        if current number > number before it we have to increment our reward
        i.e: res[i] = res[i - 1] + 1
        
        STEP 2: We compare same way but from end of the array to beggining of it
        if current number > number after it we increment if and only if there is a need to increment
        because maybe when we incremented in the first step we already gave more rewards for current number
        this can be observed in the above example 
        """
        
        n = len(ratings)
        res = [1] * (n)
        for i in range(1, n):
            if ratings[i] > ratings[i - 1] and res[i] <= res[i - 1]:
                res[i] = res[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and res[i] <= res[i + 1]:
                res[i] = res[i + 1] + 1
        return sum(res)