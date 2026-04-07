class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        st = []

        for token in tokens:

            if token not in "+-*/":
                token = int(token)
                st.append(token)
            else:
                a = st.pop() 
                b = st.pop()

                match token:
                    case "*":
                        st.append(a*b)
                    case "+":
                        st.append(a+b)
                    case "-":
                        st.append(b - a)
                    case "/":
                        st.append(int(b / a))
        
        return st[-1]
                    
