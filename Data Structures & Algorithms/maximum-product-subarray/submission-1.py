class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        tracker = nums[0]
        running = nums[0]
        for i in range(1,len(nums)):
            temp_tracker = max(nums[i], tracker * nums[i], running * nums[i])
            running = min(nums[i], tracker * nums[i], running * nums[i])
            tracker = temp_tracker
            res = max(res, tracker)

        return res