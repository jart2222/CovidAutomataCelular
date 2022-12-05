from EspaciosTrabajo.Espacio import Espacio
from EspaciosTrabajo.Casa import Casa
from EspaciosTrabajo.Escuela import Escuela
from EspaciosTrabajo.Trabajo import Trabajo
from EspaciosTrabajo.Trasporte import Trasporte
from modelo.Persona import Persona;
class HtmlTablas:
    def __init__(self, espacios):
        self.espacios= espacios
        self.texto=""

    def ObtenerHtml(self):


        self.texto=f"""<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>{self.espacios.nombre}: {self.espacios.id}</title>
                <link rel="stylesheet" href="css/estilos.css">

            </head>
            <body>
            <h1> {self.espacios.nombre}: {self.espacios.id}</h1>
            
            
            <table>
                <tr>
                    <th>Persona id</th>
                    <th>Edad</th>
                    <th>Sexo</th>
                    <th>Emfermedades Cronicas</th>
                    <th>Contiagado</th>
                    <th>Vacunado</th>
                    <th>Ubicacion</th>
                    <th>Vivo</th>
                    <th>Inmunidad</th>
                    <th>Factor de riesgo</th>
                </tr>"""

        for persona in self.espacios.listaAutomatasContenidos:
            self.texto+=f"""
                <tr>
                    <td>{persona.idPersona}</td>
                    <td>{persona.edad}</td>
                    <td>{persona.sexo}</td>
                    <td>{persona.emfermedadesCronicas}</td>
                    <td>{persona.contagiado}</td>
                    <td>{persona.vacunado}</td>
                    <td>({persona.ubicacionX},{persona.ubicacionY})</td>
                    <td>{persona.vivo}</td>
                    <td>{persona.inmunidadAdquiridad}</td>
                    <td>{persona.factorDeRiesgo}</td>

                </tr>
            """

        self.texto+="""</table>
                </body>
                </html>"""

        return self.texto;