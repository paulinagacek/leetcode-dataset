class Solution:
      
    def calculate(self, s: str) -> int:

        stack = []
        num = 0 # Running number
        res = 0 # Running result
        sign = 1 # Running sign, 1 means positive, -1 means negative  

        for char in s:
            
            if char.isdigit():
                num = (num * 10) + int(char)

            elif char == \'+\':
                res += sign * num
                sign = 1
                num = 0

            elif char == \'-\':
                res += sign * num
                sign = -1
                num = 0

            elif char == \'(\':
                stack.append(res)
                stack.append(sign)

                num = 0
                sign = 1
                res = 0

            elif char == \')\':
                res += sign * num

                res *= stack.pop() # stack pop previously stored sign
                res += stack.pop() # stack pop previously stored operand

                num = 0

        return res + sign * num