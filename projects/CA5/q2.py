def BFS(graph, sl, s):
    v = len(graph)
    visited = [0] * v
    q = []
    visited[0] = 1
    dist = [-1000] * v
    q.append(0)
    dist[0] = 0

    while len(q) > 0:
        u = q[0]
        q.pop(0)
        
        for i in range(len(graph[u])):
            if visited[graph[u][i]] == 0:            
                dist[graph[u][i]]  = dist[u] + 1
                q.append(graph[u][i])
                visited[graph[u][i]] = 1
    return(dist)

def getIndex(i, j, n, m):
    if (n-1-i)%2 == 0:
        idx = m*(n-i-1) + j
    else:
        idx = m*(n-i-1) + m-j-1
    return idx       

def main():
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    sl = [-2]*m*n

    graph = [[] for x in range(n*m)]

    c = input()
    while c != '-1 -1 -1':
        i = int(c.split()[0])
        j = int(c.split()[1])
        dest = int(c.split()[2])

        sl[getIndex(i, j, n, m)] = dest
        c = input()
        
    for i in range(m*n):
        for j in range(6):
            if(i+j+1 < m*n):
                if sl[i+j+1] != -2:
                    if sl[i+j+1] not in graph[i]:
                        graph[i].append(sl[i+j+1])
                        if sl[sl[i+j+1]] != -2:
                            graph[i][-1] = sl[sl[i+j+1]]
                elif i+j+1 not in graph[i]:
                    graph[i].append(i+j+1)
        

    # print(sl)
    print(BFS(graph,sl, 0)[-1])
    # print(graph)



if __name__ == "__main__":
    main()