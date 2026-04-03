class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary(0, len(nums) - 1, nums, target)
     

    def binary(self, start:int, end:int, nums:List[int], target:int) -> int:
        index = (end + start) // 2
        middle = nums[index]
        if start > end:
            return -1
        elif middle == target:
            return index
        elif middle > target:
            return self.binary(start, index - 1 ,nums, target)

        return self.binary(index + 1, end ,nums, target)
    


        