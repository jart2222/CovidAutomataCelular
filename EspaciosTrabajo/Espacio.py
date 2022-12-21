import numpy as np;
class Espacio():
  def __init__(self,dim,id,nombre):
    self.id=id;
    self.nombre=nombre;
    self.dim = dim;
    self.a = np.zeros((dim,dim));
    self.etapa=0;
    self.listaAutomatasContenidos = []
    self.arregloEnteros1 = [*range(-1, 2, 1)]
    self.arregloEnteros2 = [*range(-1, 2, 1)]

  def dectarVecinoAutomata(self):
    """
     Por cada automata en la lista, bu	sca si hay otro en la lista que sea vecino

    @return  :
    @author
    """
    pass

  def setEtapa(self, etapa):
    self.etapa=etapa
  def darMovimientoAutomata(self):
    """
     Le asigna un movimiento a cada automata

    @return  :
    @author
    """
    pass

  def moverAutomata(self):
    """
     Corre el metodo de cambiar ubicicacion(Movimiento) a cada Automata en la lista

    @return  :
    @author
    """
    pass

  def nuevaMatriz(self):
    """
     cambia la matriz a con las nuevas ubicaciones de cada automata

    @return  :
    @author
    """
    pass

  def obtenerImagenMatriz(self):
    """
     Obtiene la imagen de la matriz en cada etapa

    @return  :
    @author
    """
    pass

  def addPersona(self, persona):
    if persona not in self.listaAutomatasContenidos :
      self.listaAutomatasContenidos.append(persona);
      self.a[persona.ubicacionX, persona.ubicacionY] = 1

  def removePersona(self, persona):

    if persona in self.listaAutomatasContenidos:
      self.listaAutomatasContenidos.remove(persona);
      self.a[persona.ubicacionX, persona.ubicacionY] = 0
      #print(f"\t\tSI me elimine de espacio {self.id} la persona con id {persona.idPersona}")
    else:
      print(f"\t\tNO me elimine de espacio {self.id} la persona con id {persona.idPersona}")


  def __str__(self) -> str:
    texto=f"Espacio: {self.nombre}\n" \
          f" id: {self.id}\n " \
          f"dim: {self.dim}"

    if(len(self.listaAutomatasContenidos)>=0):
      for automata in self.listaAutomatasContenidos:
        texto+=str(automata)+"\n"

    return texto
