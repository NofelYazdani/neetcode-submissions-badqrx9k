class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for i, j in enumerate(nums):
            temp[j] = i
        for i, j in enumerate(nums):
            if (target - j) in temp and temp[target - j] != i:
                return [i, temp[target - j]]
        