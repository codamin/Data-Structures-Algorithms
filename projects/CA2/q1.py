def Gooni(n , from_elevator, to_elevator, with_elevator): 
    if n == 1: 
        print (from_elevator, to_elevator)
        return
    Gooni(n-1, from_elevator, with_elevator, to_elevator) 
    print(from_elevator, to_elevator)
    Gooni(n-1, with_elevator, to_elevator, from_elevator) 
          
n = int(input())
Gooni(n, 'A', 'C', 'B') 
