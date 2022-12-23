import random
from EspaciosTrabajo.Casa import Casa
from EspaciosTrabajo.Escuela import Escuela
from EspaciosTrabajo.Trabajo import Trabajo
from EspaciosTrabajo.Trasporte import Trasporte
from modelo.Persona import Persona;


class AsignacionLugares:
    def __init__(self,casas,dim):
        self.dim=dim
        self.lugaresCasas=casas;
        self.espacioInstancia = []
        self.dias = 0
        self.contadorLugares=0;
        self.lugaresTrasporte=random.randint(1,casas);
        self.lugaresEscuelas=random.randint(1,casas);
        self.lugaresTrabajos=random.randint(1,casas);
        self.contadorEtapas=0;
        self.idIndividuos=0;
        self.casas = []
        self.trasportes = []
        self.trabajos = []
        self.escuelas = []
        self.personas = []
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
        for i in range(self.lugaresCasas):
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
            #print(f"La casa {casa.id} tiene {len(casa.listaAutomatasContenidos)}")
            for persona in self.personas:
                if (persona in casa.listaAutomatasContenidos):
                    if (persona.edad >= 0 and persona.edad <= 1):
                        persona.setTrabajo(self.escuelas[random.randint(0,self.lugaresEscuelas-1)].id)
                        persona.setTrasposte(self.trasportes[random.randint(0, self.lugaresTrasporte - 1)].id)
                    if (persona.edad >= 2 and persona.edad < 6):
                        persona.setTrabajo(self.trabajos[random.randint(0, self.lugaresTrabajos - 1)].id)
                        persona.setTrasposte(self.trasportes[random.randint(0, self.lugaresTrasporte - 1)].id)
                    if (persona.edad >= 6):
                        continue

    def moverPersonaEspacio(self):
        self.aumentarEtapa()

        for persona in self.personas:
            idEspacioActual = persona.espacioActual
            edad = persona.edad

            if ((idEspacioActual < self.lugaresCasas) and (
                    edad < 6)):  # persona esta en su casa y por su edad tiene que tomar el trasporte
                trasporte = self.trasportes[persona.trasposte - (self.lugaresCasas)]
                casa = self.casas[persona.casa]
                self.cambioEspacio(persona, trasporte, casa, persona.trasposte)
                continue

            if ((idEspacioActual >= self.lugaresCasas) and (idEspacioActual < (
                    self.lugaresCasas + self.lugaresTrasporte))):  # persona se encuentra en el trasporte

                trasporte = self.trasportes[persona.trasposte - self.lugaresCasas]

                if (self.contadorEtapas % 4 == 0):  # etapa en que las personas ya fueron al trabajo y regresan
                    casa = self.casas[persona.casa]
                    self.cambioEspacio(persona, casa, trasporte, persona.casa)
                    continue

                else:  # personas que van al trabajo
                    if (edad >= 0 and edad < 2):
                        escuela = self.escuelas[persona.trabajo - (self.lugaresCasas + self.lugaresTrasporte)]
                        self.cambioEspacio(persona, escuela, trasporte, persona.trabajo)
                        continue
                    if (edad >= 2 and edad <= 6):
                        trabajo = self.trabajos[
                            persona.trabajo - (self.lugaresCasas + self.lugaresTrasporte + self.lugaresEscuelas)]
                        self.cambioEspacio(persona, trabajo, trasporte, persona.trabajo)
                        continue

            if ((idEspacioActual >= (
                    self.lugaresCasas + self.lugaresTrasporte))):  # persona se encuentra en el trabajo y toma el trasporte para llegar a su casa
                trasporte = self.trasportes[persona.trasposte - self.lugaresCasas]
                if (edad >= 0 and edad < 2):
                    escuela = self.escuelas[persona.trabajo - (self.lugaresCasas + self.lugaresTrasporte)]
                    self.cambioEspacio(persona, trasporte, escuela, persona.trasposte)
                    continue

                if (edad >= 2 and edad <= 6):
                    trabajo = self.trabajos[
                        persona.trabajo - (self.lugaresCasas + self.lugaresTrasporte + self.lugaresEscuelas)]
                    self.cambioEspacio(persona, trasporte, trabajo, persona.trasposte)
                    continue

    def filtrarEspacios(self):
        for espacio in self.espacioInstancia:
            if (espacio.nombre == "Casa"):
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
        # por cada persona en cada casa lo agrega a una lista
        for casa in self.casas:
            for persona in casa.listaAutomatasContenidos:
                self.personas.append(persona)

    def aumentarEtapa(self):
        self.contadorEtapas += 1
        for espacio in self.espacioInstancia:
            espacio.setEtapa(self.contadorEtapas)

    def cambioEspacio(self, persona, espacioP, espacioA, asignacionE):
        persona.setEspacioActual(asignacionE)
        espacioP.addPersona(persona)
        espacioA.removePersona(persona)
