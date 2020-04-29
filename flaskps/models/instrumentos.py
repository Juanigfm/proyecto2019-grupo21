class Instrumento(object):

    db = None

    @classmethod
    def get_listado(cls, nombre):
        filtros = ''
        if (nombre != None):
            filtros = filtros + " AND ins.nombre like '%"+ nombre +"%'"
        sql = """
            SELECT ins.*, t.nombre as nomTipo
            FROM instrumento ins INNER JOIN tipo_instrumento t ON ins.tipo_id = t.id
            WHERE 1=1 """+filtros+""" ORDER BY nombre
            """
        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT ins.*, t.nombre as nomTipo
            FROM instrumento ins
            INNER JOIN tipo_instrumento t ON ins.tipo_id = t.id
            WHERE ins.id = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, id)
        return cursor.fetchone()

    @classmethod
    def buscar_codigo(cls, codigo):
        sql = """
            SELECT ins.*, t.nombre as nomTipo
            FROM instrumento ins
            INNER JOIN tipo_instrumento t ON ins.tipo_id = t.id
            WHERE ins.codigo = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, codigo)
        return cursor.fetchone()

    @classmethod
    def create(cls, nombre, tipo_id, codigo, imagen):
        sql = """
            INSERT INTO instrumento (nombre,
                                    tipo_id,
                                    codigo,
                                    imagen)
            VALUES (%s, %s, %s, %s);
        """

        sqlid = "SELECT LAST_INSERT_ID() as idInsertado"

        cursor = cls.db.cursor()
        cursor.execute(sql, (nombre, tipo_id, codigo, imagen))
        cursor.execute(sqlid)
        return cursor.fetchone()

    @classmethod
    def update(cls, nombre, tipo_id, codigo, imagen, id):
        sql = """
            UPDATE instrumento
            SET nombre = %s,
                tipo_id = %s,
                codigo = %s,
                imagen = %s
            WHERE id = %s
            ;
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (nombre, tipo_id, codigo, imagen, id))
        cls.db.commit()
        return True

    @classmethod
    def updateNoImg(cls, nombre, tipo_id, codigo, id):
        sql = """
            UPDATE instrumento
            SET nombre = %s,
                tipo_id = %s,
                codigo = %s
            WHERE id = %s
            ;
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (nombre, tipo_id, codigo, id))
        cls.db.commit()
        return True

    @classmethod
    def delete(cls, id):
        sql = """
            DELETE
            FROM instrumento
            WHERE id=%s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, id)
        cursor.connection.commit()
        return True
