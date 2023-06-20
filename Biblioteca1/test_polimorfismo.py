from Biblioteca.docente import Docente
from Biblioteca.estudiante import Estudiante
from Biblioteca.libro import Libro
from Biblioteca.revista import Revista

# lista de personas que pueden ser estudiantes o docentes
e1 = Estudiante(nombre='Gabriela', apellido='Narváez', nivel=3)
d1 = Docente(nombre='Mario', apellido='Andrade', titulo_3er_nivel='contador')
e2 = Estudiante(nombre='Andrea', apellido='Narvaez', nivel=5)
d2 = Docente(nombre='Daniel', apellido='Martinez', titulo_3er_nivel='ingeniero')

personas = list()
personas.append(e1)
personas.append(d1)
personas.append(e2)
personas.append(d2)
print(personas)

for persona in personas:
    print(persona)

l5 = Libro(titulo='Huasipungo', autor='Jorge Icaza', disponible=True)
r5 = Revista(titulo='Revistas Emergencias', autor='Julian Casanova', disponible=False)
l6 = Libro(titulo='La iliada', autor='Homero', disponible=False)
r6 = Revista(titulo='Nutricion Hospitalaria', autor='Julian Casanova', disponible=True)

materiales =list()
materiales.append(l5)
materiales.append(r5)
materiales.append(l6)
materiales.append(r6)
print(materiales)

for material in materiales:
    print(material)

for persona in personas:
    tipo = type(persona)
    persona.pedir(lista_material=tipo, materia='revista')
