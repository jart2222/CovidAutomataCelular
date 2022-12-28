from repositorio.Repositorio import Repositorio
from servicios.AsignacionLugares import AsignacionLugares
from servicios.Imagenes import Imagenes
from servicios.Directorio import Directorio
asignacionLugares=AsignacionLugares(2,10,5)#casas,dim,subEtapas
directorio=Directorio()
repositorio=Repositorio()


repositorio.truncarInfo()

try:
    directorio.borrarDirectorio();
finally:
    directorio.crearDirectorio()

asignacionLugares.asignarEspacioPersona()

for espacio in asignacionLugares.espacioInstancia:
          imagenes = Imagenes(espacio)
          imagenes.obtenerImagenMatriz()
          repositorio.insertarEspacios(espacio)
          repositorio.insertarPersona(espacio)

for i in range(4):
     asignacionLugares.moverPersonaEspacio()
     for espacio in asignacionLugares.espacioInstancia:
          imagenes = Imagenes(espacio)
          imagenes.obtenerImagenMatriz()
          repositorio.insertarEspacios(espacio)
          repositorio.insertarPersona(espacio)
          espacio.dectarVecinoAutomata()


repositorio.cerrarConexion()
#crearHtml =CrearHtml(espacio)
# crearHtml.crear()
