import sys


def saltoDivisorRobot(m, k):
    k_inicial = k
    suma = 0
    if k > m:
        return 0
    else:
        matrix = [[0] * (m+1) for i in range(0, m-k_inicial+1)]
        for x in range(0, len(matrix[0])):
            if x%k_inicial == 0:
                    matrix[0][x] = 1

        for i in range(0, len(matrix)):
            k = (k+1)%998244353
            for j in range(0,m-k_inicial+1):
                if i == j:
                    matrix[i][j] = 0 #Diagonal principal
                elif matrix[0][j] > 0:
                    if j > i and matrix[i][j] > 0 and i + 1 < m and j + k < len(matrix[0]) :
                        matrix[i+1][j + k] = (matrix[i+1][j + k] + matrix[i][j])%998244353
                    z = j
                    while z + k + k  < len(matrix[0]):
                        z += k    
                        matrix[i+1][z+k] =  (matrix[i+1][z+k] + matrix[i][j])%998244353
            suma += matrix[i][-1]

        return suma

numero_casos = int(sys.stdin.readline())
for __ in range(numero_casos):
    caso = list(map(int, sys.stdin.readline().split()))
    m = caso[0]
    k = caso[1]
    if k >= 1 and k <= 10**5 :
        print(saltoDivisorRobot(m, k))
    else:
        print('Error en los parametros iniciales')
