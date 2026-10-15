class Solution:
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        m = { i : [] for i in range(numCourses)}
        for req in prerequisites:
            course, prereq = req[0], req[1]
            m[course].append(prereq)
        done = set()
      
      
        

        def dfs(course, path):
            if course in done:
                return True
            if course in path:
                return False

            path.add(course)
            
            for prereq in m[course]:
                if not dfs(prereq, path):
                    return False
            path.remove(course)
            done.add(course)
            return True

        for i in range(numCourses):

            if not dfs(i, set()):
                return False

        return True


