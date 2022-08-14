edad_paciente = int ( input ( "Inserte la edad del paciente en su equivalente de años a meses " ))
sexo_paciente = str ( input ( " Inserte su sexo de la siguiente manera , femenino (F) o masculino (M) " ))
nivel_hemoglobina = float ( input ( "Inserte cual fue el resultado del nivel de hemoglobina en la sangre " ))
sexo =  sexo_paciente [ 0 ] 

resultado = ''
si ( nivel_hemoglobina >= 13  y  nivel_hemoglobina <= 26 ) y ( edad_paciente >= 0  y  edad_paciente <= 1 ):
    resultado = ( "El resultado es Negativo" )
elif ( nivel_hemoglobina >= 10  y  nivel_hemoglobina <= 18 ) y ( edad_paciente > 1  y  edad_paciente <= 6 ):
    resultado = ( "El resultado es Negativo" )
elif ( nivel_hemoglobina >= 11  y  nivel_hemoglobina <= 15 ) y ( edad_paciente > 6  y  edad_paciente <= 12 ):
    resultado = ( "El resultado es Negativo" )
elif ( nivel_hemoglobina >= 11.5  and  nivel_hemoglobina <= 15 ) and ( edad_paciente > 12  and  edad_paciente <= 60 ): 
    resultado = ( "El resultado es Negativo" )
elif ( nivel_hemoglobina >= 12.6  and  nivel_hemoglobina <= 15.5 ) and ( edad_paciente > 60  and  edad_paciente <= 120 ): 
    resultado = ( "El resultado es Negativo" )
elif ( nivel_hemoglobina >= 13  and  nivel_hemoglobina <= 15.5 ) and ( edad_paciente > 120  and  edad_paciente <= 180 ): 
    resultado = ( "El resultado es Negativo" )  
elif ( nivel_hemoglobina >= 12  and  nivel_hemoglobina <= 16 ) and ( edad_paciente > 180  and  sexo == "F" ): 
    resultado = ( "El resultado es Negativo" )       
elif ( nivel_hemoglobina >= 14  and  nivel_hemoglobina <= 18 ) and ( edad_paciente > 180  and  sexo == "M" ): 
    resultado = ( "El resultado es Negativo" )
más :
    resultado =  "El resultado es positivo"



imprimir ( resultado )

    