def depth_first_search(graph, root, target):
  visited = [False for i in range(len(graph))]
  queue = [(root, [root])]

  while len(queue):
    vertex, path = queue.pop()
    visited[vertex] = True

    for edge in graph[vertex]:
      index = edge["to"]

      if index == target:
        return path + [index]

      if not visited[index]:
        queue.append((index, path + [index]))

  return None

graph = [
  [
    { "to": 1, "weight": 3 },
    { "to": 2, "weight": 1 },
  ],
  [
    { "to": 4, "weight": 1 },
  ],
  [
    { "to": 3, "weight": 7 },
  ],
  [],
  [
    { "to": 1, "weight": 1 },
    { "to": 3, "weight": 5 },
    { "to": 5, "weight": 2 },
  ],
  [
    { "to": 2, "weight": 18 },
    { "to": 6, "weight": 1 },
  ],
  [
    { "to": 3, "weight": 1 },
  ],
]

path = depth_first_search(graph, 0, 6)
print(path)

path = depth_first_search(graph, 0, 7)
print(path)
