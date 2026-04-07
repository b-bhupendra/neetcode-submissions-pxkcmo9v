class Solution:
    def isPalindrome(self, s: str) -> bool:

        
        s = s.lower()
        #preprocessing
        ns = []
        for c in s:
            if c.isalnum():
                ns.append(c)
        
       

        ns = ''.join(ns)
        s = ns
        l , r = 0 , len(s) - 1
        print(ns)

        if len(s) in [1,0]:
            return True
        if len(s) == 2:
            return s[0] == s[1]
        while l < r and s[l] == s[r]:
            l+=1
            r-=1
            
        
        return abs(r - l) in [0, 1] and s[l] == s[r]
