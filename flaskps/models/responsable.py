class Responsable(object):

    db = None
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM responsable
            WHERE id = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (id))
        return cursor.fetchone()

    @classmethod
    def all(cls):
        sql = 'SELECT * FROM responsable'
        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()

    @classmethod
    def find_by_id_estudiante(cls, idEstudiante):
        sql = """   SELECT r.* FROM responsable r 
                    INNER JOIN responsable_estudiante re 
                    ON r.id = re.responsable_id 
                    WHERE re.estudiante_id = %s """
        cursor = cls.db.cursor()
        cursor.execute(sql, (idEstudiante))
        return cursor.fetchall()