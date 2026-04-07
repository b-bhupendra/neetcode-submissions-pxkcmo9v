class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp_s, mp_t = {} ,{}

        for c in s:
            mp_s[c] = 1 + mp_s.get(c,0)

        for c in t:
            mp_t[c] = 1 + mp_t.get(c,0)

        if len(mp_s) != len(mp_t):
            return False

        cpy_s = dict(mp_s)

        for k, v in cpy_s.items():
            if k in mp_t and v == mp_t[k]:
                del mp_t[k]
                del mp_s[k]
            else:
                return False



        



        return 0 == len(mp_s) and 0 == len(mp_t)        