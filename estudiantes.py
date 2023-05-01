class estudiante:
    def __init__(self, nombre, apellido, legajo, DNI, email, celular, materia):
        self.nombre = nombre
        self.apellido = apellido
        self.legajo = legajo
        self.DNI = DNI
        self.email = email
        self.celular = celular
        self.materias = [materia]

class profesor:
    def __init__(self, nombre, apellido, legajo, DNI, email, celular, materia):
        self.nombre = nombre
        self.apellido = apellido
        self.legajo = legajo
        self.DNI = DNI
        self.email = email
        self.celular = celular
        self.materias = [materia]
        
class materia:
    def __init__(self, nombre, codigo, duracion):
        self.nombre = nombre
        self.codigo = codigo
        self.duracion = duracion

if __name__ == '__main__':
    materia_matematica = materia("Matemáticas", "00010", "Semestral")
    print('Objeto ID: ' + str(id(materia_matematica)))
    print('Nombre: ' + materia_matematica.nombre)
    print('Código: ' + materia_matematica.codigo)
    print('Duración: ' + materia_matematica.duracion)
    print()

    alumno_tadeo = estudiante("Tadeo", "Drube", 62222, 44122610, "t.drube@um.edu.ar", 2616816942, materia_matematica)
    print('Objeto ID: ' + str(id(alumno_tadeo)))
    print('Nombre: ' + alumno_tadeo.nombre)
    print('Apellido: ' + alumno_tadeo.apellido)
    print('Legajo: ' + str(alumno_tadeo.legajo))
    print('DNI: ' + str(alumno_tadeo.DNI))
    print('E-mail: ' + alumno_tadeo.email)
    print('Número de celular: ' + str(alumno_tadeo.celular))
    print('Materias: ', end= "" )
    print(alumno_tadeo.materias)
    print()
    
    profesor_juan = profesor("Juan", "Perez", 1, 1, "juan.perez@um.edu.ar", 261123456789, materia_matematica)
    print('Objeto ID: ' + str(id(profesor_juan)))
    print('Nombre: ' + profesor_juan.nombre)
    print('Apellido: ' + profesor_juan.apellido)
    print('Legajo: ' + str(profesor_juan.legajo))
    print('DNI: ' + str(profesor_juan.DNI))
    print('E-mail: ' + profesor_juan.email)
    print('Número de celular: ' + str(profesor_juan.celular))
    print('Materias: ', end= "" )
    print(profesor_juan.materias) 
    

    