import sys
from operator import add,sub
from operator import itemgetter
import math
import random
 

TOTAL_N = 10000
PEOPLE_N = 100


def sigmoid(gamma):
    if gamma < 0:
        return 1 - 1 / (1 + math.exp(gamma))
    return 1 / (1 + math.exp(-gamma))


def get_cheater(matriz):

    S_p = []
    Q_p = None
    i_max = 10000
    maxi = 0
    maxi_ant = None
    
    for idx,i in enumerate(matriz):
        if Q_p is None:
            Q_p = i
        else:
            Q_p =  list(map(add, Q_p, i))
        S_p.append(sum(i))

    #S_p = list(map((1.0/TOTAL_N).__mul__, S_p))
    #Q_p = list(map((1.0/PEOPLE_N).__mul__, Q_p))

    scores = []
    for i in range(PEOPLE_N):
        f=list(map(lambda x:sigmoid(S_p[i]/TOTAL_N-x/PEOPLE_N)>0.5 if random.randint(0, 1)==0 else 1 ,Q_p))
        score = sum(1 for x,y in zip(f,matriz[i]) if x == y) / len(f)
        scores.append(score)
    index, element = max(enumerate(scores), key=itemgetter(1))

    return 1+index

T = int(input())
P = int(input())

for j in range(T):
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
    
    if j>P*T/100:
        ans = get_cheater(matriz)
    else:
        ans = random.randint(1,PEOPLE_N)

    if j != (T-1):
        print("Case #"+str(j+1)+": "+str(ans))
    else:
        print("Case #"+str(j+1)+": "+str(ans), end='')
            
            