
import sys


def salto_robot(m:int, k:int):
    if k > m:
        return 0
    else:
        matrix = [[0] * (m+1) for i in range(0, m)]
        matrix_conect = [[0] * (m+1) for i in range(0, m)]
        for i in range(0, m):
            for j in range(0,m+1):
                diff = (j-i)%k
                if i == 0 and diff == 0:
                    matrix[i][j] = 1
                elif i == j:
                    matrix[i][j] = 0
                elif k >= j or diff !=0:
                    matrix[i][j] = matrix[i-1][j]
                else:
                    matrix[i][j] = matrix[i-1][j] + matrix[i-1][i]
            k= (k+1)%998244353
        return matrix
m= salto_robot(7,1)
for p in m:
    print(p)
"""numero_casos = int(sys.stdin.readline())
for __ in range(numero_casos):
    caso = list(map(int, sys.stdin.readline().split()))
    m = caso[0]
    k = caso[1]
    if k >= 1 and k <= 10**5 :
        print(salto_robot(m, k))
    else:
        print('Error en los parametros iniciales')"""