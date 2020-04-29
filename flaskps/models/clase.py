class Clase(object):

    db = None

    @classmethod
    def delete(cls, id):
        sql = """
            UPDATE clase SET activo = 0 WHERE id = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, id)
        cls.db.commit()
        return True

    @classmethod
    def desasignar(cls, id):
        sql = """
            UPDATE clase SET activo = 0, taller_id = NULL WHERE taller_id = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, id)
        cls.db.commit()
        return True

    @classmethod
    def update(cls, dia, hora_inicio, hora_fin, docente_id, id):
        sql = """
            UPDATE clase SET dia = %s, 
            hora_inicio = %s, 
            hora_fin = %s, 
            docente_id = %s
            WHERE id = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (dia, hora_inicio, hora_fin, docente_id, id))
        cls.db.commit()
        return True

    @classmethod
    def all(cls):
        sql = """
                SELECT *
                FROM clase
                """
        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()
    
    @classmethod
    def create(cls, dia, hora_inicio , hora_fin, taller_id, docente_id):
        sql = """
                INSERT INTO clase (dia, hora_inicio , hora_fin, taller_id, docente_id, activo)
                VALUES (%s,%s,%s,%s,%s, 1);
                """

        cursor = cls.db.cursor()
        cursor.execute(sql, (dia, hora_inicio , hora_fin, taller_id, docente_id))
        cls.db.commit()
        return True

    # @classmethod
    # def add_docente_clase(cls, docente_id, clase_id):
    #     sql = """
    #             INSERT INTO docente_clase (docente_id, clase_id)
    #             VALUES (%s,%s);
    #             """
    #     cursor = cls.db.cursor()
    #     cursor.execute(sql, (docente_id, clase_id))
    #     # cls.db.commit()
    #     return cursor.fetchone()

    @classmethod
    def get_clases_by_taller(cls, taller_id):
        sql = """
                SELECT c.*, d.nombre, d.apellido
                FROM clase c 
                INNER JOIN docente d ON c.docente_id = d.id 
                WHERE c.activo = 1 and c.taller_id = %s
                """
        cursor = cls.db.cursor()
        cursor.execute(sql, taller_id)
        return cursor.fetchall()

    @classmethod
    def get_clases_by_docente_taller(cls, docente_id, taller_id):
        sql = """
                SELECT count(c.id) as cantidadClases
                FROM clase c 
                WHERE c.activo = 1 and c.taller_id = %s and c.docente_id = %s
                """
        cursor = cls.db.cursor()
        cursor.execute(sql, (taller_id, docente_id))
        return cursor.fetchone()

    @classmethod
    def get_clases_by_docente(cls, docente_id):
        sql = """
                SELECT c.*, t.nombre as nombreTaller, n.nombre as nombreNucleo
                FROM clase c 
                INNER JOIN taller t ON c.taller_id = t.id 
                INNER JOIN nucleo n ON t.nucleo_id = n.id
                WHERE c.activo = 1 and c.docente_id = %s
                """
        cursor = cls.db.cursor()
        cursor.execute(sql, docente_id)
        return cursor.fetchall()

    @classmethod
    def get_clases_de_taller(cls, taller_id):
        sql = """
                SELECT c.dia as diaclase, c.hora_inicio as iniclase, c.hora_fin as finclase, lc.fecha as fechalog, lc.id as idlog
                FROM clase c 
                INNER JOIN log_clase lc ON c.id = lc.clase_id
                WHERE activo = 1 and taller_id = %s
                """
        cursor = cls.db.cursor()
        cursor.execute(sql, taller_id)
        return cursor.fetchall()

    @classmethod
    def get_log_by_id(cls, idlog):
        sql = """
                SELECT *
                FROM log_clase
                WHERE id = %s
                """
        cursor = cls.db.cursor()
        cursor.execute(sql, idlog)
        return cursor.fetchone()

