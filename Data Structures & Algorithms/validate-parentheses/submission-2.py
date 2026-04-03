class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openpa = {"(" , "{", "["}
        closepa = {")": "(", "}": "{" , "]":"[" }
        for i in s:
            if i in openpa:
                stack.append(i)
            if i in closepa:
                if len(stack) > 0 and closepa[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        return False
        