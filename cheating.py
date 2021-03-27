import sys
from operator import add,sub
from operator import itemgetter
import math
import random
 
def sigmoid(gamma):
    if gamma < 0:
        return 1 - 1 / (1 + math.exp(gamma))
    return 1 / (1 + math.exp(-gamma))


T = int(input())

TOTAL_N = 10000
PEOPLE_N = 100

def get_cheater(matriz):

    S_p = []
    Q_p = [0 for i in range(TOTAL_N)]
    i_max = 10000
    maxi = 0
    maxi_ant = None
    
    for idx,i in enumerate(matriz):
        Q_p =  list(map(add, Q_p, i) )
        S_p.append(sum(i))

    S_p = list(map((1.0/TOTAL_N).__mul__, S_p))
    Q_p = list(map((1.0/PEOPLE_N).__mul__, Q_p))

    scores = []
    for i in range(PEOPLE_N):
        f=list(map(lambda x:sigmoid(S_p[i]-x)>0.5 if random.randint(0, 1)==0 else 1 ,Q_p))
        score = sum(1 for x,y in zip(f,matriz[i]) if x == y) / len(f)
        '''
        score= 0
        for idx in range(TOTAL_N):
            if f[idx]>0.5 and matriz[i][idx] ==1:
                score+=1
            elif f[idx]<=0.5 and matriz[i][idx] ==0:
                score+=0
        '''
        scores.append(score)

    index, element = max(enumerate(scores), key=itemgetter(1))

    return 1+index#np.argmax(scores)


for j in range(T):
    P = int(input())
    matriz1 = []
    matriz = []
    
    #'''
    for i in range(PEOPLE_N):
        texto = sys.stdin.readline().strip()#input().strip()#input()
        #print(len(lista))
        matriz1.append(texto)
    for texto in matriz1:
        lista = list(map(int,list(texto)))
        matriz.append(lista)
    
    ans = get_cheater(matriz)

    if j != (T-1):
        print("Case #"+str(j+1)+": "+str(ans))
    else:
        print("Case #"+str(j+1)+": "+str(ans), end='')
            
            