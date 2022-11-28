
class Persona():

  def __init__(self,idPersona,edad,sexo,emfermedadesCronicas,contagiado,vacunado,ubicacionX,ubicacionY):
    self.idPersona=idPersona;
    self.edad=edad;
    self.sexo=sexo;
    self.emfermedadesCronicas=emfermedadesCronicas;
    self.contagiado=contagiado;
    self.vacunado=vacunado;
    self.ubicacionX = ubicacionX;
    self.ubicacionY = ubicacionY;
    self.vivo=True;
    self.inmunidadAdquiridad=False;
    self.factorDeRiesgo=0;
    self.diasInfectado = 0;
    self.diasAdquisicionVirus = 0;
    self.espaciosC=[];

  def asignarFactorRiesgo(self):
    """
     Asigna factor de riesgo, la cual esta dictada por las variables sexo,edad,
     enfermedades cronicas, vacunado, inmunidad

    @return  factor de riego de la persona segun sus caracterisiticas :
    @author
    """
    pass

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



