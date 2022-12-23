from matplotlib import pyplot as plt


class Imagenes:

    def __init__(self, espacios):
        self.espacios= espacios
        self.listaFormatosGrafica = ["o", "d", "v", "s"]


    def obtenerImagenMatriz(self):
        self.listaCoordenadasX = []
        self.listaCoordenadasY = []



        espacio=self.espacios.listaAutomatasContenidos
        if len(espacio)>0:
            for persona in espacio:
                self.listaCoordenadasX.append(persona.ubicacionX)
                self.listaCoordenadasY.append(persona.ubicacionY)

            fig, ax = plt.subplots()
            ax.axis([0, self.espacios.dim, 0, self.espacios.dim])
            ax.plot(self.listaCoordenadasX, self.listaCoordenadasY, self.listaFormatosGrafica[0])
            ax.set_title(f" Etapa: {self.espacios.etapa} {self.espacios.nombre} {self.espacios.id}")  # Add a title to the axes.
            #self.nombreImagen = f"EspaciosEtapa\\{self.espacios.nombre}_N{self.espacios.id}_E{self.espacios.etapa}.png"
            self.nombreImagen = f"EspaciosEtapa\\Etapa_{self.espacios.etapa}_{self.espacios.nombre}_{self.espacios.id}.png"
            plt.savefig(self.nombreImagen)
            plt.close()



        #self.nombreImagen=f"Casa\\Etapa_{self.matrix.contadorImagen}.png"
        # plt.savefig(self.nombreImagen)
        # plt.close()
        # self.matrix.contadorImagen = self.matrix.contadorImagen + 1;
