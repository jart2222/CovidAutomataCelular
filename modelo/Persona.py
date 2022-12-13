
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


  def setEspacioActual(self, idEspacio):
      self.espacioActual=idEspacio
  def asignarFactorRiesgo(self):
    """
     Asigna factor de riesgo, la cual esta dictada por las variables sexo,edad,
     enfermedades cronicas, vacunado, inmunidad

    @return  factor de riego de la persona segun sus caracterisiticas :
    @author
    """

    riesgo=self.edad;

    if(self.sexo=="H"):
        riesgo = riesgo+1;

    if (self.emfermedadesCronicas >0):
        riesgo=riesgo+self.emfermedadesCronicas;

    return riesgo;
  def setTrabajo(self, id):
      self.trabajo= id;
  def setTrasposte(self, id):
      self.trasposte= id;

  def vidaMuerte(self, azar):
    """
     Al factor del riego se le suma un numero al azar y si el resultado es mayor que
     1 es individo cambia la variable vida a false

    @param undef azar : Numero azar 

    @return  :
    @author
    """
    pass

  def asignarEspacios(self, espacio):
    """
     recibe espacio al que pertenece

    @param Espacio espacio : 
    @return  :
    @author
    """
    pass

  def __eq__(self, persona):
      return (self.ubicacionX == persona.ubicacionX and self.ubicacionY == persona.ubicacionY)

  def __str__(self) -> str:

      info=f"Persona: {self.idPersona}\n\t" \
           f"Edad: {self.edad} \n\t" \
           f"Sexo: {self.sexo} \n\t" \
           f"EmfermedadesCronica: {self.emfermedadesCronicas} \n\t" \
           f"Contiagado: {self.contagiado} \n\t" \
           f"Vacunado: {self.vacunado} \n\t" \
           f"Ubicacion: ({self.ubicacionX},{self.ubicacionY}) \n\t" \
           f"Vivo: {self.vivo} \n\t" \
           f"Inmunidad: {self.inmunidadAdquiridad} \n\t" \
           f"Factor de riesgo: {self.factorDeRiesgo} \n\t"

      if(self.contagiado):
          return info+\
                 f"Dias de infectado: {self.diasInfectado} \n\t" \
                 f"Dias de Adquision del Virus: {self.diasAdquisicionVirus} \n\t"

      else:
           return info


