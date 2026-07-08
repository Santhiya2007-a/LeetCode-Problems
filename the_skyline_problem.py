class Solution(object):
    def getSkyline(self, buildings):
        events = []

        for l,r,h in buildings:
            events.append((l,-h,r))
            events.append((r,0,0))

        events.sort()
        res = []
        heap = [(0,float("inf"))]
        prev = 0

        for x,h,r in events:
            while heap[0][1] <= x:
                heapq.heappop(heap)

            if h:
                heapq.heappush(heap,(h,r))
            curr = -heap[0][0]

            if curr != prev:
                res.append([x,curr])
                prev = curr

        return res