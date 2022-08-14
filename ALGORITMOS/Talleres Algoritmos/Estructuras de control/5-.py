venta_primer = int ( input ( "Inserte las Ventas que obtuvo el departamento No 1 en el mes : " ))
venta_segun = int ( input ( "Inserte las Ventas que obtuvo el departamento No 2 en el mes : " ))
venta_ter = int ( input ( "Inserte las Ventas que obtuvo el departamento No 3 en el mes: " ))
sueldo_empleados = int ( input ( " Inserte el salario que tienen los empleados " )) 

s  = (( venta_primer  +  venta_segun  +  venta_ter ) * 0.33 ) 

e = ( sueldo_empleados * 0.2 ) 
sf = ( e + sueldo_empleados ) 

si (venta_primer  >  s :)
    
    print ( f" Comision que recibiran cada uno de los empleados del departamento No 1 en el mes es de : { e } , por lo tanto su sueldo final es de { sf } " )
más :

    print ( f" Los empleadosl departamento 1 no recibiran comision , recibiran su salario normal : { sueldo_empleados } " )
si ( venta_segun  >  s ):

    print ( f" La Comision que recibiran cada uno de los empleados del departamento No 2 en el mes es de : { e } , por lo tanto su sueldo final es de { sf } " )
más :

    print ( f"Los empleados del departamento 2 no recibiran comision , recibiran su salario normal : { sueldo_empleados } " )
si ( venta_ter  >  s ):

    print ( f" La Comision que recibiran cada uno de los empleados del departamento No 3 en el mes es de { e } , por lo tanto su sueldo final es de : { sf } " )
más :
    print ( f"Los empleados del departamento 3 no recibiran comision , recibiran su salario normal : { sueldo_empleados } " )
