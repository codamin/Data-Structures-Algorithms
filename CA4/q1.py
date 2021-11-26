def dfs(graph, v, visits, maxLen):
    visits[v] = 1
    for i in range(len(graph[v])):
        if visits[graph[v][i]] == 0:
            dfs(graph, graph[v][i], visits, maxLen)
    maxLen[0] = max(maxLen[0], visits.count(1))
    visits[v] = 0


def hasPath(graph):
    v = len(graph)
    maxLen = [0]
    for i in range(v):
        visits = [0] * v
        if len(graph[i])!=0:
            dfs(graph, i, visits, maxLen)
            if maxLen[0] == v:
                return True
    return False

def addEdge(graph, v, w, e):
    graph[v].append(w)
    e[v] = 1
    e[w] = 1

def main():
    v = int(input())
    graph = [[] for x in range(v)]
    dic = {}
    for i in range(v):
        word = input()
        if 'end' + word[0] in dic:
            endingWithThis = dic['end' + word[0]]
            for j in endingWithThis:
                graph[j] += [i]
        if 'begin' + word[-1] in dic:
            graph[i] += dic['begin' + word[-1]]
        
        if 'begin' + word[0] in dic:
            dic['begin' + word[0]] += [i]
        else:
            dic['begin' + word[0]] = [i]
        if 'end' + word[-1] in dic:
            dic['end' + word[-1]] += [i]
        else:
            dic['end' + word[-1]] = [i]

    if hasPath(graph):
        print('possible')
    else:
        print('not possible')
if __name__ == "__main__":
    main()


