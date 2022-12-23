class Persona():
  def __init__(self,idPersona,edad,sexo,emfermedadesCronicas,contagiado,vacunado,ubicacionX,ubicacionY,espacioActual):
    self.idPersona=idPersona;
    self.edad=edad;
    self.sexo=sexo;
    self.emfermedadesCronicas=emfermedadesCronicas;
    self.contagiado=contagiado;
    self.vacunado=vacunado;
    self.ubicacionX = ubicacionX;
    self.ubicacionY = ubicacionY;
    self.espacioActual = espacioActual;
    self.vivo = True;
    self.inmunidadAdquiridad = False;
    self.casa=espacioActual
    self.factorDeRiesgo = self.asignarFactorRiesgo();
    self.diasInfectado = 0;
    self.diasAdquisicionVirus = 0;
    self.espaciosC = [];
    self.trasposte=0;
    self.trabajo=0;

    def asignarFactorRiesgo(self):
        """
         Asigna factor de riesgo, la cual esta dictada por las variables sexo,edad,
         enfermedades cronicas, vacunado, inmunidad

        @return  factor de riego de la persona segun sus caracterisiticas :
        @author
        """

        riesgo = self.edad;

        if (self.sexo == "H"):
            riesgo = riesgo + 1;

        if (self.emfermedadesCronicas > 0):
            riesgo = riesgo + self.emfermedadesCronicas;

        return riesgo;

    def asignacionMovimientoAutomata(self, movimientoX, movimientoY):  # Le asigna el movimiento a cada automata
        self.movimientoX = movimientoX;
        self.movimientoY = movimientoY;

    def moverAutomata(self):  # Cambia de ubicacion del automata ocupando el movimiento
        if ((
                self.ubicacionY + self.movimientoY) < 0):  # si la suma de la ubicacion y movimiento es cero se mueve al otro extremo de la matriz
            self.ubicacionY = self.dimension - 1;

        elif ((
                      self.ubicacionY + self.movimientoY) >= self.dimension):  # si cumple se mueve al otro extremo de la matriz
            self.ubicacionY = 0;

        else:
            self.ubicacionY = self.ubicacionY + self.movimientoY

        if ((self.ubicacionX + self.movimientoX) < 0):  # si cumple se mueve al otro extremo de la matriz
            self.ubicacionX = self.dimension - 1;

        elif ((
                      self.ubicacionX + self.movimientoX) >= self.dimension):  # si cumple se mueve al otro extremo de la matriz
            self.ubicacionX = 0;

        else:
            self.ubicacionX = self.ubicacionX + self.movimientoX

    def setEspacioActual(self, idEspacio):
        """recibe espacio al que pertenece"""
        self.espacioActual = idEspacio

    def setTrabajo(self, id):
        self.trabajo = id;

    def setTrasposte(self, id):
        self.trasposte = id;

    def vidaMuerte(self, azar):
        """
         Al factor del riego se le suma un numero al azar y si el resultado es mayor que
         1 es individo cambia la variable vida a false

        @param undef azar : Numero azar

        @return  :
        @author
        """
        pass

    def __eq__(self, persona):
        return self.idPersona == persona.idPersona
        # return (self.ubicacionX == persona.ubicacionX and self.ubicacionY == persona.ubicacionY)

    def __str__(self) -> str:

        info = f"Persona: {self.idPersona}\n\t" \
               f"Edad: {self.edad} \n\t" \
               f"Sexo: {self.sexo} \n\t" \
               f"EmfermedadesCronica: {self.emfermedadesCronicas} \n\t" \
               f"Contiagado: {self.contagiado} \n\t" \
               f"Vacunado: {self.vacunado} \n\t" \
               f"Ubicacion: ({self.ubicacionX},{self.ubicacionY}) \n\t" \
               f"Vivo: {self.vivo} \n\t" \
               f"Inmunidad: {self.inmunidadAdquiridad} \n\t" \
               f"Factor de riesgo: {self.factorDeRiesgo} \n\t"

        if (self.contagiado):
            return info + \
                   f"Dias de infectado: {self.diasInfectado} \n\t" \
                   f"Dias de Adquision del Virus: {self.diasAdquisicionVirus} \n\t"

        else:
            return info
