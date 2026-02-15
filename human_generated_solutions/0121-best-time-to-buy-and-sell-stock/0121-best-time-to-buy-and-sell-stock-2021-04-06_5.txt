def maxProfit(self, p):
        n = len(p)
        max_so_far = 0
        
        for i in range(n):
            for j in range(i+1,n):
                max_so_far = max(max_so_far, p[j] - p[i])
                
        return max_so_far