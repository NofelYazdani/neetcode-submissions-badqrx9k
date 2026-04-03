class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub = nums[0]
        currentsum = 0
        for r in nums:
            currentsum = currentsum + r
            maxsub = max(maxsub, currentsum)
            if currentsum < 0:
                currentsum = 0
        return maxsub


        