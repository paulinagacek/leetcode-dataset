class Solution:
    def romanToInt(self, s: str) -> int:
        sym = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        
        result = 0
        prev = 0
        
        for c in reversed(s):
            if sym[c] >= prev:
                result += sym[c]
            else:
                result -= sym[c]
            prev = sym[c]
            
        return result