class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        if n == 1:
            return 1
        
		#stores the elements that are smaller than both its neighbors
        s = set()
        
        if ratings[0] <= ratings[1]:
            s.add(0) # first position
            
        if ratings[n-1] <= ratings[n-2]:
            s.add(n-1) # last position 
        
        for i in range(1, n-1):
            if ratings[i] <= ratings[i-1] and ratings[i] <= ratings[i+1]:
                s.add(i) # everything in between
  
        curr = 0
        count = [1] * n # start with everyone having one candy
        
        while s:
            curr += 1
            ns = set()
            
            for i in s:
                count[i] = curr
                if i != 0 and ratings[i-1] > ratings[i]:
                    ns.add(i-1) # add left neighbor if it is greater
                if i != n-1 and ratings[i+1] > ratings[i]:
                    ns.add(i+1) # add right neighbor if it is greater
            s = ns
            
        return sum(count)