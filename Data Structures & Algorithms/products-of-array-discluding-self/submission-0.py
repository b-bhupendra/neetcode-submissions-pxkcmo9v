class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left = [1]

        for i in range(0, len(nums) - 1):
            left.append(left[-1] * nums[i])

        right = [1]

        for i in range( len(nums) - 1 , 0, -1):
            right.append(right[-1]  *nums[i])
        
        right = right[::-1]

        print(left)
        print(right)
        return [ left[i] * right[i] for i in range(len(nums))]