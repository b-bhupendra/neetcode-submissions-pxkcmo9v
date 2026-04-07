from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        # 1. Convert to compact list: (height, count)
        # This tracks sequential repetitions (e.g., [1,1,0,2,2] -> [(1,2), (0,1), (2,2)])
        compact = []
        for h in height:
            if compact and compact[-1][0] == h:
                compact[-1] = (h, compact[-1][1] + 1)
            else:
                compact.append((h, 1))
        
        total_water = 0
        # We use a stack to manage the "boundaries" and find dips (Steps 2-5)
        # The stack stores indices of the 'compact' list
        stack = []
        
        for i in range(len(compact)):
            # 2 & 5. If current height is greater than the previous (potential dip found)
            while stack and compact[i][0] > compact[stack[-1]][0]:
                # This is the "dip" (the floor of the container)
                mid_idx = stack.pop()
                
                if not stack:
                    break
                
                # 3. Boundaries
                left_idx = stack[-1]
                right_idx = i
                
                # Determine the height of the water level
                # height[px] > height[i] < height[c_y] 
                bounded_height = min(compact[left_idx][0], compact[right_idx][0]) - compact[mid_idx][0]
                
                # 4. Calculate interval (width)
                # We need the sum of all 'counts' between the left and right boundaries
                width = 0
                for k in range(left_idx + 1, right_idx):
                    # 6. Multiply by the "compacted" count to get the total area
                    width += compact[k][1]
                
                total_water += bounded_height * width
            
            stack.append(i)
            
        return total_water