class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def buildgraph(edges):
            graph = {}

            for edge in edges:
                [a, b] = edge

                if a not in graph:
                    graph[a] = []
                if b not in graph:
                    graph[b] = []

                graph[a].append(b)
                graph[b].append(a)

            return graph
        
        graph = buildgraph(edges)
        visited = set()
        stack = [source]

        while stack:
            node = stack.pop()

            if node == destination:
                return True
            if node not in visited:
                visited.add(node)
                for neighbour in graph[node]:
                    if neighbour not in visited:
                        stack.append(neighbour)

        return False