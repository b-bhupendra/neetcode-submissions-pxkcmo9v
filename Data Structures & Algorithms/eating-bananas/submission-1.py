class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def at_Speed_K_Hrs_Taken(piles, i):
            
            hrs_elasped = 0
            for n in piles:
                hrs_elasped += math.ceil(n / i)

            return hrs_elasped

        l = 1
        r = 1e9
        ans = float('inf')
        while l <= r:
            mid = ( l + r ) // 2
            taken = at_Speed_K_Hrs_Taken(piles, mid)
            if taken <= h:
                ans = min(mid, ans)
                # we had one of condition covered bananas eaten under the h hrs
                # we can now find tighter bound
                r = mid - 1
            else:
                l = mid + 1
            
        return int(ans)

