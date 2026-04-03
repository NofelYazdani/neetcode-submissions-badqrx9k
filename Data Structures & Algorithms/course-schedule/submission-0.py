class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {}
        for i in range(numCourses):
            courses[i] = []
        for crs, pre in prerequisites:
            courses[crs].append(pre)
        visit = set()
        def dfs(c):
            if c in visit:
                print("hello")
                return False
            if courses[c] == []:
                return True
            visit.add(c)
            for i in courses[c]:
                print(i)
                if not dfs(i):
                    return False
            visit.remove(c)
            courses[c] = []
            return True
        for i in courses:
            if not dfs(i):
                return False
        return True


            

        