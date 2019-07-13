def get_mat(n):
    mat = [0] * n 
    for i in range(0,n):
        mat[i] = [0] * n
        
    for i in range(n):
        row = input().split()
        for j in range(n):  
            mat[i][j] = int(row[j])
    return mat

def cal_max(mat,n):
    i = j = 0
    max = mat[i][j] + mat[i][j+1] + mat[i][j+2] + mat[i+1][j+1] + mat[i+2][j] + mat[i+2][j+1] + mat[i+2][j+2]
    for i in range(n-2):
        for j in range(n-2):
            sum = mat[i][j] + mat[i][j+1] + mat[i][j+2] + mat[i+1][j+1] + mat[i+2][j] + mat[i+2][j+1] + mat[i+2][j+2]
            if(sum > max):
                max = sum
    
    return max
        
    
n = 6
mat = get_mat(n)
print(cal_max(mat,n))



