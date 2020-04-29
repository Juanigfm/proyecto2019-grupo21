class Barrio(object):

    db = None
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM barrio
            WHERE id = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (id))
        return cursor.fetchone()

    @classmethod
    def all(cls):
        sql = 'SELECT * FROM barrio'
        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()