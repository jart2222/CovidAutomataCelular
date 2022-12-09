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
        self.dias = 0
        self.dim=dim
        self.contadorLugares = 0;
        self.idIndividuos = 0;
        self.casas=casas;
        self.crearEspacios();
    def creacionAutomata(self, contadorLugares):
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
                    , random.randint(0, self.dim-1) # Coordenada Y
                    ,contadorLugares
                    )

        self.idIndividuos += 1
        return p;

    def crearEspacios(self):
        for i in range(self.casas):
            casa = Casa(self.dim, self.contadorLugares, "Casa")
            for i in range(random.randint(0, 10)):
                casa.addPersona(self.creacionAutomata(self.contadorLugares))

            self.contadorLugares += 1;
            self.espacioInstancia.append(casa)

        escuela=Escuela(self.dim, self.contadorLugares, "Escuela")
        self.contadorLugares += 1;
        trabajo=Trabajo(self.dim, self.contadorLugares, "Trabajo")
        self.contadorLugares += 1;
        trasporte=Trasporte(self.dim, self.contadorLugares, "Trasporte")
        self.contadorLugares += 1;

        self.espacioInstancia.append(escuela)
        self.espacioInstancia.append(trabajo)
        self.espacioInstancia.append(trasporte)

    def asignarEspacioPersona(self):
        """
         asigna un espacio segun el tipo de persona

        @param Persona persona :
        @return  :
        @author
        """
        casas=[]
        trasportes=[]
        trabajos=[]
        escuelas=[]
        for espacio in self.espacioInstancia:
            if(espacio.nombre=="Casa"):
                casas.append(espacio)
                continue
            if (espacio.nombre == "Trabajo"):
                trabajos.append(espacio)
                continue
            if (espacio.nombre == "Trasporte"):
                trasportes.append(espacio)
                continue
            if (espacio.nombre == "Escuela"):
                escuelas.append(espacio)
                continue

        listaPersona=[]
        for casa in casas:
            for persona in casa.listaAutomatasContenidos:
                listaPersona.append(persona)

        for casa in casas:
            print( f"La casa {casa.id} tiene {len(casa.listaAutomatasContenidos)}")
            for persona in listaPersona:
                if(persona in casa.listaAutomatasContenidos):
                    if (persona.edad >= 0 and persona.edad <= 1):
                        persona.setEspacioActual(escuelas[0].id)
                        escuelas[0].addPersona(persona)
                        casa.removePersona(persona)

                    if (persona.edad >= 2 and persona.edad <= 4):
                        persona.setEspacioActual(trabajos[0].id)
                        trabajos[0].addPersona(persona)
                        casa.removePersona(persona)

                    if (persona.edad > 4):
                        persona.setEspacioActual(trasportes[0].id)
                        trasportes[0].addPersona(persona)
                        casa.removePersona(persona)







        # for casa in casas:
        #     for persona in casa.listaAutomatasContenidos:
        #         if (persona in trabajos[0].listaAutomatasContenidos):
        #             casa.removePersona(persona)
        #             continue;
        #         if (persona in escuelas[0].listaAutomatasContenidos):
        #             casa.removePersona(persona)
        #             continue;
        #         if (persona in trasportes[0].listaAutomatasContenidos):
        #             casa.removePersona(persona)
        #             continue;
        # #

        #         persona.setEspacioActual(escuelas[0].id)
        #         escuelas[0].addPersona(persona)
        #
        #     if persona in lista2_4:
        #         casa.removePersona(persona)
        #         persona.setEspacioActual(trabajos[0].id)
        #         trabajos[0].addPersona(persona)
        #
        #     if persona in lista5_:
        #         casa.removePersona(persona)
        #         persona.setEspacioActual(trasportes[0].id)
        #         trasportes[0].addPersona(persona)
