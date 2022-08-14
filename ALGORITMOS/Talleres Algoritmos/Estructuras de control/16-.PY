
a = float ( input ( "valor para A en la fórmula cuadratica" ))
b = float ( input ( "valor para B en la fórmula cuadratica" ))
c = float ( input ( "valor para C en la fórmula cuadratica" ))  


de  cmath  importar  sqrt
x1 = ( - b - sqrt ( b ** 2 - 4 * a * c )) / ( 2 * a )
x2 = ( - b + sqrt ( b ** 2 - 4 * a * c )) / ( 2 * a )
discriminante = b ** 2 - 4 * a * c  
solución = ""
si ( discriminante == 0 ):
    solucion =  - b / ( 2 * a ) 
elif ( discriminante > 0 ):
    solución =  x1 , x2 
elif ( discriminante < 0 ):
    solucion =  "No tiene solucion en los reales"

print ( f" La solucion o soluciones de la ecuacion de segundo grado son { solucion } " )