class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = defaultdict(int)
        ans = 0
        l , r = 0 , 0
        if not len(s): return 0
        
        while r < len(s):
            
            window[s[r]] += 1 
            while window[s[r]] > 1:
                window[s[l]] -= 1
                if window[s[l]] == 0 :
                    del window[s[l]] 
                l += 1
    
            ans = max(ans , r - l + 1 )        
            r += 1
        
        return ans 


            
