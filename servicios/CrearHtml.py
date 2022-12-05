import os
from modelo.HtmlTablas import HtmlTablas
from EspaciosTrabajo.Espacio import Espacio
from EspaciosTrabajo.Casa import Casa
from EspaciosTrabajo.Escuela import Escuela
from EspaciosTrabajo.Trabajo import Trabajo
from EspaciosTrabajo.Trasporte import Trasporte
from modelo.Persona import Persona;

class CrearHtml:
    def __init__(self, espacios):
        self.espacios = espacios

    def crear(self):
        file = open(f"TablasHtmls/{self.espacios.nombre}{self.espacios.id}.html", "w")
        html = HtmlTablas(self.espacios)
        file.write(html.ObtenerHtml())
        file.close()
