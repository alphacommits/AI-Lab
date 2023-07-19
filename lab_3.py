def dfs(visited, graph, node):
  visited.add(node)
  stack.append(node)

  print("DFS: ")
  while stack:
    s = stack.pop()
    print (s, end = " ")

    for neighbour in reversed(graph[s]):
      if neighbour not in visited:
        visited.add(neighbour)
        stack.append(neighbour)
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}
visited = set()
stack = []
dfs(visited, graph, 'A')