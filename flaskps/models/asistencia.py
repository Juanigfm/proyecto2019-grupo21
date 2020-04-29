class Asistencia(object):

    db = None

    @classmethod
    def all(cls):
        sql = 'SELECT * FROM asistencia'
        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()

    @classmethod
    def get_asistencia_by_fecha_y_clase(cls, clase_id, fecha):
        sql = """
            SELECT * 
            FROM asistencia
            WHERE clase_id = %s and fecha = %s
            """
        cursor = cls.db.cursor()
        cursor.execute(sql, (clase_id, fecha))

        return cursor.fetchall()

    @classmethod
    def insert_asistencia_de_estudiante(cls, presente, estudiante_id, clase_id, estudiante_apellido, estudiante_nombre, estudiante_documento, fecha):
        if presente == True:
            presente = 1
        else:
            presente = 0
        sql =  """
                INSERT INTO asistencia (presente, estudiante_id, clase_id, estudiante_apellido, estudiante_nombre, estudiante_documento, fecha)
                VALUES ("""+ str(presente) +","+str(estudiante_id)+","+str(clase_id)+",'"+estudiante_apellido+"','"+estudiante_nombre+"',"+str(estudiante_documento)+",'"+fecha+"');"
        cursor = cls.db.cursor()
        # cursor.execute(sql,(presente, estudiante_id, int(clase_id), estudiante_apellido, estudiante_nombre, estudiante_documento))
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def insert_asistencias_log(cls, fecha, clase_id):
        sql =  """
                INSERT INTO log_clase (fecha, clase_id)
                VALUES (%s,%s);
                """
        cursor = cls.db.cursor()
        cursor.execute(sql,(fecha, clase_id))
        return cursor.fetchall()

    @classmethod
    def get_registro_by_clase_fecha(cls, clase_id, fecha):
        sql = """
            SELECT *
            FROM log_clase
            WHERE clase_id ="""+str(clase_id)+" and fecha = '"+fecha+"'"
        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()
