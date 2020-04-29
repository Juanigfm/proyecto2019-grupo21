class Ciclo(object):

    db = None

    @classmethod
    def all(cls):
        sql = """
                SELECT *
                FROM ciclo_lectivo
                """
        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()
    
    @classmethod
    def create(cls, fecha_ini , fecha_fin , semestre):
        sql = """
                INSERT INTO ciclo_lectivo (fecha_ini, fecha_fin, semestre)
                VALUES (%s,%s,%s);
                """
        cursor = cls.db.cursor()
        cursor.execute(sql, (fecha_ini, fecha_fin, semestre))
        cls.db.commit()
        return cursor.fetchone()
    
    @classmethod
    def get_talleres(cls, id):
        sql = """
                SELECT t.nombre as nombre, t.nombre_corto as nombre_corto, t.id as id
                FROM ciclo_lectivo cl
                INNER JOIN ciclo_lectivo_taller clt ON cl.id = clt.ciclo_lectivo_id
                INNER JOIN taller t ON clt.taller_id = t.id
                WHERE cl.id = %s
                """
        cursor = cls.db.cursor()
        cursor.execute(sql, id)

        return cursor.fetchall()

    @classmethod
    def find_by_id(cls, id):
        sql = """
                SELECT *
                FROM ciclo_lectivo 
                WHERE id = %s
                """
        cursor = cls.db.cursor()
        cursor.execute(sql, id)

        return cursor.fetchone()

    @classmethod
    def update(cls, fi,fn,sem,id):
        sql = """
            UPDATE ciclo_lectivo
            SET fecha_ini=%s, fecha_fin=%s, semestre=%s
            WHERE id=%s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (fi, fn, sem, id) )
        cls.db.commit()
        
        return True

    @classmethod
    def delete(cls, id):
        sql = """
                DELETE
                FROM ciclo_lectivo
                WHERE ciclo_lectivo.id = %s
                """
        cursor = cls.db.cursor()
        cursor.execute(sql, id)
        # cls.db.commit()
        
        return True
    
    @classmethod
    def delete_clt(cls, id):
        sql = """
                DELETE 
                FROM ciclo_lectivo_taller 
                WHERE ciclo_lectivo_id=%s
                """
        cursor = cls.db.cursor()
        cursor.execute(sql, id)
        # cls.db.commit()
        
        return True
    
    @classmethod
    def assign_taller(cls, clid, taller_id):
        sql = """
                INSERT INTO ciclo_lectivo_taller (ciclo_lectivo_id, taller_id)
                VALUES (%s,%s);
                """

        cursor = cls.db.cursor()
        cursor.execute(sql, (clid,taller_id))
        cls.db.commit()
        
        return True
    
    # @classmethod
    # def ciclo_vacio(cls,clid):
    #     sql = """
    #             SELECT *
    #             FROM ciclo_lectivo cl
    #             INNER JOIN ciclo_lectivo_taller clt ON clt.ciclo_lectivo_id = cl.id
    #             INNER JOIN estudiante_taller et ON et.ciclo_lectivo_id = cl.id
    #             INNER JOIN docente_taller dt ON dt.ciclo_lectivo_id = cl.id
    #             WHERE cl.id = %s
    #             """
    #     cursor = cls.db.cursor()
    #     cursor.execute(sql, clid)
    #     cls.db.commit()

    #     return cursor.fetchall()

    @classmethod
    def get_talleres_sin_repeticion(cls, id):
        sql = """
                SELECT * 
                FROM taller t
                WHERE NOT EXISTS(
                    SELECT t.*
                    FROM ciclo_lectivo_taller clt 
                    WHERE clt.taller_id = t.id AND clt.ciclo_lectivo_id = %s ) 
                """
        cursor = cls.db.cursor()
        cursor.execute(sql, id)

        return cursor.fetchall()

