# sample test : ok
# test 1 : ok

from itertools import permutations 
import numpy as np
T = int(input())

def reversort(lista):
    #if len(lista)==1:
    #    return 1
    suma = 0
    for i in range(len(lista)-1):
        j = i+np.argmin(lista[i:])
        #print(i,j,lista,lista[i:j][::-1])
        lista[i:(j+1)] = lista[i:(j+1)][::-1]
        suma += (j-i)
        suma += 1
        
        #print(i,j,j-i+1,lista)
    return suma


for j in range(T):
    lista = list(map(int,input().split()))
    N = int(lista[0])
    C = int(lista[1])
    
    min_c = N-1
    max_c = (N*(N+1))/2-1
    
    if C>max_c or C<min_c:
        ans = 'IMPOSSIBLE'
    else:
  
        perm = permutations([i for i in range(1,N+1)]) 
        for i in list(perm):
            suma = reversort(list(i).copy())
            if suma == C:
                ans = list(i)
                break    

    if ans != 'IMPOSSIBLE':
        texto = ''
        for i in ans:
            texto+=str(i)+' '
        ans = texto[:-1]
    if j != (T-1):        
        print("Case #"+str(j+1)+": "+str(ans))
    else:
        print("Case #"+str(j+1)+": "+str(ans), end='')
            
            
