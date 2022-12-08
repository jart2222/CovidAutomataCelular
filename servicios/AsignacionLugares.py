import random
from EspaciosTrabajo.Espacio import Espacio
from EspaciosTrabajo.Casa import Casa
from EspaciosTrabajo.Escuela import Escuela
from EspaciosTrabajo.Trabajo import Trabajo
from EspaciosTrabajo.Trasporte import Trasporte
from modelo.Persona import Persona;
class AsignacionLugares:
    def __init__(self,casas,dim):
        self.espacioInstancia = []
        self.listaPersonas = []
        self.dias = 0
        self.dim=dim
        self.contadorLugares = 0;
        self.idIndividuos = 0;
        self.casas=casas;
        self.crearEspacios();
    def creacionAutomata(self):
        """
         crea un automata y lo agrega a la lista de automatas

        @return  :
        @author
        """
        p = Persona(self.idIndividuos  # idPersona
                    , random.randint(0, 8)  # Edad
                    , random.choice(['M', 'H'])  # Sexo: ->Mujer o Hombre
                    , random.randint(0, 3)  # Enfermedades Cronicas
                    , False  # Contagiado
                    , random.choice([True, False])  # Vacunado
                    , random.randint(0, self.dim-1)  # Coordenada X
                    , random.randint(0, self.dim-1))  # Coordenada Y

        self.idIndividuos += 1
        return p;

    def crearEspacios(self):
        for i in range(self.casas):
            casa = Casa(self.dim, self.contadorLugares, "Casa")
            self.contadorLugares += 1;
            for i in range(random.randint(0, 10)):
                casa.addPersona(self.creacionAutomata())
            self.espacioInstancia.append(casa)

        escuela=Escuela(self.dim, self.contadorLugares, "Escuela")
        self.contadorLugares += 1;
        trabajo=Escuela(self.dim, self.contadorLugares, "Trabajo")
        self.contadorLugares += 1;
        trasporte=Trasporte(self.dim, self.contadorLugares, "Trasporte")
        self.contadorLugares += 1;

        self.espacioInstancia.append(escuela)
        self.espacioInstancia.append(trabajo)
        self.espacioInstancia.append(trasporte)

    def asignarEspacioPersona(self, persona):
        """
         asigna un espacio segun el tipo de persona

        @param Persona persona :
        @return  :
        @author
        """


        pass






