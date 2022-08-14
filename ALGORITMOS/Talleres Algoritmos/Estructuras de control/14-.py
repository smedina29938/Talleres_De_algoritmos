lv = int ( input ( "Inserte la lectura anterior de kivolatios usados ​​" ))
la = int ( input ( "Inserte la lectura actual de kivolatios usados ​" ))
consumo = abs ( la - lv ) 

si ( consumo >= 0 ) o ( consumo <= 100 ):
    monto_pagar = ( consumo * 4600 ) 
elif ( consumo >= 101 ) o ( consumo <= 300 ):
    monto_pagar = ( consumo * 80.00 )
elif ( consumo >= 301 ) o ( consumo <= 500 ):
    monto_pagar = ( consumo * 100_000 )
elif ( consumo >= 501 ):
    monto_pagar = ( consumo * 120_000 )

print ( f" Monto final que debera pagar por el consumo de luz electrica y aseo urbano es de : { monto_pagar } " )

