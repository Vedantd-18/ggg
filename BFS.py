graph = {
  'S' : ['A', 'B', 'C'],
  'A' : ['S', 'D'],
  'B' : ['D','G'],
  'C' : ['S', 'G'],
  'D' : ['A', 'G'],
  'G' : ['D']
}
visited = []
queue = []
goal = 'G'
def bfs(visited, graph, node):
    queue.append (node)
    visited.append(node)
    while queue:
        s = queue. pop (0)
        print (s, end = "\n")
        for neighbour in graph [s]:

          if neighbour not in visited:
            visited.append(neighbour)
            queue.append(neighbour)
            if goal is visited:
                break
bfs(visited,graph,'S')