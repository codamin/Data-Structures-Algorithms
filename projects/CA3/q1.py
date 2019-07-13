def next_greater_idx(mines):
    n = len(mines)
    ngx = [n-1] * n
    s = []
    ind = []
    s.append(mines[0])
    ind.append(0)

    for i in range(1,n):
        j = i
        while len(s) != 0 and mines[i] > s[-1]:
            ngx[ind[-1]] = i
            s.pop()
            ind.pop()
            j -= 1
        s.append(mines[i])
        ind.append(i)
    return ngx

def last_greater_idx(mines):
    mines = mines[::-1]
    n = len(mines)
    ngx = [n-1] * n
    s = []
    ind = []
    s.append(mines[0])
    ind.append(0)

    for i in range(1,n):
        j = i
        while len(s) != 0 and mines[i] > s[-1]:
            ngx[ind[-1]] = i
            s.pop()
            ind.pop()
            j -= 1
        s.append(mines[i])
        ind.append(i)
    ngx = ngx[::-1]
    return ngx


            
def find_max(f, l):
    maxi = []
    for i in range(len(l)):
        maxi.append(max(abs(f[i]-i),abs(l[i]-(len(l)-1-i))))
    return maxi



n = int(input())
numbers = input().split()
for i in range(n):
    numbers[i] = int(numbers[i])
first = next_greater_idx(numbers)
last = last_greater_idx(numbers)
sol = find_max(first, last)
for i in range(len(sol)):
    print(sol[i],end = " ")

