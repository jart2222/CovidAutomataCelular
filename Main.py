from repositorio.Repositorio import Repositorio
from servicios.AsignacionLugares import AsignacionLugares
from servicios.Imagenes import Imagenes

asignacionLugares=AsignacionLugares(5,10)
asignacionLugares.asignarEspacioPersona()
repositorio=Repositorio()
repositorio.truncarInfo()

for espacio in asignacionLugares.espacioInstancia:
          imagenes = Imagenes(espacio)
          imagenes.obtenerImagenMatriz()
          repositorio.insertarEspacios(espacio)
          repositorio.insertarPersona(espacio)

for i in range(8):
     asignacionLugares.moverPersonaEspacio()
     for espacio in asignacionLugares.espacioInstancia:
          imagenes = Imagenes(espacio)
          imagenes.obtenerImagenMatriz()
          repositorio.insertarEspacios(espacio)
          repositorio.insertarPersona(espacio)


repositorio.cerrarConexion()
#crearHtml =CrearHtml(espacio)
# crearHtml.crear()
