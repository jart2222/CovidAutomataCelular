import random
from servicios.AsignacionLugares import AsignacionLugares
from servicios.Imagenes import Imagenes

asignacionLugares=AsignacionLugares(5,10)
for espacio in asignacionLugares.espacioInstancia:
    print(espacio)
    imagenes=Imagenes(espacio)
    imagenes.obtenerImagenMatriz()
