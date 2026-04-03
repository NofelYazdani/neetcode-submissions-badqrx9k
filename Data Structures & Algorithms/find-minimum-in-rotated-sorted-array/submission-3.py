class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        start, end = 0, len(nums) - 1        
        while start <= end:
            middle  = (start + end) // 2
            if nums[middle] >= nums[start]:
                res = min(res, nums[start])
                start = middle + 1
            else:
                res = min (res, nums[middle])
                end = middle - 1
        return res
        