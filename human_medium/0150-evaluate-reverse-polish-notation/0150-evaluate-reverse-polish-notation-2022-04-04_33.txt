class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(["*", "+", "/", "-"])
        stack = []
        for token in tokens:
            if token in operators:
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                stack.append(eval(f"{op1}{token}{op2}"))
            else:
                stack.append(token)
        return int(stack[0])
