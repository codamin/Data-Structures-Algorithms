def mines_num(numbers, n):
    dict = {}
    mines = [0]*n
    for i in range(len(numbers)):
        if numbers[i] not in dict:
            dict[numbers[i]] = 1
        else:
            dict[numbers[i]] += 1
    for i in range(len(numbers)):
        mines[i] = dict[numbers[i]]
    return mines

def next_greater_idx(mines):
    n = len(mines)
    ngx = [-1] * n
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
            



def main_f(numbers, n):
    mines = mines_num(numbers, n)
    ngis = next_greater_idx(mines)
    sol = []
    for i in range(len(ngis)):
        if(ngis[i] == -1):
            sol.append(-1)
        else:
             sol.append(numbers[ngis[i]])
    for i in range(len(sol)):
        print(sol[i],end = " ")




n = int(input())
numbers = input().split()
for i in range(n):
    numbers[i] = int(numbers[i])
main_f(numbers, n)