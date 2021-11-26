def getmmin(numbers, n, k):
    min = 0
    for i in range(n):
        if(numbers[i]==1):
            min += 2
            for j in range(k):
                if(i + j >= n):
                    break
                if numbers[i+j] == 0:
                    numbers[i + j] = 2
                elif numbers[i + j] == 1:
                    numbers[i+j] = 0
                else:
                    numbers[i + j] = 1
        elif(numbers[i]==2):
            min += 1
            for j in range(k):
                if(i + j >= n):
                    break
                if numbers[i+j] == 0 or numbers[i+j] == 1:
                    numbers[i + j] += 1
                else:
                    numbers[i + j] = 0
    return min

def getmin2(numbers, n, k):
    mini = 0
    q = [(0,0)]
    to_add = 0
    for i in range(n):
        numbers[i] += to_add
        # mini += (3 - numbers[i]) % 3
        if(q[0][0] < i):
            numbers[i] -= q[0][1]
            to_add -= q[0][1]
            q.pop(0)
        mini += (3 - numbers[i]) % 3
        to_add += (3 - numbers[i]) % 3
        q.append((i+k-1,(3 - numbers[i]) % 3))
        numbers[i] = 0
    return mini
nk = input().split()
n = int(nk[0])
k = int(nk[1])
numbers = input().split()
for i in range(n):
    numbers[i] = int(numbers[i])
print(getmin2(numbers, n, k))

