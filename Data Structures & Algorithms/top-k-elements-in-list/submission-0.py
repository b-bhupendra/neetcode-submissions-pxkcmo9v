import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        hp = []
        
        for n in nums:
            
            if n in mp:
                mp[n] += 1
            else:
                mp[n] = 1
        
        for key, value in mp.items():
            heapq.heappush(hp,(-value,key))
        ans = []
        while k:
            ans.append(heapq.heappop(hp)[1])
            k -= 1
        
        return ans