from queue import PriorityQueue

input_file = "input.txt"  # файл с данными
INF = 9999


def dijkstra(graph: dict, start_v: int):
    distances = {vertex: INF for vertex in graph.keys()}
    distances[start_v] = 0
    visited = set()
    pq = PriorityQueue()
    pq.put((0, start_v))

    while not pq.empty():
        cur_d, cur_v = pq.get()
        visited.add(cur_v)

        for adj_v in graph[cur_v]:
            if adj_v in visited:
                continue
            new_d = distances[cur_v] + 1
            if distances[adj_v] > new_d:
                distances[adj_v] = new_d
                pq.put((new_d, adj_v))

    return distances


with open(input_file, 'r') as f:
    N, M = map(int, f.readline().split())
    adj_list = {v: [] for v in range(N)}
    for _ in range(M):  # задаём словарём, т.к в нём доступ тоже за О(1)
        v1, v2 = map(int, f.readline().split())
        adj_list[v1 - 1].append(v2 - 1)
    s1_size = int(f.readline())  # повторяющийся код, пока не знаю как исправить
    s1 = set([elem - 1 for elem in map(int, f.readline().split())])
    s2_size = int(f.readline())
    s2 = set([elem - 1 for elem in map(int, f.readline().split())])

answer = []
for vertex in range(N):
    dijkstra_result = dijkstra(adj_list, vertex)
    # удаляем недоступные вершины
    available_vertices = {vertex: distance for vertex, distance in dijkstra_result.items() if distance != INF}
    # смотрим какие вершины достижимы из заданных множеств
    s1_tmp = set(available_vertices.keys()).intersection(s1)
    s2_tmp = set(available_vertices.keys()).intersection(s2)
    if s1_tmp and s2_tmp:
        resulted_distance = min(available_vertices[v] for v in s2_tmp)
        resulted_distance += min(available_vertices[v] for v in s1_tmp)
        answer += [(vertex, resulted_distance)]

for vertex, distance in sorted(answer, key=lambda elem: elem[1]):
    print(vertex + 1)
