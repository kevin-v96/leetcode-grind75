#https://leetcode.com/problems/course-schedule/
class Solution:
    def buildAdjacencyList(self, n, edgesList):
        adjList = [[] for _ in range(n)]
        for c1, c2 in edgesList:
            adjList[c2].append(c1)
        return adjList

    def getTopoOrder(self, numNodes: int, edgesList: List[List[int]]) -> bool:
        adjList = self.buildAdjacencyList(numNodes, edgesList)
        inDegrees = [0] * numNodes
        for v1, v2 in edgesList:
            inDegrees[v1] += 1
        
        queue = []
        for v in range(numNodes):
            if inDegrees[v] == 0:
                queue.append(v)

        count = 0
        topoOrder = []

        while queue:
            v = queue.pop(0)
            topoOrder.append(v)

            count += 1
            for des in adjList[v]:
                inDegrees[des] -= 1
                if inDegrees[des] == 0:
                    queue.append(des)

        if count != numNodes:
            return None
        else:
            return topoOrder

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return bool(self.getTopoOrder(numCourses, prerequisites))