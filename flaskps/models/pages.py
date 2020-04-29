class Pages(object):

    db = None

    @classmethod
    def all(cls):
        sql = 'SELECT * FROM configuracion_sistema'
        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()

    @classmethod
    def updateIndex(cls, vista, titulo, cuerpo, id):
        sql = """
            UPDATE configuracion_sistema
            SET vista = %s, titulo = %s, cuerpo = %s
            WHERE id = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (vista, titulo, cuerpo, id))
        cls.db.commit()

        return True

    @classmethod
    def getByVista(cls, vista):
        sql = 'SELECT * FROM configuracion_sistema WHERE vista=%s'

        cursor = cls.db.cursor()
        cursor.execute(sql, vista)

        return cursor.fetchall()
    
    @classmethod
    def getEstado(cls):
        sql = """ 
            SELECT cuerpo 
            FROM configuracion_sistema
            WHERE titulo='Estado'
            """
        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchone()

    @classmethod
    def updateEstado(cls, valor):
        sql = """
            UPDATE configuracion_sistema
            SET Estado=%s
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, valor)
        cursor.connection.commit()
        
        return True

    @classmethod
    def get_paginado(cls):
        sql = """
            SELECT cuerpo
            FROM configuracion_sistema
            WHERE titulo = 'Paginado' AND vista = 'sistema'              
        """

        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchone()

    @classmethod
    def getNucleos(cls):
        sql = """
            SELECT * 
            FROM nucleo
        """

        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()

