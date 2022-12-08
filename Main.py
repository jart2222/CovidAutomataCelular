from servicios.AsignacionLugares import AsignacionLugares
from servicios.Imagenes import Imagenes
from modelo.HtmlTablas import HtmlTablas
from servicios.CrearHtml import CrearHtml
from repositorio.Repositorio import Repositorio

asignacionLugares=AsignacionLugares(5,10)
repositorio=Repositorio()
repositorio.truncarInfo()

for espacio in asignacionLugares.espacioInstancia:
    imagenes=Imagenes(espacio)
    repositorio.insertarInfo(espacio)
    imagenes.obtenerImagenMatriz()


#crearHtml =CrearHtml(espacio)
# crearHtml.crear()
