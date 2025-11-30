import heapq
import sys

def task1_ege():
    print("Введите данные для задачи 1:")
    print("Формат: N M K C")
    print("города через пробел")
    print("M строк: u v t")
    
    try:
        first_line = input().strip().split()
        N, M, K, C = int(first_line[0]), int(first_line[1]), int(first_line[2]), int(first_line[3])
        
        cities = list(map(int, input().strip().split()))
        
        graph = [[] for _ in range(N+1)]
        for i in range(M):
            road_data = input().strip().split()
            u, v, t = int(road_data[0]), int(road_data[1]), int(road_data[2])
            graph[u].append((v, t))
            graph[v].append((u, t))
        
        dist = [float('inf')] * (N+1)
        dist[C] = 0
        heap = [(0, C)]
        
        while heap:
            current_dist, u = heapq.heappop(heap)
            if current_dist > dist[u]:
                continue
                
            for v, time in graph[u]:
                new_dist = current_dist + time
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(heap, (new_dist, v))
        
        results = []
        for city in cities:
            results.append((city, dist[city]))
        
        results.sort(key=lambda x: (x[1], x[0]))
        
        print("\nРезультат задачи 1:")
        for city, time in results:
            print(f"{city} {time}")
            
    except Exception as e:
        print(f"Ошибка ввода: {e}")

def task2_infrastructure():
    print("\nВведите данные для задачи 2:")
    print("Формат: N M")
    print("M строк: u v w")
    
    try:
        first_line = input().strip().split()
        N, M = int(first_line[0]), int(first_line[1])
        
        INF = 10**9
        dist = [[INF] * (N+1) for _ in range(N+1)]
        
        for i in range(1, N+1):
            dist[i][i] = 0
        
        for i in range(M):
            road_data = input().strip().split()
            u, v, w = int(road_data[0]), int(road_data[1]), int(road_data[2])
            dist[u][v] = min(dist[u][v], w)
            dist[v][u] = min(dist[v][u], w)
        
        for k in range(1, N+1):
            for i in range(1, N+1):
                for j in range(1, N+1):
                    if dist[i][k] < INF and dist[k][j] < INF:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        min_max_dist = INF
        best_site = 1
        
        for i in range(1, N+1):
            max_dist = 0
            for j in range(1, N+1):
                if dist[i][j] < INF:
                    max_dist = max(max_dist, dist[i][j])
            
            if max_dist < min_max_dist:
                min_max_dist = max_dist
                best_site = i
            elif max_dist == min_max_dist and i < best_site:
                best_site = i
        
        print("Результат задачи 2:")
        print(best_site)
        
    except Exception as e:
        print(f"Ошибка ввода: {e}")

if __name__ == "__main__":
    task1_ege()
    task2_infrastructure()