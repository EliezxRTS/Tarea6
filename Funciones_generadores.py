import pandas as pd
import numpy as np
import random

#Función para definir un número de cuenta
def funcion_no_cta():
    claves = [314, 315, 316, 317, 318, 319, 320, 321, 322, #Bachillerato
        417, 418, 419, 420, 421, 422, 423, 424, 425] #Examen
    clave = random.choice(claves)
    registro = random.randint(111111,999999) #Añade el total de números faltantes
    no_cta = f"{clave}{registro}"
    return no_cta

#Función para definir la edad, 18+ años al momento de ingreso a licenciatura
def funcion_edad(no_cta):
    clave = int(no_cta[:3]) #Slicing para obtener ano_ingreso
    edades_posibles = [18] * 60 + [19] * 20 + [20] * 10 + [21] * 5 #Alumno de 18+ años
    edad_ingreso = random.choice(edades_posibles) #Se define una edad de ingreso aleatoria
    ano_actual = 25 #Nuevo ingreso en 2025-I
    if clave < 400:
        ano_ingreso = (clave % 100) + 3 #Edad de Bach 15+, entonces 15+3=18
    else:
        ano_ingreso = (clave % 100)
    tiempo_estudios = ano_actual - ano_ingreso #Tiempo desde el ingreso
    edad_actual = edad_ingreso + tiempo_estudios
    return edad_actual

#Función para definir un semestre dado el año de ingreso
def funcion_semestre(no_cta):
    clave = int(no_cta[:3])
    ano_actual = 25
    if clave < 400:
        ano_ingreso = (clave % 100) + 3
    else:
        ano_ingreso = (clave % 100)
    tiempo_estudios = ano_actual - ano_ingreso #Tiempo desde el ingreso
    #Se elige un semestre de una lista, lo que genera alumnos irregulares y regulares
    if tiempo_estudios == 0:
        semestre = random.choice([1, 2])
    elif tiempo_estudios == 1:
        semestre = random.choice([1, 2])
    elif tiempo_estudios == 2:
        semestre = random.choice([1, 2, 3, 4])
    elif tiempo_estudios == 3:
        semestre = random.choice([3, 4, 5, 6])
    elif tiempo_estudios == 4:
        semestre = random.choice([5, 6, 7, 8])
    elif tiempo_estudios >=5:
        semestre = random.choice([5, 6, 7, 8, 9])
    return semestre

#Función para definir un nombre desde una base de datos
def funcion_nombre():
    df = pd.read_excel('Nombres.xlsx')
    genero = random.choice(['Hombre', 'Mujer']) #Selecciona de entre 2 campos un nombre
    nombres_seleccionados = df[genero] #Obtiene la lista de ese campo
    nombre = random.choice(nombres_seleccionados) #Escoge uno de forma aleatoria
    apellidos = df['Apellido'].tolist() #Obtiene la lista del campo Apellido
    frecuencias = df['Frecuencia'].tolist() #Obtiene la lista del campo Frecuencia, esta se tomó de una base de datos de natalidad del INEGI
    apellido_paterno = np.random.choice(apellidos, p=np.array(frecuencias) / sum(frecuencias)) #Convierte la frecuencia a un valor entre 0 y 1
    apellido_materno = np.random.choice(apellidos, p=np.array(frecuencias) / sum(frecuencias))
    """frecuencia_paterno = frecuencias[apellidos.index(apellido_paterno)]
    frecuencia_materno = frecuencias[apellidos.index(apellido_materno)]
    print(f"Frecuencia del apellido paterno '{apellido_paterno}': {frecuencia_paterno}")
    print(f"Frecuencia del apellido materno '{apellido_materno}': {frecuencia_materno}")"""
    #El bloque comentado es para verificar que selecciona el apellido correcto dada la probabilidad p
    return nombre, apellido_paterno, apellido_materno

#Función para definir un correo desde el nombre
def funcion_correo(nombre, apellido_paterno, apellido_materno):
    apellido_correo = random.choice([apellido_paterno,apellido_materno]) #Selecciona un apellido para el correo
    correo = f"{nombre[:-1].lower()}.{apellido_correo[:-1].lower()}{random.randint(1, 99):02d}@fesaragon.unam.mx.com" #Esto es para no generar un correo real por accidente
    return correo

#Función para definir las materias que cursa el alumno dado su semestre
def funcion_materias(semestre):
    materias_por_semestre = { #Lista predefinida de materias
        1: ["GEOMETRIA ANALITICA","CALCULO DIFERENCIAL E INTEGRAL","ALGEBRA","COMPUTADORAS Y PROGRAMACION","INTRODUCCION A LA INGENIERIA EN COMPUTACION"],
        2: ["ALGEBRA LINEAL","CALCULO VECTORIAL","PROGRAMACION ORIENTADA A OBJETOS","COMUNICACION","EMPRENDIMIENTO 1"],
        3: ["ELECTRICIDAD Y MAGNETISMO","ESTRUCTURA DE DATOS","METODOS NUMERICOS","ECUACIONES DIFERENCIALES","EMPRENDIMIENTO 2"],
        4: ["PROBABILIDAD Y ESTADISTICA","BASES DE DATOS 1","EMPRENDIMIENTO 3","MATEMATICAS DISCRETAS","DISPOSITIVOS ELECTRONICOS"],
        5: ["LENGUAJES FORMALES-AUTOMATAS","DISEÑO Y ANALISIS DE ALGORITMOS","ADMINISTRACION DE PROYECTOS","PROGRAMACION WEB 1","DISEÑO LOGICO"], 
        6: ["COMPILADORES","SISTEMAS OPERATIVOS","DISEÑO DE SISTEMAS DIGITALES","INGENIERIA DE SOFTWARE","INTERNET DE LAS COSAS"],
        7: ["SISTEMAS DE INFORMACION","PROGRAMACION WEB 2","REDES DE COMPUTADORAS 1","MICROPROCESADORES Y MICROCONTROLADORES","PROGRAMACION DE VIDEOJUEGOS 1"],
        8: ["BASES DE DATOS 2","PROGRAMACION MOVIL 1","REDES DE COMPUTADORAS 2","PROGRAMACION DE VIDEOJUEGOS 2","GRAFICACION POR COMPUTADORA"],
        9: ["INTELIGENCIA ARTIFICIAL","SEGURIDAD INFORMATICA","MINERIA DE DATOS","PROGRAMACION MOVIL 2","ANALISIS DE MACRODATOS"]
    }
    return materias_por_semestre.get(semestre)

#Función para definir el promedio general
def funcion_promedio():
    return round(random.uniform(5.0, 10.0), 2)