fecha_nacimiento = input ( "Digite en este formato 'dd/mm,yy: " )
dia , mes , año  =  fecha_nacimiento . dividir ( "/" )
dia_nacimiento = int ( día )
mes_nacimiento = int ( mes )
a ñ o_nacimiento  = int ( año )


importar  fecha y hora
x  = fecha y  hora . fecha y hora ahora () 
mes_actual  =  int ( x . strftime ( "%m" ))
a ñ o_actual  =  int ( x . strftime ( "%Y" ))
dia_actual  =  int ( x . strftime ( "%d" ))
edad = ( añ o_actual - añ o_nacimiento ) _ _



signo = ""
si (( mes_nacimiento == 11 ) y ( dia_nacimiento >= 22 )) o (( mes_nacimiento == 12 ) y ( dia_nacimiento <= 21 )):
    signo = ( "Su signo zodiacal es Sagitario " )
si (( mes_nacimiento == 12 ) y ( dia_nacimiento >= 22 )) o (( mes_nacimiento == 1 ) y ( dia_nacimiento <= 20 )):
    signo = ( "Su signo zodiacal es Capricornio" )
si (( mes_nacimiento == 1 ) y ( dia_nacimiento >= 21 )) o (( mes_nacimiento == 2 ) y ( dia_nacimiento <= 19 )):
    signo = ( "Su signo zodiacal es Acuario " )
si (( mes_nacimiento == 2 ) y ( dia_nacimiento >= 20 )) o (( mes_nacimiento == 3 ) y ( dia_nacimiento <= 19 )):
    signo = ( "Su signo zodiacal es Piscis " )
si (( mes_nacimiento == 3 ) y ( dia_nacimiento >= 21 )) o (( mes_nacimiento == 4 ) y ( dia_nacimiento <= 20 )):
    signo = ( "Su signo zodiacal es Aries " )
si (( mes_nacimiento == 4 ) y ( dia_nacimiento >= 21 )) o (( mes_nacimiento == 5 ) y ( dia_nacimiento <= 21 )):
    signo = ( "Su signo zodiacal es Tauro" )
si (( mes_nacimiento == 5 ) y ( dia_nacimiento >= 22 )) o (( mes_nacimiento == 6 ) y ( dia_nacimiento <= 21 )):
    signo = ( "Su signo zodiacal es Géminis " )
si (( mes_nacimiento == 6 ) y ( dia_nacimiento >= 22 )) o (( mes_nacimiento == 7 ) y ( dia_nacimiento <= 22 )):
    signo = ( "Su signo zodiacal es Cáncer" )
si (( mes_nacimiento == 7 ) y ( dia_nacimiento >= 23 )) o (( mes_nacimiento == 8 ) y ( dia_nacimiento <= 23 )):
    signo = ( "Su signo zodiacal es Leo" )
si (( mes_nacimiento == 8 ) y ( dia_nacimiento >= 24 )) o (( mes_nacimiento == 9 ) y ( dia_nacimiento <= 22 )):
    signo = ( "Su signo zodiacal es Virgo" )
si (( mes_nacimiento == 9 ) y ( dia_nacimiento >= 23 )) o (( mes_nacimiento == 10 ) y ( dia_nacimiento <= 22 )):
    signo = ( "Su signo zodiacal es Libra" )
si (( mes_nacimiento == 10 ) y ( dia_nacimiento >= 23 )) o (( mes_nacimiento == 11 ) y ( dia_nacimiento <= 21 )):
    signo = ( "Su signo zodiacal es Escorpión" )


print ( f" Su signo del Zodiaco es { signo } " )
print ( f" Su edad es de : { edad } años " )