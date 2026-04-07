class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # contains the tuple (index , left boundary)
        
        n = len(heights)

        ans = 0

        for i in range(n):
            
            if not stack:
                stack.append((i, i))
            else:
                left_bnd = i
                while stack and heights[stack[-1][0]] > heights[i]:
                    ans = max(ans , ( i - stack[-1][1] ) *  heights[stack[-1][0]] )
                    left_bnd = min(left_bnd, stack[-1][1])
                    stack.pop()
                stack.append((i, left_bnd))
        
        while stack:
            ans = max(ans , ( (n) - stack[-1][1] ) *  heights[stack[-1][0]] )
            stack.pop()
    
        return ans

            


