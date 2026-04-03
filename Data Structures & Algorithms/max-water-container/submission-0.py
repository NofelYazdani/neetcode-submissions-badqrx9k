class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        left = 0
        right = len(heights) - 1

        while right > left:
            area = min(heights[right], heights[left]) * (right - left)
            if area > maxarea:
                maxarea = area
            if heights[right] > heights[left]:
                left = left + 1
            elif heights[left] > heights[right]:
                right = right - 1
            else:
                left = left + 1
        return maxarea 

        