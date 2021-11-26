def get_max(maxW , i): 

    if i == 0 or maxW == 0 : 
        return 0
    if (ws[i-1] > maxW): 
        return get_max(maxW, i-1) 
    else: 
        return max(values[i-1] + get_max(maxW-ws[i-1], i-1), get_max(maxW, i-1)) 

mx = 0
wSum = 0
valSum = 0
maxw = int(input().split()[0])
values = input().split()
for i in range(len(values)):
    values[i] = int(values[i])
ws = input().split()
ws_len = len(ws)
for i in range(len(ws)):
    ws[i] = int(ws[i])


print(get_max(maxw, ws_len))

