import queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  print("BFS: ")
  while queue:
    s = queue.pop(0)
    print (s, end = " ")

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : [],
  'F' : []
}

visited = []
queue = []
bfs(visited, graph, 'A')