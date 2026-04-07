class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        for i in range(len(heights)):
            l , r  = i , i 
            min_height = heights[i]
            ans = max(ans, min_height)
            
            # just move until you see lesser height

            while l <= r:

                ans = max(ans, (r - l + 1) * min_height)

                if l - 1 >= 0 and heights[l - 1] >= min_height:
                    l = l - 1
                elif ((r + 1) < len(heights)) and heights[r + 1] >= min_height:
                    r = r + 1
                else:
                    break
            
        return ans



            


