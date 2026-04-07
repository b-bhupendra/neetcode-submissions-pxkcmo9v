class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         mp = set()

         for x in nums:
            if x in mp:
                return True
            
            mp.add(x)

         return False