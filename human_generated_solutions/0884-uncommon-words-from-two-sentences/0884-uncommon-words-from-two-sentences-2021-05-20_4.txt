class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        uncommon = []
        
        def find_uncommon(s , t):
            ans = []
            for i in s:
                if(s.count(i) == 1 and i not in t):
                    ans.append(i)
            
            return ans
        
        return find_uncommon(A.split() , B.split()) + find_uncommon(B.split() , A.split())