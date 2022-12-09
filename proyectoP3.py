import sys
# Santiago Martînez Novoa 202112020
#Mar{ia Alejandra Estrada Garcîa 202021060
#Ernesto Carlos Perez Covo 202112530

def saltoDivisorRobot(m, k):
    suma = 0
    matrix = [[0] * (m+1) for i in range(0, m-k+1)]
    if k >m:
        return 0
    else:
        for x in range(0, len(matrix[0])):
            if x%k == 0:
                matrix[0][x] = 1

        for i in range(0, m+1):
            k += 1
            for j in range(0,m-k+1):
                if i == j:
                    matrix[i][j] = 0 #Diagonal principal
                
                if j > i and matrix[i][j] > 0 and i + 1 < m and j + k < len(matrix[0]) :
                    matrix[i+1][j + k] = (matrix[i+1][j + k] + matrix[i][j])%998244353
                    z = j
                    while z + k + k  < len(matrix[0]):
                        z += k    
                        matrix[i+1][z+k] =  (matrix[i+1][z+k] + matrix[i][j])%998244353
            if i<len(matrix):
                suma= (suma +  matrix[i][-1])%998244353
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
