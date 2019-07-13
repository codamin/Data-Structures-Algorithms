def one(numList, max):
    count = 0
    books = []
    for i in range(len(numList)):
        if numList[i] not in books:
            count += 1
            if(len(books) < max):
                books.append(numList[i])

            else:
                books = books[1:len(books)]
                books.append(numList[i])
    return count

def two(numList, max):
    count = 0
    books = []
    new = []
    for i in range(len(numList)):
        if numList[i] not in books:
            count += 1
            if(len(books) < max):
                books.append(numList[i])
            else:
                max_idx = 0
                new = numList[i + 1 : len(numList)]
                max_idx_later = 0
                
                for j in range(len(books)):
                    if books[j] not in new:
                        max_idx = j
                        break
                    elif(new.index(books[j]) > max_idx_later):
                        max_idx_later = new.index(books[j])
                        max_idx = j

                books[max_idx] = numList[i]


    return count

def three(numList, max):
    count = 0
    books = []
    for i in range(len(numList)):
        if numList[i] not in books:
            count += 1
            if(len(books) < max):
                books.append(numList[i])

            else:
                books = books[1:len(books)]
                books.append(numList[i])

        else:
            books.remove(numList[i])
            books.append(numList[i])
            
    return count


numList= input().split('-')
numList = list(map(int, numList))
maxBook = int(input())
method = int(input())
if method == 1 :
    print(one(numList, maxBook))
elif method == 2 :
    print(two(numList, maxBook))
elif method == 3 :
    print(three(numList,maxBook))



