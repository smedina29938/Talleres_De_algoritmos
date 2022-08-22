num=1

k=0

list=[]

while k<1000:
    k = ( num**2 + 1 )/num
    print ( k )
    list.append(num)
    num = num+1
    print( len ( list ))
    break
