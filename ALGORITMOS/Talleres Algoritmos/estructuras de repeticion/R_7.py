
x=int(input(" Incremento exp de monstruos "))
m=int(input(" Valor exp monstruos "))


while(0<x<=3): 
    if (10<=m<=(2**32)-1) and (0<x<=3):
        incremento=m*x
        print(incremento)
    elif x==0 and m==0:
        break 
