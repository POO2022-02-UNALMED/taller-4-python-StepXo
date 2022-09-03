from classroom.asignatura import Asignatura
from classroom.grupo import Grupo

if __name__ == "__main__":
    asignatura1 = Asignatura("Matematicas")
    asignatura2 = Asignatura("Castellano", "Salon 201")
    grupo1 = Grupo()

    print(asignatura1) #arroja solo el espacio de memoria falta un __str__ pa imprimir algo con solo llamarlo
    print(grupo1)      #arroja solo el espacio de memoria falta un __str__ pa imprimir algo con solo llamarlo
    print(grupo1.grado) #debe imprimir "Grado 12"

    grupo2 = Grupo("Grupo 5", [], ["Alejandro", "Carlos"])

    grupo3 = Grupo()
    grupo4 = Grupo()
    grupo5 = Grupo()
    grupo3.agregarAlumno("Kelly") #hay problemas de definicion de variables, las init se deben cambiar de None tipe a [] para poder usar append y +=[]
    grupo4.agregarAlumno("Santiago", ["Jaime", "Pedro"]) # por la misma razon de arriba no podemos agrafar nada a un None tipe, hay que cambiar por is not None
    grupo5.agregarAlumno("Javier")

    print(grupo3.listadoAlumnos)
    print(grupo4.listadoAlumnos)
    print(grupo5.listadoAlumnos)

    grupo3.listadoAsignaturas(as1="Ciencias", as2="Quimica", as3="Ingles") #no sirve de nada instarnciar kwargs sin el **
    print(len(grupo3._asignaturas))

    Grupo.asignarNombre("Grado 1")
    print(Grupo.grado)
    Grupo.asignarNombre()
    print(Grupo.grado) #en python no existe la sobre carga de metodos
