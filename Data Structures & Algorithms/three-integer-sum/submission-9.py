class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []
        nums = sorted(nums)
        for i, j in enumerate(nums):
            if i > 0 and nums[i - 1] == j:
                continue
            l = i + 1
            r = len(nums) - 1
            while r > l:
                if nums[r] + nums[l] + j > 0:
                    r = r - 1
                elif nums[r] + nums[l] + j < 0:
                    l = l + 1
                else:
                    solution.append([j, nums[r], nums[l]])
                    r = r - 1
                    while nums[r] == nums[r + 1] and r > l:
                        r = r -1
        return solution

        