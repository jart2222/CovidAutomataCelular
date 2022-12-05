from EspaciosTrabajo.Espacio import Espacio

class Casa (Espacio):

  """
   

  :version:
  :author:
  """

  def __int__(self, dim, id):
    super().__int__(dim,id)

  def __str__(self) -> str:
    return super().__str__("Casa")



