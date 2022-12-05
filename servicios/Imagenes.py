from matplotlib import pyplot as plt
from EspaciosTrabajo.Espacio import Espacio
from EspaciosTrabajo.Casa import Casa
from modelo.Persona import Persona

class Imagenes:

    def __init__(self, espacios):
        self.espacios= espacios
        self.listaFormatosGrafica = ["o", "d", "v", "s"]


    def obtenerImagenMatriz(self):
        self.listaCoordenadasX = []
        self.listaCoordenadasY = []

        fig, ax = plt.subplots()
        ax.axis([0, self.espacios.dim, 0,  self.espacios.dim])

        for persona in self.espacios.listaAutomatasContenidos:
            self.listaCoordenadasX.append(persona.ubicacionX)
            self.listaCoordenadasY.append(persona.ubicacionY)

        ax.plot(self.listaCoordenadasX, self.listaCoordenadasY, self.listaFormatosGrafica[0])
        ax.set_title(f" Casa {self.espacios.id}")  # Add a title to the axes.
        self.nombreImagen = f"EspaciosEtapa\\Casa_{self.espacios.id}.png"
        plt.savefig(self.nombreImagen)
        plt.close()



        #self.nombreImagen=f"Casa\\Etapa_{self.matrix.contadorImagen}.png"
        # plt.savefig(self.nombreImagen)
        # plt.close()
        # self.matrix.contadorImagen = self.matrix.contadorImagen + 1;
