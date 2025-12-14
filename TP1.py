import random as  r # aléatoire en python
# randit(a,b) : cette méthode génère 1 nb aléatoire entre a et b

## Exercice 1 :
# question 1
def mat(n,m):
    M=[]
    for i in range(0,n):
        C=[]
        for j in range(0,m):
            C.append(r.randint(0,5))
        M.append(C)
    return M
    
# question 2
def affichage(M):
    for e in M:
        print(e)
        
# question 3
def sommat(m1,m2):
    if len(m1)==leng(m2) and len(m1[0])==len(m2[0]): #si m1 et m2 ont le même nombre de lignes que de colonnes entre elles
        M=[]
        n = len(A)
        m = len(A[0])
        for i in range(0,n):
            C = []
            for j in range(0,m):
                C.append(m1[i][j] + m2[i][j])
            M.append(C)
        return M
    else:
        print('Veuillez mettre le même nombre de colonnes et de lignes pour vos 2 matrices')
        
# question 4
def echanger_ligne(A,a,b):
    for j in range(len(A[0])):
        temp = A[a][i]
        A[a][i] = A[b][i]
        A[b][i] = temp
    return A

# question 5
def echange_colonne(A,j1,j2):
    n = len(A)
    for i in range(0,n):
        temp = A[i][j]
        A[i][j1] = A[i][j2]
        A[i][j2] = temp
    return A
    
# question 6
def transpose(A):
    M = []
    n = len(A)
    m = len(A[0])
    for i in range(0,m):
        C = []
        for j in range(0,n): # attention ! on a inverser les n et m pour avoir les bonnes dimensions
            C.append(A[j][i])
        M.append(C)
    return M
    
# question 7
def produit(A,B):
    if len(A[0])==len(B):
        S = []
        for i in range(len(A)):
            C = []
            s = 0
            for j in range(len(B[0])):
                for k in range(len(B)):
                    s += A[i][k] * B[k][j]
                C.append(s)
            S.append(C)
        return S
                
# question 8
def presence(A,e):
    bool = False
    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            if e == A[i][j]:
                bool = True
    return bool

# question 9
def ligne(A, indice):
    M = []
    for j in range(0, len(A[indice])):
        M.append(A[indice][j])
    return M
            
# main
if __name__ == '___main__'
    m1 = [[1,2],[1,2]]
    m2 = [[3,4],[4,5]]
    m3 = [[1,2],[3,4],[5,6]]
    mat(4,5)
    print(mat(4,5))