class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for st in strs:
            key = tuple(sorted(st))
            if key in group:
                group[key].append(st)
            else:
                group[key] = [st]
            
        ans = []
        for key, value in group.items():
            ans.append(value)

        return ans