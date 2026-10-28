class Solution:


    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = { i : set() for i in range(1, len(edges) + 1)}
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)


        def dfs(node, path):
            if node in path:
                return False

            path.add(node)
           

            if len(path) == len(edges):
                return True

        

            for child in graph[node]:
                if dfs(child, path):
                    return True

           
            return False
            
            



        for i in range(len(edges) - 1, -1, -1):
            a, b = edges[i][0], edges[i][1]
            graph[a].remove(b)
            graph[b].remove(a)

            if dfs(1, set()):
                return edges[i]

            graph[a].add(b)
            graph[b].add(a)

        

            