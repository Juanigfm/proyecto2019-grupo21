class Taller(object):

    db = None

    @classmethod
    def all(cls):
        sql = 'SELECT * FROM taller'
        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()

    @classmethod
    def listado(cls, nombre):
        filtros = ''
        if (nombre != None):
            filtros = filtros + " AND (nombre like '%"+ nombre +"%' OR nombre_corto like '%"+ nombre +"%')"
        sql = ' SELECT *, cl.id as clid FROM taller t INNER JOIN ciclo_lectivo_taller clt ON t.id=clt.taller_id INNER JOIN ciclo_lectivo cl ON clt.ciclo_lectivo_id=cl.id WHERE 1=1 '+filtros+' ORDER BY nombre'
        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()

    @classmethod
    def delete(cls, id):
        sql = """
                DELETE
                FROM taller
                WHERE taller.id = %s
                """
        cursor = cls.db.cursor()
        cursor.execute(sql, id)
        # cls.db.commit()
        return True
    
    @classmethod
    def get_detalle_taller(cls,id):
        sql = """
                SELECT t.id as id, t.nombre as nombreT, cl.semestre as semestre, cl.fecha_ini as ini, cl.fecha_fin as fin
                FROM taller t
                INNER JOIN ciclo_lectivo_taller clt ON t.id = clt.taller_id  
                INNER JOIN ciclo_lectivo cl ON cl.id = clt.ciclo_lectivo_id
                WHERE t.id=%s                
                """
        cursor = cls.db.cursor()
        cursor.execute(sql, (id))

        return cursor.fetchone()

    @classmethod
    def get_alumnos_taller(cls,id):
        sql = """
                SELECT e.nombre as nombre, e.apellido as apellido, e.tipo_doc_id as tipo_doc, e.numero as doc_num, e.id as est_id
                FROM taller t
                INNER JOIN estudiante_taller et ON t.id = et.taller_id
                INNER JOIN estudiante e ON et.estudiante_id = e.id
                WHERE t.id=%s 
                """
        cursor = cls.db.cursor()
        cursor.execute(sql,(id))

        return cursor.fetchall()

    @classmethod
    def get_docentes_taller(cls,id):
        sql = """
                SELECT d.nombre as nombre, d.apellido as apellido, d.tipo_doc_id as tipo_doc, d.numero as doc_num, d.id as doc_id
                FROM taller t
                INNER JOIN docente_taller dt ON t.id = dt.taller_id
                INNER JOIN docente d ON dt.docente_id = d.id
                WHERE t.id=%s 
                """
        cursor = cls.db.cursor()
        cursor.execute(sql,(id))

        return cursor.fetchall()
    
    @classmethod
    def create(cls,nombre,nombrecorto,nucleo_id):
        sql = """
                INSERT INTO taller (nombre, nombre_corto, nucleo_id)
                VALUES (%s, %s, %s);
                """

        sqlid = "SELECT LAST_INSERT_ID() as idInsertado"


        cursor = cls.db.cursor()
        cursor.execute(sql, (nombre, nombrecorto, nucleo_id))
        # cls.db.commit() en controlador

        cursor.execute(sqlid)

        return cursor.fetchone()

    @classmethod
    def assign_ciclo(cls,taller,ciclo):
        sql = """
                INSERT INTO ciclo_lectivo_taller (taller_id, ciclo_lectivo_id)
                VALUES (%s, %s);
                """

        cursor = cls.db.cursor()
        cursor.execute(sql, (taller, ciclo))
        #cls.db.commit() en controlador
        return cursor.fetchone()

    @classmethod
    def assign_docente(cls,docente,taller):
        sql = """
                INSERT INTO docente_taller (docente_id, taller_id)
                VALUES (%s, %s);
                """

        cursor = cls.db.cursor()
        cursor.execute(sql, (docente, taller))
        #cls.db.commit() en controlador
        return True

    @classmethod
    def assign_alumno(cls,alumno,taller):
        sql = """
                INSERT INTO estudiante_taller (estudiante_id, taller_id)
                VALUES (%s, %s);
                """

        cursor = cls.db.cursor()
        cursor.execute(sql, (alumno, taller))
        cls.db.commit()
        return True

    @classmethod
    def baja_alumno(cls,alumno,taller):
        sql = """
                DELETE
                FROM estudiante_taller
                WHERE estudiante_id=%s AND taller_id=%s;
                """
        cursor = cls.db.cursor()
        cursor.execute(sql,(alumno,taller))
        cls.db.commit()
        return True

    @classmethod
    def baja_docente(cls,docente,taller):
        sql = """
                DELETE
                FROM docente_taller
                WHERE docente_id = %s AND taller_id=%s
                """
        cursor = cls.db.cursor()
        cursor.execute(sql, (docente,taller))
        cls.db.commit()
        return True

    @classmethod
    def baja_alumnos(cls,taller):
        sql = """
                DELETE
                FROM estudiante_taller
                WHERE taller_id=%s;
                """
        cursor = cls.db.cursor()
        cursor.execute(sql,(taller))
        # cls.db.commit()
        return True

    @classmethod
    def baja_docentes(cls,taller):
        sql = """
                DELETE
                FROM docente_taller
                WHERE taller_id=%s
                """
        cursor = cls.db.cursor()
        cursor.execute(sql, (taller))
        # cls.db.commit()
        return True

    @classmethod
    def get_talleres_con_clases_de_docente(cls, docente_id):
        sql = """
                SELECT t.nombre
                FROM taller t 
                INNER JOIN clase c on t.id = c.taller_id
                WHERE c.activo = 1 and c.docente_id = %s
                GROUP BY nombre
                """
        cursor = cls.db.cursor()
        cursor.execute(sql, (docente_id))
        return cursor.fetchall()