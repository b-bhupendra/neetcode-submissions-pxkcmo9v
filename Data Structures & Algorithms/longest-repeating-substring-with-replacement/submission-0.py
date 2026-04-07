class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)

        ans = 0

        l, r = 0 , 0

        while r < len(s):
            c = s[r]
            count[c] = 1 + count[c]

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                if count[l] == 0:
                    del count[l]
                l += 1
            ans = max(ans , r - l + 1)
            r += 1

        
        return ans