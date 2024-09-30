from collections import deque

class Nodo: #Los Nodos reciben objetos Alumno
    def __init__(self, alumno):
        self.alumno = alumno
        self.izquierdo = None
        self.derecho = None

class BST:
    def __init__(self):
        self.raiz = None

    #La Función insertar agrega los nodos usando el no_cta como llave
    #pero almacenan todo el objeto alumno para su consulta
    def insertar(self, alumno):
        if self.raiz is None:
            self.raiz = Nodo(alumno)
        else:
            nodo_actual = self.raiz
            while True:
                if alumno.no_cta < nodo_actual.alumno.no_cta:
                    if nodo_actual.izquierdo is None:
                        nodo_actual.izquierdo = Nodo(alumno)
                        break
                    nodo_actual = nodo_actual.izquierdo
                elif alumno.no_cta > nodo_actual.alumno.no_cta:
                    if nodo_actual.derecho is None:
                        nodo_actual.derecho = Nodo(alumno)
                        break
                    nodo_actual = nodo_actual.derecho
                else:
                    print("\nAlumno inválido!!!")
                    print(f"El número de cuenta {alumno.no_cta} ya está en el árbol.")
                    break

    #La Función buscar usa el atributo no_cta del Alumno
    def buscar(self, alumno):
        nodo_actual = self.raiz
        while nodo_actual is not None:
            if alumno == nodo_actual.alumno.no_cta:
                print("Alumno encontrado:", nodo_actual.alumno)
                return nodo_actual.alumno
            elif alumno < nodo_actual.alumno.no_cta:
                nodo_actual = nodo_actual.izquierdo
            else:
                nodo_actual = nodo_actual.derecho
        print("Alumno no encontrado.")
        return None

#Función para imprimir en terminal una vista gráfica de referencia del árbol
def imprimir_por_niveles(raiz):
    if not raiz:
        print("El árbol está vacío.")
        return 0
    cola = deque([raiz])
    #Dado que el árbol no inserta no_cta que ya estén agregados se implementa
    #un contador que ayuda a verificar si hubo duplicados en la ejecución
    total_nodos = 0
    while cola:
        nivel_size = len(cola)
        nivel_nodos = []
        for _ in range(nivel_size):
            nodo_actual = cola.popleft()
            nivel_nodos.append(nodo_actual.alumno.no_cta)
            total_nodos += 1
            if nodo_actual.izquierdo:
                cola.append(nodo_actual.izquierdo)
            if nodo_actual.derecho:
                cola.append(nodo_actual.derecho)
        print("Nivel:", nivel_nodos)
    print(f"Número total de nodos en el árbol: {total_nodos}")
    return total_nodos