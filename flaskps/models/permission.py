class Permission(object):

    db = None

    @classmethod
    def all(cls):
        sql = 'SELECT * FROM permiso'
        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()

    @classmethod
    def seacr_by_name(cls,name):
        sql = "SELECT * FROM permiso WHERE nombre LIKE '%:name1%'"
        cursor = cls.db.cursor()
        cursor.execute(sql,{'name1' : name})

        return cursor.fetchall()

    @classmethod
    def all_by_rol(cls, rolId):
        sql = """SELECT p.* FROM permiso as p INNER JOIN rol_tiene_permiso AS rtp 
                ON p.id = rtp.permiso_id WHERE rtp.rol_id = %s"""
        cursor = cls.db.cursor()
        cursor.execute(sql, (rolId))

        return cursor.fetchall()