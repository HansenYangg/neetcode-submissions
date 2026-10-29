class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = { i : [] for i in range(numCourses)}
   

        for course, preReq in prerequisites:
            graph[course].append(preReq)
      


        done, path = set(), set()
        res = []
        def dfs(course):
   
            if course in path:
                return False

            if course in done:
                return True
            
        
            path.add(course)
            for preReq in graph[course]:
               
                if not dfs(preReq):
                    return False

            path.remove(course)
            done.add(course)
            res.append(course)

            
            return True



    

         

        for course in range(numCourses):
           
            if not dfs(course):
                return []

             

        return res


            


        

        
