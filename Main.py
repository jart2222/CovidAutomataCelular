from servicios.AsignacionLugares import AsignacionLugares
from servicios.Imagenes import Imagenes
from modelo.HtmlTablas import HtmlTablas
from servicios.CrearHtml import CrearHtml


asignacionLugares=AsignacionLugares(5,10)
for espacio in asignacionLugares.espacioInstancia:
    print(espacio)
    imagenes=Imagenes(espacio)
    crearHtml =CrearHtml(espacio)
    crearHtml.crear()
    imagenes.obtenerImagenMatriz()
