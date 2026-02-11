from heapq import heappop, heappush

graph = {
          'A': [('B', 10), ('C', 3)],
          'C': [('D', 2)],
          'D': [('E', 10)],
          'E': [('A', 7)],
          'B': [('C', 3), ('D', 2)]
        }

def dijkstras(graph, start):
  distances = {}

  for vertex in graph:
    distances[vertex] = float("inf")

  distances[start] = 0
  vertices = [(0, start)]

  while vertices:
    distance, current = heappop(vertices)

    for neighbor, weight in graph[current]:
      new_distance = distance + weight

      if new_distance < distances[neighbor]:
        distances[neighbor] = new_distance
        heappush(vertices, (new_distance, neighbor))

  return distances

distances_from_d = dijkstras(graph, 'D')
print(f"Shortest Distances: {distances_from_d}")
