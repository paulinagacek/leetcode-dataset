class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i, X = 0, []
        for x in pushed:
            while X and X[-1] == popped[i]:
                X.pop()
                i += 1
            
            X.append(x)
        
        while X and X[-1] == popped[i]:
            X.pop()
            i += 1
        
        return not X