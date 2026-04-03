class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        for i in tokens:
            if i in operators:
                second = stack.pop()
                first = stack.pop()
                stack.append(int(float(eval(str(first) + str(i) + str(second)))))
            else:
                stack.append(i)
        return int(stack[-1])

            
        