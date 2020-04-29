class Roles(object):

    db = None

    @classmethod
    def all(cls):
        sql = 'SELECT * FROM rol'
        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()

    @classmethod
    def search_by_name(cls,name):
        sql = "SELECT * FROM rol WHERE nombre LIKE '%:name1%'"
        cursor = cls.db.cursor()
        cursor.execute(sql,{'name1' : name})

        return cursor.fetchall()

    @classmethod
    def get_roles(cls, idUsuario):
        sql = """
            SELECT rol.id, rol.nombre
            FROM usuario_tiene_rol INNER JOIN rol ON usuario_tiene_rol.rol_id=rol.id
            WHERE usuario_tiene_rol.usuario_id=%s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, idUsuario)

        return cursor.fetchall()
