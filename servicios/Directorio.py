import os
import shutil

class Directorio:
    def __init__(self):
        self.ruta=os.getcwd()+"\EspaciosEtapa"

    def borrarDirectorio(self):
        if os.path.exists(self.ruta):
            print("Carpeta borrada: "+self.ruta );
            shutil.rmtree(self.ruta)
        else:
            print("No existe la carpeta: "+self.ruta )



    def crearDirectorio(self):
        if not os.path.exists(self.ruta):
            print("Carpeta creada: "+self.ruta);
            os.makedirs(self.ruta)
        else:
            print("Ya existe la carpeta "+self.ruta  )




