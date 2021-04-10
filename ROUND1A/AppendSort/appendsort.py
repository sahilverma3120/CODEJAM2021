T = int(input())
import math


def get_value(number1,number2):
    cost = 0

    if number1 == number2:
        number2 = number2*10
        cost=1
    elif number2>number1:
        cost=0
    else:
        digit1 = int(math.log10(number1))
        digit2 = int(math.log10(number2))

        if  digit1 == digit2:
            cost+=1
            number2 = number2*10
        else:
            list1 = [int(i) for i in str(number1)]
            list2 = [int(i) for i in str(number2)]
            
            number2 = number2*10*(digit1-digit2)
            cost+= (digit1-digit2)

            while(int(math.log10(number2))<int(math.log10(number1))):
                number2=number2*10
                cost+=1
            if number2==number1:
                number2+=1
            elif number2<number1:
                digit2 = int(math.log10(number2))
                number2 = (number1-number2)+number1
                cost+= int(math.log10(number2))-digit2

    print(number1,number2,cost)
    
    return cost,number2

for j in range(T):

    n = int(input())
    lista = list(map(int,input().split()))
    back = lista[0]
    ans = 0
    for number in lista[1:]:
        cost,number= get_value(back,number)
        ans+=cost
        back=number

    if j != (T-1):
        print("Case #"+str(j+1)+": "+str(ans))
    else:
        print("Case #"+str(j+1)+": "+str(ans), end='')
            
            