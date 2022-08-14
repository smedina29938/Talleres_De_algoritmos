valor_total = int (input ( "digite el valor de la compra" ))

capital = ( valor_total * 0.55 ) 
banco = ( valor_total * 0.3 )
credito = ( valor_total * 0.15 )
interes = ( credito * 0.2 )

capital2 = ( valor_total * 0.7 )
credito2 =( valor_total * 0.30 )
interes2 = ( credito2 * 0.2 )

elif valor_total > 5000000 :
    print ( f"valor de la inversion de los fondos: {capital}" )
    print ( f"valor a pagar en el credito: {banco + credito}" )
    print ( f"valor a pagar en interes: {interes}" )
    print ( f"valor prestado por el banco: {banco}" )
any:
    print ( f"valor de la inversion de los fondos: {capital2}" )
    print ( f"valor a pagar en el credito: {banco + credito2}" )
    print ( f"valor a pagar en interes: {interes2}" )
    print ( f"valor prestado por el banco: {banco}" )
