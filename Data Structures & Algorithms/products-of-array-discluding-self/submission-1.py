class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = [1]

        for i in range(0, len(nums) - 1):
            ans.append(ans[-1] * nums[i])

        print(ans)
        right = 1 * nums[-1]
        print(right)
        for i in range( len(nums) - 2 , -1, -1):
            ans[i] = ans[i] * right
            right *= nums[i]

        return ans