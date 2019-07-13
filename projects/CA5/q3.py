def BFS(graph,f, t):
    v = len(graph)
    visited = [0] * v
    dist = [-1] * v
    q = []
    visited[f] = 1
    q.append(f)
    dist[f] = 0
    end = 0

    while not end and len(q) > 0:
        u = q[0]
        q.pop(0)

        for i in range(len(graph[u])):
            if not visited[graph[u][i]]:
                dist[graph[u][i]] = dist[u] + 1
                q.append(graph[u][i])
                visited[graph[u][i]] = 1
                if graph[u][i] == t:
                    end = 1
                    break
    
    return(dist[t])



n = int(input())
graph = [[] for x in range(20)]

for j in range(n):
    path = input().split()
    for i in range(len(path)):
        for j in range(len(path)):
            if j != i:
                graph[int(path[i])].append(int(path[j]))
        
ft = input().split()
f = int(ft[0])
t = int(ft[1])
# print(graph)
print(BFS(graph, f, t))