#https://leetcode.com/problems/k-closest-points-to-origin/
import heapq

#we use a min heap queue (max heap by default in python, which is why we 
#put a - in front of the distance), which keeps track of the k minimum elements, since
#it has to keep the invariant min heap property
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for (x, y) in points:
            distance = -(x * x + y * y)
            if len(heap) == k:
                heapq.heappushpop(heap, (distance, x, y))
            else:
                heapq.heappush(heap, (distance, x, y))

        return [(x, y) for (distance, x, y) in heap]