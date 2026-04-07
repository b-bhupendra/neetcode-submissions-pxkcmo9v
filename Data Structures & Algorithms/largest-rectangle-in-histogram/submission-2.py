class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        n = len(heights)

        nb = self.nextBoundry(heights)
        pb = self.prevBoundry(heights)
        print(nb, pb)
        for i in range(len(heights)):
            ans = max(ans , heights[i] * ( nb[i] - pb[i] + 1 ) )

        return ans

    def nextBoundry(self, heights):
        stack = []
        n = len(heights)
        nb = [-1] * n 
        for i in range(n):
            
            if not stack:
                stack.append(i)
            elif heights[stack[-1]] <= heights[i]:
                stack.append(i)
            else:
                try:
                    while stack and heights[stack[-1]] > heights[i]:
                        nb[stack[-1]] = i - 1
                        stack.pop()

                    stack.append(i)
                except:
                    print(f"the problem at {stack} {i} {heights}")
        while stack:
            nb[stack[-1]] = n - 1
            stack.pop()

        return nb

    def prevBoundry(self, heights):
            stack = []
            n = len(heights)
            pb = [-1] * n 
            for i in range(n - 1, -1, -1):
                if not stack:
                    stack.append(i)
                elif heights[stack[-1]] <= heights[i]:
                    stack.append(i)
                else:                   
                    while stack and heights[stack[-1]] > heights[i]:
                        pb[stack[-1]] = i + 1
                        stack.pop()

                    stack.append(i)

            while stack:
                pb[stack[-1]] = 0
                stack.pop()

            return pb



            


