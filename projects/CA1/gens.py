def func(gen):
    a = gen.count('A')
    c = gen.count('C')
    t = gen.count('T')
    g = gen.count('G')
    ln = len(gen)
    lenf = (ln)/4
    if(a == lenf and c == lenf and t == lenf and g == lenf):
        return 0
    mn = ln
    i = 0
    j = 0
    ap = 0
    cp = 0
    tp = 0
    gp = 0
    while (i<ln):
        if(a-ap<=lenf and c-cp<=lenf and t-tp<=lenf and g-gp<=lenf and i<j):
            # print(i,j,ap,tp,cp,gp)
            if(j-i < mn):
                mn = j-i
            if(gen[i] == 'A'):
                ap -= 1
            elif(gen[i] == 'T'):
                tp -= 1
            elif(gen[i] == 'C'):
                cp -= 1
            elif(gen[i] == 'G'):
                gp -= 1 
            i += 1
            continue
        if (j==ln):
            break
        if(gen[j] == 'A'):
            ap += 1
        elif(gen[j] == 'T'):
            tp += 1
        elif(gen[j] == 'C'):
            cp += 1
        elif(gen[j] == 'G'):
            gp += 1
        j += 1
    return mn
i = input()
gen = input()
print(func(gen))