class Graph:
    def __init__(self, n):
        self.V = n
        self.graph = [[] for _ in range(n)]

    def add_edge(self, u, v, w):
        self.graph[u - 1].append((v - 1, w))
        self.graph[v - 1].append((u - 1, w))

    def dijkstra(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0

        visited = [False] * self.V

        for _ in range(self.V):
            u = self.min_distance(dist, visited)
            visited[u] = True

            for v, w in self.graph[u]:
                if not visited[v] and dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w

        return dist

    def min_distance(self, dist, visited):
        min_dist = float('inf')
        min_index = -1

        for v in range(self.V):
            if dist[v] < min_dist and not visited[v]:
                min_dist = dist[v]
                min_index = v

        return min_index

def find_optimal_server(N, g, clients, min_max_latency):
    optimal_server = -1

    for node in range(N):
        distances = g.dijkstra(node)
        max_latency = max(distances[client - 1] for client in clients)
        if max_latency < min_max_latency:
            min_max_latency = max_latency
            optimal_server = node + 1

    return min_max_latency, optimal_server

def main():
    with open('gamesrv.in', 'r') as f:
        N, M = map(int, f.readline().split())
        clients = list(map(int, f.readline().split()))

        g = Graph(N)

        for _ in range(M):
            start, end, latency = map(int, f.readline().split())
            g.add_edge(start, end, latency)

    min_max_latency = float('inf')

    min_max_latency, optimal_server = find_optimal_server(N, g, clients, min_max_latency)

    with open('gamesrv.out', 'w') as outfile:
        outfile.write(str(min_max_latency) + "\n")
        outfile.write(str(optimal_server))

if __name__ == "__main__":
    main()
