class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        op_brackets = "({["
        close_brackets = ")}]"
        for ch in s:
            if ch in op_brackets:
                stack.append(ch)
            else:
                if len(stack) and op_brackets.find(stack[-1]) == close_brackets.find(ch):
                    stack.pop()
                else:
                    return False

        
        return len(stack) == 0