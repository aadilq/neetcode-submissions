class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        
        minHeap = []

        currpassengers = 0

        for passengers, pickup, end in trips:
            while minHeap and minHeap[0][0] <= pickup:
                currpassengers -= minHeap[0][1]
                heapq.heappop(minHeap)
            currpassengers += passengers
            if currpassengers > capacity:
                return False
            heapq.heappush(minHeap, [end, passengers])
        return True
            


