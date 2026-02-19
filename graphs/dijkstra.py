from heapq import heappop, heappush

def dijkstras(graph, start):
  distances = {}
  paths = {}

  for vertex in graph:
    distances[vertex] = float('inf')

  distances[start] = 0
  vertices = [(0, start)]
  paths[start] = [start]

  while vertices:
    distance, current = heappop(vertices)

    for neighbor, weight in graph[current]:
      new_distance = distance + weight

      if new_distance < distances[neighbor]:
        distances[neighbor] = new_distance
        paths[neighbor] = paths[current] + [neighbor]
        heappush(vertices, (new_distance, neighbor))

  print(paths)

  return distances


if __name__ == '__main__':
  graph = {
    'A': [('B', 10), ('C', 3)],
    'C': [('D', 2)],
    'D': [('E', 10)],
    'E': [('A', 7)],
    'B': [('C', 3), ('D', 2)]
  }

  result = dijkstras(graph, 'D')
  print(f'Shortest Distances: {result}')

  # Graph for traveling salesperson problem.
  graph = {
    'a': [('b', 3), ('c', 4), ('d', 5)],
    'b': [('a', 3), ('c', 2), ('d', 6)],
    'c': [('a', 4), ('b', 2), ('d', 1)],
    'd': [('a', 5), ('b', 6), ('c', 1)]
  }

  result = dijkstras(graph, 'a')
  print(f'Shortest Distances: {result}')
