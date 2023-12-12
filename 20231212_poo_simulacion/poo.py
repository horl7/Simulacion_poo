from datetime import datetime

class Curso:
    def __init__(self, id_curso, nombre, creditos, anos_de_estudio):
        self.id_curso = id_curso
        self.nombre = nombre
        self.creditos = creditos
        self.anos_de_estudio = anos_de_estudio

    def mostrar_ficha_curso(self):
        print(f"Ficha del Curso: {self.nombre}")
        print(f"ID: {self.id_curso}")
        print(f"Créditos: {self.creditos}")
        print(f"Años de Estudio: {self.anos_de_estudio}")
        print("\n")

class Alumno:
    def __init__(self, id_alumno, nombre, email):
        self.id_alumno = id_alumno
        self.nombre = nombre
        self.email = email
        self.cursos_matriculados = []

    def mostrar_ficha_alumno(self):
        print(f"Ficha del Alumno: {self.nombre}")
        print(f"ID: {self.id_alumno}")
        print(f"Email: {self.email}")
        print(f"Cursos Matriculados: {', '.join(curso.nombre for curso in self.cursos_matriculados)}")
        print("\n")

class Matricula:
    def __init__(self, id_matricula, fecha_matricula, id_alumno, id_curso):
        self.id_matricula = id_matricula
        self.fecha_matricula = fecha_matricula
        self.id_alumno = id_alumno
        self.id_curso = id_curso

    def mostrar_datos_matricula(self):
        print(f"Datos de la Matrícula (ID: {self.id_matricula}):")
        print(f"Fecha de Matrícula: {self.fecha_matricula}")
        print(f"ID del Alumno: {self.id_alumno}")
        print(f"ID del Curso: {self.id_curso}")
        print("\n")

class CentroMatriculas:
    matriculas_realizadas = []

    @classmethod
    def realizar_matricula(cls, alumno, curso):
        try:
            if curso not in alumno.cursos_matriculados:
                id_matricula = len(cls.matriculas_realizadas) + 1
                fecha_matricula = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                matricula = Matricula(id_matricula, fecha_matricula, alumno.id_alumno, curso.id_curso)
                cls.matriculas_realizadas.append(matricula)
                alumno.cursos_matriculados.append(curso)
                print(f"El alumno {alumno.nombre} se ha matriculado en el curso {curso.nombre}")
            else:
                raise ValueError(f"El alumno {alumno.nombre} ya está matriculado en el curso {curso.nombre}")
        except Exception as e:
            print(f"Error al realizar la matrícula: {e}")

    @classmethod
    def mostrar_matriculas_centro(cls):
        try:
            if not cls.matriculas_realizadas:
                raise ValueError("No hay matrículas realizadas en el centro.")
            else:
                print("Matrículas realizadas en el centro:")
                for matricula in cls.matriculas_realizadas:
                    matricula.mostrar_datos_matricula()
        except Exception as e:
            print(f"Error al mostrar las matrículas del centro: {e}")


curso1 = Curso(1, "Matemáticas", 5, 2)
curso2 = Curso(2, "Historia", 4, 3)

alumno1 = Alumno(1, "Juan", "juan@email.com")
alumno2 = Alumno(2, "Ana", "ana@email.com")

curso1.mostrar_ficha_curso()
curso2.mostrar_ficha_curso()

alumno1.mostrar_ficha_alumno()
alumno2.mostrar_ficha_alumno()

CentroMatriculas.realizar_matricula(alumno1, curso1)
CentroMatriculas.realizar_matricula(alumno2, curso1)
CentroMatriculas.realizar_matricula(alumno2, curso2)

CentroMatriculas.mostrar_matriculas_centro()
