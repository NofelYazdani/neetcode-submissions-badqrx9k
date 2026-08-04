from _heapq import heapify
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key= lambda t: t[1]) #
        minheap = [] # end time, number of people 
        curr = 0
        for i in trips:
            numpass, start, end = i
            while minheap and minheap[0][0] <= start:
                curr -= minheap[0][1]
                heapq.heappop(minheap)
            curr += numpass
            if curr > capacity:
                return False
            heapq.heappush(minheap, [end, numpass])
        return True
        