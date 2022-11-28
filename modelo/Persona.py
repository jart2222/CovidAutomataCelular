# coding=System

class Persona(object):

  """
   

  :version:
  :author:
  """

  """ ATTRIBUTES

   Edad del individuo que va de en rangos de 1-7, osea de 0-10, 10-20.....70 o mas

  edad  (private)

   puedes ser un numero entre 1-4,  las enfermedades cronicas podrian ser diabetis,
   hipertension, obesidad, ITS

  enfermedadesCronicas  (private)

   Si el individuo esta contagiado o no

  contagiado  (private)

   Si el individuo esta vacunado o no
   

  vacunado  (private)

   Si el individuo recientemente tuvo la enfermedad y posee inmunidad

  inmunidadAdquirida  (private)

   numero entre 0-1, inicialmente es 0

  factorDeRiesgo  (private)

   

  idPersona  (private)

   

  diasInfectado  (private)

   El dia que adquiere la enfermedad
   

  diaAdquisicionVirus  (private)

   Ubicacion X en matriz

  ubicacionX  (private)

   ubicacion Y en matriz
   

  ubicacionY  (private)

   

  espaciosC_  (private)

  """

  def asignarFactorRiesgo(self):
    """
     Asigna factor de riesgo, la cual esta dictada por las variables sexo,edad,
     enfermedades cronicas, vacunado, inmunidad

    @return  :
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



