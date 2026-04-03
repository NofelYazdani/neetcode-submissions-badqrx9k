class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = []
        result = max(piles)
        start, end = 1, max(piles)
        while start <= end:
            middle = (start + end) // 2
            total_time = 0
            for i in piles:
                total_time = total_time + math.ceil(float(i)/middle)
            if total_time <= h:
                result = min(middle, result)
                end = middle - 1
            elif total_time > h:
                start = middle + 1
            else:
                return middle
        return result 

        

        