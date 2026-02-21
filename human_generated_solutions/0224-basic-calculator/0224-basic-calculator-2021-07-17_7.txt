class Solution:
    def calculate(self, s: str) -> int:
        
        def recurs(s, start):
            operand = result = 0
            nextSign = 1 # 1 for positive, -1 for negative (used to change sign of operand since we\'re always adding)
            i = start
            while i < len(s) - 1:
                i += 1
                c = s[i]
                
                if c == " ":
                    continue

                if c.isdigit():
                    # add digit to operand (could be multiple)
                    operand = 10 * operand + int(c)
                elif c == "(":
                    # new sub-expression - recurs
                    end, operand = recurs(s, i)
                    i = end
                elif c == ")":
                    # sub-expression ended - exit
                    break
                else:
                    # operator
                    result += nextSign * operand
                    nextSign = 1 if c == "+" else -1
                    operand = 0

            return i, result + (nextSign * operand)
        
        return recurs(s, -1)[1]