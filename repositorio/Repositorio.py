from EspaciosTrabajo.Espacio import *
import pymysql
class Repositorio (Espacio):
  def __init__(self):
      self.connection = pymysql.connect(
        host='localhost',
        user='root',
        password='MyNewPass',
        db='covid19_automatas'
      )
      self.cursor = self.connection.cursor()

  def insertarEspacios(self,espacio):
    try:
      sqlEspacios="INSERT INTO `covid19_automatas`.`espacios` (`id_espacio`, `nombre`, `dimension`, `personas_contenidas`) " \
         f"VALUES ({espacio.id}, '{espacio.nombre}', '{espacio.dim}', {len(espacio.listaAutomatasContenidos)});"
      self.cursor.execute(sqlEspacios);
    except Exception as e:
      print(e)
      self.connection.rollback()

  def truncarInfo(self):
    try:
      self.cursor.execute("""truncate table covid19_automatas.espacios;""")
      self.cursor.execute("""truncate table covid19_automatas.persona;""")
      self.connection.commit();
    except Exception as e:
      print(e)
      self.connection.rollback()



  def insertarPersona(self, espacio):
    try:
      for persona in espacio.listaAutomatasContenidos:
        sql = f"""INSERT INTO `covid19_automatas`.`persona`
               (`id_persona`, `edad`, `sexo`, `emfermedades_cronicas`, `contagiado`,
               `vacunado`, `ubicacion_x`, `ubicacion_y`, `vivo`, `inmunidad_adquiridad`,
                `factor_de_riesgo`, `dias_infectado`, `dias_adquisicion_virus`,`id_espacio`,`trasporte`,`trabajo`,`casa`)
              VALUES ('{persona.idPersona}', '{persona.edad}', '{persona.sexo}', '{persona.emfermedadesCronicas}', '{int(persona.contagiado)}',
               '{int(persona.vacunado)}', '{persona.ubicacionX}', '{persona.ubicacionY}', '{int(persona.vivo)}', '{int(persona.inmunidadAdquiridad)}',
                '{persona.factorDeRiesgo}', '{persona.diasInfectado}', '{persona.diasAdquisicionVirus}', '{espacio.id}', '{persona.trasposte} ', 
                '{persona.trabajo}', '{persona.casa}');"""
        self.cursor.execute(sql);
      self.connection.commit()

    except Exception as e:
      self.connection.rollback()
      print(e)



  def cerrarConexion(self):
    self.cursor.close()
    self.connection.close()



