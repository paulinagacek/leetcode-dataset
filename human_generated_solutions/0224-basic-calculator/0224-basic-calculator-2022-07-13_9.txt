class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operand = 0
        res = 0 # for the ongoing result
        sign = 1 # 1 means +ve, -1 means -ve
        
        for ch in s:
            if ch.isdigit():
                operand = operand * 10 + int(ch)
            
            
            elif ch == \'+\':
                #evaluate expression to the left
                res += sign * operand
                #save the sign
                sign = 1
                #reset operand
                operand = 0
            elif ch == \'-\':
                res += sign * operand
                sign = -1
                operand  = 0
            
            elif ch == \'(\':
                #push the result and then the sign
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            
            elif ch == \')\':
                res += sign * operand
                res *= stack.pop()
                res += stack.pop()
                operand = 0
        return res + sign*operand