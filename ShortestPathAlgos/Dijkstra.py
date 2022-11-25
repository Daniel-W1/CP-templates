def dijkstra(self, n, graph):
        distance = [float('inf') for _ in range(n+1)]
        distance[n] = 0
        heap = [(0, n)]
        visited = [False for _ in range(n+1)]
        
        while heap:
            dist, node = heappop(heap)
            visited[node] = True
            
            # first optimisation is this
            if dist > distance[node]: continue
            
            for neig in graph[node]:
                if visited[neig]: continue
                
                current_distance = dist + graph[node][neig]
                if current_distance < distance[neig]:
                    distance[neig] = current_distance
                    heappush(heap, (current_distance, neig))
                # relaxing all the neighbor edges
            
        return distance

# time comp O(V + ElogE)
# O(V)
