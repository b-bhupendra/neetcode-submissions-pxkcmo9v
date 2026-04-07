class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = defaultdict(int)

        for i, n in enumerate(numbers):
            
            if target - n in mp:
                return [mp[target-n] + 1, i + 1]
            
            mp[n] = i
        