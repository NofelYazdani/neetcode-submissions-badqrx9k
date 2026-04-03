class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq._heapify_max(nums)
        final = 0
        for _ in range(k):
            final = heapq.heappop_max(nums) 
        return final