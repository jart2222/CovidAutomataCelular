from servicios.AsignacionLugares import AsignacionLugares
from servicios.Imagenes import Imagenes
from modelo.HtmlTablas import HtmlTablas
from servicios.CrearHtml import CrearHtml
from repositorio.Repositorio import Repositorio

asignacionLugares=AsignacionLugares(5,10)
asignacionLugares.asignarEspacioPersona()
repositorio=Repositorio()
repositorio.truncarInfo()

for espacio in asignacionLugares.espacioInstancia:
     imagenes=Imagenes(espacio)
     imagenes.obtenerImagenMatriz()
     repositorio.insertarEspacios(espacio)
     repositorio.insertarPersona(espacio)


repositorio.cerrarConexion()
#crearHtml =CrearHtml(espacio)
# crearHtml.crear()
