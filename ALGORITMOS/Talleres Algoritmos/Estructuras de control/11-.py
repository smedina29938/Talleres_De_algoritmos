t = float ( input ( " Digite temperatura " ))

deportes =  ''
si ( t > 85  y  t <  120 ):
    deporte =  "Natación"
elif ( t > 70  y  t <=  85 ):
    deporte =  "tenis"
elif ( t > 32  y  t <=  70 ):
    deporte  =  "Golf"
elif ( t > 10  y  t <=  32 ):
    deporte  =  "Esqui"
elif ( t >= 0  y  t <=  10 ):
    deporte  =  "Marcha"
más :
    deporte =  "No hay ningún deporte a practicar"

print ( f"El deporte apropiado para practicar es : { deporte } " )