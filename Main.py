import sys
from Binary_Search_Tree import *
from Alumno import *
from Funciones_generadores import *

def menu():
    print("\nMenu:")
    print("1. Crear un árbol y generar 100 alumnos")
    print("2. Insertar un alumno nuevo")
    print("3. Buscar un alumno por número de cuenta")
    print("4. Imprimir el árbol")
    print("5. Salir")

def generar_alumnos(bst):
    for i in range(100):
        alumno = Alumno()
        print("Alumno", i + 1, ":", alumno)
        bst.insertar(alumno)

def generar_alumno():
    alumno = Alumno()
    print("Alumno", ":", alumno)
    return alumno

def crear_arbol():
    arbol_bst = BST()
    generar_alumnos(arbol_bst)
    print("\nEstructura del árbol (por niveles):")
    imprimir_por_niveles(arbol_bst.raiz)
    return arbol_bst

def insertar_alumno_manual(arbol_bst):
    print("\nElige el método de inserción:")
    print("1. Insertar un alumno manualmente")
    print("2. Insertar un alumno generado automáticamente")
    opcion = input("Selecciona una opción (1 o 2): ")
    match opcion:
        case '1':
            no_cta = input("\nIntroduce el número de cuenta: ")
            nombre = input("Introduce el nombre: ")
            apellido_paterno = input("Introduce el apellido paterno: ")
            apellido_materno = input("Introduce el apellido materno: ")
            edad = int(input("Introduce la edad: "))
            correo = input("Introduce el correo: ")
            semestre = int(input("Introduce el semestre: "))
            materias = input("Introduce las materias (separadas por comas): ").split(",")
            promedio = float(input("Introduce el promedio: "))
            nuevo_alumno = Alumno()
            nuevo_alumno.no_cta = no_cta
            nuevo_alumno.nombre = nombre
            nuevo_alumno.apellido_paterno = apellido_paterno
            nuevo_alumno.apellido_materno = apellido_materno
            nuevo_alumno.edad = edad
            nuevo_alumno.correo = correo
            nuevo_alumno.semestre = semestre
            nuevo_alumno.materias = materias
            nuevo_alumno.promedio = promedio
        case '2':
            nuevo_alumno = generar_alumno()
        case _:
            print("\nOpción no válida. Volviendo al menú principal.")
            return
    arbol_bst.insertar(nuevo_alumno)
    print("\nAlumno insertado correctamente.")

def buscar_alumno(arbol_bst):
    no_cta_a_buscar = input("\nIntroduce el número de cuenta del alumno a buscar: ")
    arbol_bst.buscar(no_cta_a_buscar)

def imprimir_arbol(arbol_bst):
    if arbol_bst is not None:
        print("\nEstructura del árbol (por niveles):")
        imprimir_por_niveles(arbol_bst.raiz)
    else:
        print("\nNo hay ningún árbol creado.")

if __name__ == "__main__":
    arbol_bst = None
    while True:
        menu()
        opcion = input("\nSelecciona una opción: ")
        match opcion:
            case '1':
                arbol_bst = crear_arbol()
            case '2':
                if arbol_bst is None:
                    print("\nPrimero debes crear un árbol.")
                else:
                    insertar_alumno_manual(arbol_bst)
            case '3':
                if arbol_bst is None:
                    print("\nPrimero debes crear un árbol.")
                else:
                    buscar_alumno(arbol_bst)
            case '4':
                imprimir_arbol(arbol_bst)
            case '5':
                print("\nSaliendo del programa...")
                sys.exit()
            case _:
                print("\nOpción no válida. Por favor, selecciona de nuevo.")