class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for i in prerequisites:
            course, prereq = i
            adj[course].append(prereq)
        visited, cycle = set(), set()
        result = []
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)
            for i in adj[crs]:
                if dfs(i) == False:
                    return False
            result.append(crs)
            cycle.remove(crs)
            visited.add(crs)
            return True
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return result
     


            

