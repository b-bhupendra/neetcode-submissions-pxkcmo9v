class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        for i,n in enumerate(nums):
            if target - n in mp:
                return [mp[target-n],i]
            
            mp[n] = i
        
        