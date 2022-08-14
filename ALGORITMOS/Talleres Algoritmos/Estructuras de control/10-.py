cat = int ( input ( "Digite su categoria" ))
sueldo_bruto = int ( input ( "Dígito de su salario bruto" ))

aumento =  ''
si ( cat == 1  y  sueldo_bruto ==  5_000_000 ):
    aumento = ( sueldo_bruto * 0.10 )
elif ( gato == 2  y  sueldo_bruto == 4_300_000 ):
    aumento = ( sueldo_bruto * 0.15 )
elif ( gato == 3  y  sueldo_bruto ==  3_600_000 ):
    aumento = ( sueldo_bruto * 0.20 )
elif ( gato == 4  y  sueldo_bruto ==  2_000_000 ):
    aumento  = ( sueldo_bruto * 0.40 )
elif ( cat == 5  y  sueldo_bruto ==  900_000 ):
    aumento  = ( sueldo_bruto * 0.60 )
más :
    aumento =  "No hay ningun aumento a aplicar "

nuevo_sueldo = ''
si ( cat == 1  y  sueldo_bruto ==  5_000_000 ):
    nuevo_sueldo = (( sueldo_bruto * 0.10 ) + sueldo_bruto )
elif ( gato == 2  y  sueldo_bruto == 4_300_000 ):
    nuevo_sueldo = (( sueldo_bruto * 0.15 ) + sueldo_bruto )
elif ( gato == 3  y  sueldo_bruto ==  3_600_000 ):
    nuevo_sueldo = (( sueldo_bruto * 0.20 ) + sueldo_bruto )
elif ( gato == 4  y  sueldo_bruto ==  2_000_000 ):
    nuevo_sueldo  = (( sueldo_bruto * 0.40 ) + sueldo_bruto )
elif ( cat == 5  y  sueldo_bruto ==  900_000 ):
    nuevo_sueldo  = (( sueldo_bruto * 0.60 ) + sueldo_bruto )
más :
    nuevo_sueldo = ( f" El sueldo se mantiene igual { sueldo_bruto } " )

print ( f"La categoria del trabajador es { cat } , el aumento que tendra sera de { aumento } y su nuevo sueldo bruto sera de { nuevo_sueldo } " )

