import random
from EspaciosTrabajo.Espacio import Espacio
from EspaciosTrabajo.Casa import Casa
from EspaciosTrabajo.Escuela import Escuela
from EspaciosTrabajo.Trabajo import Trabajo
from EspaciosTrabajo.Trasporte import Trasporte
from modelo.Persona import Persona;
class AsignacionLugares:
    def __init__(self,casas,dim):
        self.dim=dim
        self.casasContador=casas;
        self.espacioInstancia = []
        self.dias = 0
        self.contadorLugares=0;
        self.lugaresTrasporte=random.randint(1,casas);
        self.lugaresEscuelas=random.randint(1,casas);
        self.lugaresTrabajos=random.randint(1,casas);
        self.idIndividuos=0;
        self.casas = []
        self.trasportes = []
        self.trabajos = []
        self.escuelas = []
        self.personas=[]
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
        for i in range(self.casasContador):
            casa = Casa(self.dim, self.contadorLugares, "Casa")

            for i in range(random.randint(0, 10)):
                casa.addPersona(self.creacionAutomata(self.contadorLugares))

            self.espacioInstancia.append(casa)
            self.contadorLugares += 1;

        for _ in range(self.lugaresTrasporte):
            trasporte=Trasporte(self.dim, self.contadorLugares, "Trasporte")
            self.contadorLugares += 1;
            self.espacioInstancia.append(trasporte)

        for _ in range(self.lugaresEscuelas):
            escuela=Escuela(self.dim, self.contadorLugares, "Escuela")
            self.contadorLugares += 1;
            self.espacioInstancia.append(escuela)

        for _ in range(self.lugaresTrabajos):
            trabajo=Trabajo(self.dim, self.contadorLugares, "Trabajo")
            self.contadorLugares += 1;
            self.espacioInstancia.append(trabajo)






    def asignarEspacioPersona(self):
        """
         asigna un espacio segun el tipo de persona

        @param Persona persona :
        @return  :
        @author
        """
        self.filtrarEspacios()

        for casa in self.casas:
            print(f"La casa {casa.id} tiene {len(casa.listaAutomatasContenidos)}")
            for persona in self.personas:
                if (persona in casa.listaAutomatasContenidos):
                    if (persona.edad >= 0 and persona.edad <= 1):
                        persona.setTrabajo(self.escuelas[random.randint(0,self.lugaresEscuelas-1)].id)
                        persona.setTrasposte(self.trasportes[random.randint(0, self.lugaresTrasporte - 1)].id)
                    if (persona.edad >= 2 and persona.edad < 6):
                        persona.setTrabajo(self.trabajos[random.randint(0,self.lugaresTrabajos-1)].id)
                        persona.setTrasposte(self.trasportes[random.randint(0, self.lugaresTrasporte - 1)].id)
                    if (persona.edad >= 6):
                        continue

    def moverPersona(self):
        for persona in self.personas:
            idEspacioActual=persona.espacioActual
            edad=persona.edad
            if((idEspacioActual<self.casasContador) and (edad<6)):#persona esta en su casa y por su edad tiene que tomar el trasporte
                persona.setEspacioActual(persona.trasposte)
                self.trasportes[persona.trasposte - (self.casasContador)].addPersona(persona)
                self.casas[persona.casa].removePersona(persona)
                continue

            if((idEspacioActual>=self.casasContador)): # persona se encuentra en el trasporte y tiene que cambiar a su trabajo
                if(edad>=0 and edad<2):
                    persona.setEspacioActual(persona.trabajo)
                    self.escuelas[persona.trabajo-(self.casasContador+self.lugaresTrasporte)].addPersona(persona)
                    self.trasportes[persona.trasposte-self.casasContador].removePersona(persona)
                    continue
                if (edad>=2 and edad<=6):
                    persona.setEspacioActual(persona.trabajo)
                    self.trabajos[persona.trabajo-(self.casasContador+self.lugaresTrasporte+self.lugaresEscuelas)].addPersona(persona)
                    self.trasportes[persona.trasposte-self.casasContador].removePersona(persona)
                    continue
                #persona.setEspacioActual(persona.trabajo)

                #self.trasportes[persona.trasposte].addPersona(persona)
                #self.casas[persona.casa].removePersona(persona)
                #print(persona.trasposte - (self.casasContador + self.lugaresEscuelas + self.lugaresTrabajos))
                #print(persona.trasposte)
                #print("============================")

        # for casa in casas:
        #     print(f"La casa {casa.id} tiene {len(casa.listaAutomatasContenidos)}")
        #     for persona in listaPersona:
        #
        #         if (persona in casa.listaAutomatasContenidos):
        #             if (persona.edad >= 0 and persona.edad <= 1):
        #                 persona.setEspacioActual(escuelas[0].id)
        #                 escuelas[0].addPersona(persona)
        #                 persona.setTrabajo(escuelas[0].id)
        #                 casa.removePersona(persona)
        #
        #             if (persona.edad >= 2 and persona.edad <= 4):
        #                 persona.setEspacioActual(trabajos[0].id)
        #                 trabajos[0].addPersona(persona)
        #                 persona.setTrabajo(trabajos[0].id)
        #                 casa.removePersona(persona)
        #
        #             if (persona.edad > 4):
        #                 persona.setEspacioActual(trasportes[0].id)
        #                 trasportes[0].addPersona(persona)
        #                 persona.setTrasposte(trasportes[0].id)
        #                 casa.removePersona(persona)

    def filtrarEspacios(self):
        for espacio in self.espacioInstancia:
            if(espacio.nombre=="Casa"):
                self.casas.append(espacio)
                continue
            if (espacio.nombre == "Trabajo"):
                self.trabajos.append(espacio)
                continue
            if (espacio.nombre == "Trasporte"):
                self.trasportes.append(espacio)
                continue
            if (espacio.nombre == "Escuela"):
                self.escuelas.append(espacio)
                continue
        #por cada persona en cada casa lo agrega a una lista
        for casa in self.casas:
            for persona in casa.listaAutomatasContenidos:
                self.personas.append(persona)

