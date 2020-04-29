class Estudiante(object):

    db = None

    @classmethod
    def all(cls):
        sql = 'SELECT * FROM estudiante'
        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()

    @classmethod
    def create(cls, apellido, nombre, fecha_nac, localidad_id, nivel_id, domicilio, genero_id, escuela_id, tipo_doc_id, numero, tel, barrio_id):
        sql = """
            INSERT INTO estudiante (apellido, 
                                    nombre, 
                                    fecha_nac, 
                                    localidad_id, 
                                    nivel_id, 
                                    domicilio, 
                                    genero_id, 
                                    escuela_id, 
                                    tipo_doc_id, 
                                    numero, 
                                    tel, 
                                    barrio_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """

        sqlid = "SELECT LAST_INSERT_ID() as idInsertado"

        cursor = cls.db.cursor()
        cursor.execute(sql, (apellido, nombre, fecha_nac, localidad_id, nivel_id, domicilio, genero_id, escuela_id, tipo_doc_id, numero, tel, barrio_id))
        # cls.db.commit()
        cursor.execute(sqlid)
        return cursor.fetchone()

    @classmethod
    def add_responsable(cls, idResponsable, idEstudiante):
        sql = """
            INSERT INTO responsable_estudiante (responsable_id, estudiante_id)
            VALUES (%s, %s)
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (idResponsable, idEstudiante))
        # cls.db.commit()
        return True
    
    @classmethod
    def delete_responsable(cls, idEstudiante):
        sql = """
            DELETE FROM responsable_estudiante WHERE estudiante_id = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (idEstudiante))
        # cls.db.commit()
        return True

    @classmethod
    def update(cls, apellido, nombre, fecha_nac, localidad_id, nivel_id, domicilio, genero_id, escuela_id, tipo_doc_id, numero, tel, barrio_id, id):
        sql = """
            UPDATE estudiante SET   apellido = %s, 
                                    nombre = %s, 
                                    fecha_nac = %s, 
                                    localidad_id = %s, 
                                    nivel_id = %s, 
                                    domicilio = %s, 
                                    genero_id = %s, 
                                    escuela_id = %s, 
                                    tipo_doc_id = %s, 
                                    numero = %s, 
                                    tel = %s, 
                                    barrio_id = %s
            WHERE id = %s
            ;
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (apellido, nombre, fecha_nac, localidad_id, nivel_id, domicilio, genero_id, escuela_id, tipo_doc_id, numero, tel, barrio_id, id))
        cls.db.commit()
        return True

    @classmethod
    def delete(cls, id):
        sql = """
            DELETE
            FROM estudiante
            WHERE id=%s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, id)
        cursor.connection.commit()
        return True
    
    @classmethod
    def find_by_id_and_responsable(cls, id):
        sql = """
            SELECT * FROM estudiante
            INNER JOIN responsable_estudiante re ON id = estudiante_id 
            WHERE id = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, id)
        return cursor.fetchone()

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT es.*, g.nombre as nomGenero, esc.nombre as nomEscuela, b.nombre as nomBarrio 
            FROM estudiante es
            INNER JOIN genero g ON es.genero_id = g.id
            INNER JOIN escuela esc ON es.escuela_id = esc.id
            INNER JOIN barrio b ON es.barrio_id = b.id
            WHERE es.id = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, id)
        return cursor.fetchone()

    @classmethod
    def remove_estudiante_de_taller(cls, id):
        sql = """
            DELETE 
            FROM estudiante_taller 
            WHERE estudiante_id=%s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, id)
        return True

    @classmethod
    def get_listado(cls, nombre):
        filtros = ''
        if (nombre != None):
            filtros = filtros + " AND nombre like '%"+ nombre +"%'"
        sql = 'SELECT * FROM `estudiante` WHERE 1=1 '+filtros+' ORDER BY nombre'
        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()

    @classmethod
    def asociado_A_Taller(cls, id):
        sql = """
            SELECT * FROM `estudiante` e
            INNER JOIN estudiante_taller et on e.id = et.estudiante_id
            WHERE e.id=%s
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, id)

        return cursor.fetchall()

    @classmethod
    def entaller_no_rep(cls, Tid):
        sql = """
            SELECT *
            FROM `estudiante` e
            WHERE not exists(
                SELECT *
                FROM estudiante_taller et
                WHERE et.estudiante_id = e.id AND et.taller_id=%s
            )
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, Tid)

        return cursor.fetchall()

    @classmethod
    def delete_responsable_estudiante(cls, id):
        sql = """
            DELETE
            FROM responsable_estudiante
            WHERE estudiante_id=%s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, id)
        #cursor.connection.commit()
        return True

    @classmethod
    def estudiantes_by_taller(cls, idTaller):
        sql = """
            SELECT * FROM estudiante e
            INNER JOIN estudiante_taller et ON e.id = et.estudiante_id
            WHERE et.taller_id=%s order by e.apellido
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, idTaller)
        return cursor.fetchall()