class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = list()
        for i,n in enumerate(nums):

            l , r = i + 1, len(nums) - 1

            while l < r:
                curSum = nums[i] + nums[l] + nums[r]

                if curSum > 0:
                    r -= 1
                elif curSum < 0:
                    l += 1
                else:
                    ans.append((nums[i] , nums[l] , nums[r]))
                    r -= 1
                    l += 1
        
        return [list(x) for x in list(set(ans))]

        