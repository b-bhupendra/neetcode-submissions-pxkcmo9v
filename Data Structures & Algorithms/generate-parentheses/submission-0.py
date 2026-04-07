class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        tb_close = 0

        ans ,helper = [],[]

        def gen(m):
            nonlocal ans, helper , tb_close
            if m == 0 and tb_close == 0:
                ans.append(''.join(helper))
                return
            
            if m > 0:
                helper.append("(")
                tb_close += 1
                gen(m-1)
                tb_close -= 1
                helper.pop()
            
            if tb_close > 0:
                helper.append(")")
                tb_close -= 1
                gen(m)
                tb_close += 1
                helper.pop()
            
        gen(n)

        return ans


            







