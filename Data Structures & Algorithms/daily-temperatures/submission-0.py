class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        st = []

        for i, temp in enumerate(temperatures):
            if not st:
                st.append(i)
                continue
            
            while st and temperatures[st[-1]] < temp:
                res[st[-1]] = abs(i - st[-1])
                st.pop()
            
            st.append(i)
        
        return res