class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operand = []

        for n in tokens:
            print(operand)
            if n not in "+/*-":
                operand.append(int(n))
            else:
                a , b = operand.pop(), operand.pop()

                if n == "+":
                    operand.append(a + b)
                if n == "-":
                    operand.append(b - a)
                if n == "/":
                    operand.append(int(b/a))
                if n == "*":
                    operand.append(a*b)
        
        return operand[-1]

        