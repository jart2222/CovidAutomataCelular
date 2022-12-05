import numpy as np;
class Espacio():
  def __init__(self,dim,id):
    self.id=id;
    self.dim = dim;
    self.a = np.zeros((dim,dim));
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

  def __str__(self, nombre) -> str:
    texto=f"Espacio: {nombre}\n" \
          f" id: {self.id}\n "

    if(len(self.listaAutomatasContenidos)>0):
      for automata in self.listaAutomatasContenidos:
        texto+=str(automata)+"\n "

    return texto
