class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        for i in tokens:
            if i not in {"+","-","/","*"}:
                s.append(int(i))
            else:
                b,a=s.pop(),s.pop()
                if i=="+":s.append(a+b)
                elif i=="-":s.append(a-b)
                elif i=="*":s.append(a*b)
                else: s.append(trunc(a/b))
        return s[0]
