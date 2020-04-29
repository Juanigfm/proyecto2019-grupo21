class Nivel(object):

    db = None
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM nivel
            WHERE id = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (id))
        return cursor.fetchone()

    @classmethod
    def all(cls):
        sql = 'SELECT * FROM nivel'
        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()