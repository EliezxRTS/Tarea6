from Funciones_generadores import *

class Alumno:
    def __init__(self):
        self.no_cta = funcion_no_cta()
        self.edad = funcion_edad(self.no_cta)
        self.nombre, self.apellido_paterno, self.apellido_materno = funcion_nombre()
        self.correo = funcion_correo(self.nombre, self.apellido_paterno, self.apellido_materno)
        self.semestre = funcion_semestre(self.no_cta)
        self.materias = funcion_materias(self.semestre)
        self.promedio = funcion_promedio()

    def __str__(self):
        return (f"No. CTA: {self.no_cta}, Nombre: {self.nombre} {self.apellido_paterno} {self.apellido_materno}, "
                f"Correo: {self.correo}, Edad: {self.edad}, Semestre: {self.semestre}, Materias: {', '.join(self.materias)}, Promedio: {self.promedio}")