import numpy as np;
import random

from EspaciosTrabajo.Espacio import Espacio
from EspaciosTrabajo.Casa import Casa
from EspaciosTrabajo.Escuela import Escuela
from EspaciosTrabajo.Trabajo import Trabajo
from EspaciosTrabajo.Trasporte import Trasporte
from modelo.Persona import Persona;


casa=Casa(10,1)

for i in range(4):
    p = Persona(i  #idPersona
                    ,random.randint(0, 8)        #Edad
                    ,random.choice(['M', 'H'])   #Sexo: ->Mujer o Hombre
                    ,random.randint(0, 3)        #Enfermedades Cronicas
                    , False                      #Contagiado
                    , random.choice([True, False])#Vacunado
                    , random.randint(0, 9)      #Coordenada X
                    , random.randint(0, 9))     #Coordenada Y
    casa.addPersona(p)

print(casa)



print(casa.a)

