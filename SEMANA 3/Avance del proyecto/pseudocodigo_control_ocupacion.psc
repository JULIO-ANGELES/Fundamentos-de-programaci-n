Proceso ControlOcupacionGimnasioUniversitario
	
    Definir seleccion, capacidad_maxima, usuarios_presentes Como Entero
    Definir espacios_disponibles, cantidad_horarios, i Como Entero
    Definir porcentaje_ocupacion, suma_ocupacion, promedio_ocupacion Como Real
    Definir mayor_ocupacion, menor_ocupacion Como Real
	
    Definir horario Como Cadena
    Definir horario_mayor, horario_menor Como Cadena
    Definir nivel_ocupacion Como Cadena
	
    seleccion <- 0
    suma_ocupacion <- 0
    mayor_ocupacion <- 0
    menor_ocupacion <- 101
	
    Escribir "=========================================="
    Escribir " CONTROL DE OCUPACION DEL GIMNASIO"
    Escribir "          UNIVERSITARIO"
    Escribir "=========================================="
	
    Escribir "Ingrese la capacidad maxima del gimnasio:"
    Leer capacidad_maxima
	
    Mientras capacidad_maxima <= 0 Hacer
        Escribir "La capacidad debe ser mayor a cero."
        Escribir "Ingrese nuevamente la capacidad maxima:"
        Leer capacidad_maxima
    FinMientras
	
    Mientras seleccion <> 4 Hacer
		
        Escribir ""
        Escribir "------------- MENU PRINCIPAL -------------"
        Escribir "1. Registrar ocupacion de un horario"
        Escribir "2. Analizar varios horarios"
        Escribir "3. Consultar capacidad del gimnasio"
        Escribir "4. Salir"
        Escribir "Seleccione una opcion:"
        Leer seleccion
		
        Si seleccion = 1 Entonces
			
            Escribir ""
            Escribir "Ingrese el horario:"
            Leer horario
			
            Escribir "Ingrese la cantidad de usuarios presentes:"
            Leer usuarios_presentes
			
            Mientras usuarios_presentes < 0 O usuarios_presentes > capacidad_maxima Hacer
                Escribir "Cantidad de usuarios no valida."
                Escribir "Ingrese nuevamente la cantidad:"
                Leer usuarios_presentes
            FinMientras
			
            espacios_disponibles <- capacidad_maxima - usuarios_presentes
			
            porcentaje_ocupacion <- (usuarios_presentes / capacidad_maxima) * 100
			
            Si porcentaje_ocupacion <= 50 Entonces
                nivel_ocupacion <- "BAJA"
            Sino
                Si porcentaje_ocupacion <= 75 Entonces
                    nivel_ocupacion <- "MODERADA"
                Sino
                    Si porcentaje_ocupacion <= 90 Entonces
                        nivel_ocupacion <- "ALTA"
                    Sino
                        nivel_ocupacion <- "CRITICA"
                    FinSi
                FinSi
            FinSi
			
            Escribir ""
            Escribir "------------- RESULTADO -------------"
            Escribir "Horario: ", horario
            Escribir "Usuarios presentes: ", usuarios_presentes
            Escribir "Espacios disponibles: ", espacios_disponibles
            Escribir "Porcentaje de ocupacion: ", porcentaje_ocupacion, "%"
            Escribir "Nivel de ocupacion: ", nivel_ocupacion
			
            Si usuarios_presentes = capacidad_maxima Entonces
                Escribir "ALERTA: El gimnasio alcanzo su capacidad maxima."
            FinSi
			
        Sino
			
            Si seleccion = 2 Entonces
				
                Escribir ""
                Escribir "Ingrese la cantidad de horarios que desea analizar:"
                Leer cantidad_horarios
				
                Mientras cantidad_horarios <= 0 Hacer
                    Escribir "La cantidad debe ser mayor a cero."
                    Escribir "Ingrese nuevamente la cantidad de horarios:"
                    Leer cantidad_horarios
                FinMientras
				
                suma_ocupacion <- 0
                mayor_ocupacion <- 0
                menor_ocupacion <- 101
				
                Para i <- 1 Hasta cantidad_horarios Hacer
					
                    Escribir ""
                    Escribir "Registro numero ", i
					
                    Escribir "Ingrese el horario:"
                    Leer horario
					
                    Escribir "Ingrese la cantidad de usuarios presentes:"
                    Leer usuarios_presentes
					
                    Mientras usuarios_presentes < 0 O usuarios_presentes > capacidad_maxima Hacer
                        Escribir "Cantidad de usuarios no valida."
                        Escribir "Ingrese nuevamente la cantidad:"
                        Leer usuarios_presentes
                    FinMientras
					
                    espacios_disponibles <- capacidad_maxima - usuarios_presentes
					
                    porcentaje_ocupacion <- (usuarios_presentes / capacidad_maxima) * 100
					
                    suma_ocupacion <- suma_ocupacion + porcentaje_ocupacion
					
                    Si porcentaje_ocupacion <= 50 Entonces
                        nivel_ocupacion <- "BAJA"
                    Sino
                        Si porcentaje_ocupacion <= 75 Entonces
                            nivel_ocupacion <- "MODERADA"
                        Sino
                            Si porcentaje_ocupacion <= 90 Entonces
                                nivel_ocupacion <- "ALTA"
                            Sino
                                nivel_ocupacion <- "CRITICA"
                            FinSi
                        FinSi
                    FinSi
					
                    Si porcentaje_ocupacion > mayor_ocupacion Entonces
                        mayor_ocupacion <- porcentaje_ocupacion
                        horario_mayor <- horario
                    FinSi
					
                    Si porcentaje_ocupacion < menor_ocupacion Entonces
                        menor_ocupacion <- porcentaje_ocupacion
                        horario_menor <- horario
                    FinSi
					
                    Escribir ""
                    Escribir "Horario: ", horario
                    Escribir "Usuarios presentes: ", usuarios_presentes
                    Escribir "Espacios disponibles: ", espacios_disponibles
                    Escribir "Porcentaje de ocupacion: ", porcentaje_ocupacion, "%"
                    Escribir "Nivel de ocupacion: ", nivel_ocupacion
					
                FinPara
				
                promedio_ocupacion <- suma_ocupacion / cantidad_horarios
				
                Escribir ""
                Escribir "------------- RESUMEN DEL ANALISIS -------------"
                Escribir "Horarios analizados: ", cantidad_horarios
                Escribir "Promedio de ocupacion: ", promedio_ocupacion, "%"
                Escribir "Horario con mayor ocupacion: ", horario_mayor
                Escribir "Porcentaje mayor: ", mayor_ocupacion, "%"
                Escribir "Horario con menor ocupacion: ", horario_menor
                Escribir "Porcentaje menor: ", menor_ocupacion, "%"
				
            Sino
				
                Si seleccion = 3 Entonces
					
                    Escribir ""
                    Escribir "La capacidad maxima del gimnasio es de:"
                    Escribir capacidad_maxima, " usuarios."
					
                Sino
					
                    Si seleccion = 4 Entonces
						
                        Escribir ""
                        Escribir "Programa finalizado."
						
                    Sino
						
                        Escribir ""
                        Escribir "Opcion no valida."
                        Escribir "Seleccione una opcion del 1 al 4."
						
                    FinSi
					
                FinSi
				
            FinSi
			
        FinSi
		
    FinMientras
		
FinProceso

