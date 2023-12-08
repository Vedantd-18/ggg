graph = {
  'S': ['A', 'B', 'C'],
  'A': ['S', 'D'],
  'B': ['D', 'G'],
  'C': ['S', 'G'],
  'D': ['A', 'G'],
  'G': ['D']
}
visited = []
goal = 'G'

def dfs(visited, graph, node):
    visited.append(node)
    print(node, end="\n")

    if node == goal:
        return True

    for neighbour in graph[node]:
        if neighbour not in visited:
            if dfs(visited, graph, neighbour):
                return True

    return False

dfs(visited, graph, 'S')
