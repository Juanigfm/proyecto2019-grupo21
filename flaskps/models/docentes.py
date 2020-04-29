class Docente(object):

    db = None

    @classmethod
    def all(cls):
        sql = 'SELECT * FROM docente'
        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()

    @classmethod
    def create(cls, apellido, nombre, fecha_nac, localidad_id, domicilio, genero_id, tipo_doc_id, numero, tel):
        sql = """
            INSERT INTO docente (apellido, 
                                    nombre, 
                                    fecha_nac, 
                                    localidad_id, 
                                    domicilio, 
                                    genero_id,
                                    tipo_doc_id, 
                                    numero, 
                                    tel)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
        """

        # sqlid = "SELECT LAST_INSERT_ID() as idInsertado"

        cursor = cls.db.cursor()
        cursor.execute(sql, (apellido, nombre, fecha_nac, localidad_id, domicilio, genero_id, tipo_doc_id, numero, tel))
        cls.db.commit()
        # cursor.execute(sqlid)
        # return cursor.fetchone()
        return True

    @classmethod
    def update(cls, apellido, nombre, fecha_nac, localidad_id, domicilio, genero_id, tipo_doc_id, numero, tel, id):
        sql = """
            UPDATE docente SET  apellido = %s, 
                                nombre = %s, 
                                fecha_nac = %s, 
                                localidad_id = %s, 
                                domicilio = %s, 
                                genero_id = %s, 
                                tipo_doc_id = %s, 
                                numero = %s, 
                                tel = %s
            WHERE id = %s
            ;
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (apellido, nombre, fecha_nac, localidad_id, domicilio, genero_id, tipo_doc_id, numero, tel, id))
        cls.db.commit()
        return True

    @classmethod
    def delete(cls, id):
        sql = """
            DELETE
            FROM docente
            WHERE id=%s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, id)
        #cursor.connection.commit()
        return True
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT d.*, g.nombre as gen_nombre
            FROM docente d 
            INNER JOIN genero g ON d.genero_id = g.id
            WHERE d.id = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (id))
        return cursor.fetchone()

    @classmethod
    def remove_docente_de_taller(cls, id):
        sql= """
            DELETE 
            FROM docente_taller
            WHERE docente_id=%s
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, id)
        #cursor.connection.commit()
        return True

    @classmethod
    def remove_docente_de_alumno(cls, id):
        sql= """
            DELETE
            FROM responsable_estudiante
            WHERE responsable_id=%s
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, id)
        #cursor.connection.commit()
        return True
    
    @classmethod
    def get_listado(cls, nombre):
        filtros = ''
        if (nombre != None):
            filtros = filtros + " AND nombre like '%"+ nombre +"%'"
        sql = 'SELECT * FROM `docente` WHERE 1=1 '+filtros+' ORDER BY nombre'
        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()

    @classmethod
    def asociado_A_Taller(cls, id):
        sql = """
            SELECT * FROM `docente` d
            INNER JOIN docente_taller drt ON d.id = drt.docente_id   
            WHERE d.id = %s
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, id)

        return cursor.fetchall()

    @classmethod
    def entaller_no_rep(cls, Tid):
        sql = """
            SELECT *
            FROM `docente` d
            WHERE not exists(
                SELECT *
                FROM docente_taller drt
                WHERE drt.docente_id = d.id AND drt.taller_id = %s
            )
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, Tid)

        return cursor.fetchall()