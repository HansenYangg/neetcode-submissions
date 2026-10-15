class Solution:

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        0 : [1]
        1: [2]

        3: [4]


        0: [1]
        1: [2]
        2: [3]
        3: [4]


        '''
        graph = {i: [] for i in range(n)}
        for edge in edges:
            graph[edge[1]].append(edge[0])
            graph[edge[0]].append(edge[1])

        visited, connected = set(), 0

        def dfs(i):

            stack = [i]
            while stack:
                top = stack.pop()
                for child in graph[top]:
                    if child not in visited:
                        visited.add(child)
                        stack.append(child)

        
        print(graph)

        for i in range(n):
            if i not in visited:
                dfs(i)
                visited.add(i)
                connected += 1



        return connected