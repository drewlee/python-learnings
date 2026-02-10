def dfs_recursive(graph, vertex, target, visited, path):
  path.append(vertex)

  if target == vertex:
    return True

  visited[vertex] = True
  edges = graph[vertex]

  for i in range(len(edges)):
    if not visited[i] and edges[i] > 0:
      is_found = dfs_recursive(graph, i, target, visited, path)
      if is_found:
        return True

  path.pop()
  return False

def depth_first_search(graph, root, target):
  visited = [False for i in range(len(graph))]
  path = []
  is_found = dfs_recursive(graph, root, target, visited, path)

  if is_found:
    return path

  return None

graph = [
  [0, 3, 1,  0, 0, 0, 0],
  [0, 0, 0,  0, 1, 0, 0],
  [0, 0, 7,  0, 0, 0, 0],
  [0, 0, 0,  0, 0, 0, 0],
  [0, 1, 0,  5, 0, 2, 0],
  [0, 0, 18, 0, 0, 0, 1],
  [0, 0, 0,  1, 0, 0, 1],
]

result = depth_first_search(graph, 0, 6)
print(result)

result = depth_first_search(graph, 0, 7)
print(result)
