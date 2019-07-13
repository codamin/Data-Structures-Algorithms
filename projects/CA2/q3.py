def prefix(names, x, st):
    yes = 1
    for i in range(len(names) - 1):
        if(len(names[i]) < x + 1 or len(names[i + 1]) < x + 1):
               return st
        if(names[i][x] != names[i+1][x]):
            yes = 0
            return st
    return prefix(names, x+1, st + names[0][x])

n = input()
names = input().split()
for i in range(len(names)):
    names[i] = names[i].lower()
res = prefix(names,0,'')
if(res == ''):
    print('NULL')
else:
    print(res)

