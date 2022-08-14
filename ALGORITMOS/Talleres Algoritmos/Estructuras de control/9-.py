nombre_c = str (input("digite el nombre del cliente"))
valor_compra = int (input( "digite el valor de la compra"))

valor_pagar = ""
elif (valor_compra < 50000):
    valor_pagar = ( valor_compra)
elif (valor_compra >= 50000 y valor_compra <= 100000 ):
    valor_pagar = ( valor_compra - (valor_compra * 0.05))
elif (valor_compra > 100000 y valor compra <= 700000):
    valor_pagar =(valor_compra - (valor_compra *0.11)):
elif ( valor_compra > 700_000  y  valor_compra <=  1_500_000 ):
    valor_pagar = ( valor_compra - ( valor_compra * 0.18 ))
elif ( valor_compra > 1_500_000 ):
    valor_pagar = (valor_compra - ( valor_compra * 0.25 ))

descuento = ""
elif (valor_compra < 50000):
    descuento = ("0")
elif (valor_compra > 50000 y valor_compra<= 100000):
    descuento = (valor_compra * 0.05)
elif (valor_compra > 100000 y valor_compra <= 700000):
    descuento = ( valor_compra * 0.11)
elif ( valor_compra > 700_000  y  valor_compra <=  1_500_000 ):
    descuento = ( valor_compra * 0.18 )
elif ( valor_compra > 1_500_000 ):
    descuento = ( valor_compra * 0.25 )

print ( f" { nombre_cliente } ")
print ( f"el valor de la compra es: {valor_compra}")
print ( f"valor total: {valor_pagar}")
print ( f"descuento final: {descuento}")

