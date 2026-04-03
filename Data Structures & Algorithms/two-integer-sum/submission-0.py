class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        soultion = []
        for i, j in enumerate(nums):
            print(i,j)
            if target - j in hashmap:
                return [hashmap[target - j], i]
            else:
                hashmap[j] = i
                print(hashmap)
