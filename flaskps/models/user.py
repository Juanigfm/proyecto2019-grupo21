class User(object):

    db = None

    @classmethod
    def all(cls):
        sql = 'SELECT * FROM usuario ORDER BY first_name'
        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()

    @classmethod
    def get_listado(cls, id, activo, nombre):
        filtros = ''
        if (activo != None):
            filtros = filtros + ' AND usuario.activo ='+ activo
        if (nombre != None):
            filtros = filtros + " AND username like '%"+ nombre +"%'"
        sql = 'SELECT * FROM usuario WHERE usuario.id != '+ str(id) +' '+ filtros +' ORDER BY first_name'
        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()

    @classmethod
    def create(cls, email, username, password, firstName, lastName):
        sql = """
            INSERT INTO usuario (email, username, password, activo, created_at, first_name, last_name)
            VALUES (%s, %s, %s, 1, now(), %s, %s);
        """

        sqlid = "SELECT LAST_INSERT_ID() as idInsertado"

        cursor = cls.db.cursor()
        cursor.execute(sql, (email, username, password, firstName, lastName))
        # cls.db.commit()
        cursor.execute(sqlid)
        return cursor.fetchone()

    @classmethod
    def update(cls, email, username, password, firstName, lastName, idUsuario):
        sql = """
            UPDATE usuario
            SET email = %s, username = %s, updated_at = now(),password = %s, first_name = %s, last_name = %s
            WHERE id=%s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (email, username, password, firstName, lastName, idUsuario) )
        # cls.db.commit()
        
        return True

    @classmethod
    def delete(cls, idUsuario):
        sql = """
            DELETE
            FROM usuario
            WHERE id=%s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, idUsuario)
        # cursor.connection.commit()
        return True

    @classmethod
    def remove_roles_de_usuario(cls, idUsuario):
        sql = """
            DELETE
            FROM usuario_tiene_rol
            WHERE usuario_id=%s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, idUsuario)
        # cursor.connection.commit()

        return True

    @classmethod
    def updateState(cls, state, id):
        sql = """
            UPDATE usuario
            SET activo = %s
            WHERE id = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (state, id))
        cls.db.commit()

        return True

    @classmethod
    def find_by_username(cls, username):
        sql = """
            SELECT * FROM usuario
            WHERE username = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (username))
        return cursor.fetchone()

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM usuario
            WHERE id = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (id))
        return cursor.fetchone()

    @classmethod
    def find_by_email(cls, email):
        sql = """
            SELECT * FROM usuario AS u
            WHERE u.email = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (email))
        return cursor.fetchone()

    @classmethod
    def find_by_username_or_email_and_pass(cls, usuario, email, password):
        sql = """
            SELECT * FROM usuario as usu
            WHERE (usu.email = %s OR usu.username = %s) AND usu.password = %s
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, (usuario, email, password))

        return cursor.fetchone()

    @classmethod
    def get_user_by_email(cls, email):
        sql = """
            SELECT * FROM usuario
            WHERE email=%s
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, email)

        return cursor.fetchone()

    
    @classmethod
    def deactivate(cls, idUsuario):
        sql = """
            UPDATE usuario
            SET activo=0
            WHERE id=%s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql,idUsuario)

        return cursor.commit()

    @classmethod
    def activate(cls, idUsuario):
        sql = """
            UPDATE usuario
            SET activo=1
            WHERE id=%s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql,idUsuario)

        return cursor.commit()

    @classmethod
    def add_role(cls, idUsuario, idRol):
        sql = """
            INSERT INTO usuario_tiene_rol (usuario_id, rol_id)
            VALUES (%s, %s)
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (idUsuario,idRol))
        # cls.db.commit()
        return True

    @classmethod
    def remove_role(cls, idUsuario, idRol):
        sql = """
            DELETE
            FROM usuario_tiene_rol
            WHERE usuario_id=%s AND rol_id=%s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, idUsuario, idRol)
        cls.db.commit()
        return True

    @classmethod
    def buscar(cls, estado, username, email, nombre, apellido):
        sql = "SELECT * FROM usuario WHERE activo = %s"
        if username:
            sql + " AND username LIKE %s"
        if email:
            sql + " AND email LIKE %s"
        if nombre:
            sql + " AND first_name LIKE %s"
        if apellido:
            sql + " AND last_name LIKE %s"

        cursor  =  cls.db.cursor()
        cursor.execute(sql, (estado, username, email, nombre, apellido))
        return cursor.fetchall()

    @classmethod
    def update_password(cls, password, idUsuario):
        sql = """
            UPDATE usuario 
            SET updated_at = now(),password = %s
            WHERE id=%s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (password, idUsuario) )
        cls.db.commit()
    
        return True

    @classmethod
    def update_profile(cls, email, username, firstName, lastName, idUsuario):
        sql = """
            UPDATE usuario
            SET email = %s, username = %s, updated_at = now(), first_name = %s, last_name = %s
            WHERE id=%s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (email, username, firstName, lastName, idUsuario) )
        cls.db.commit()
        
        return True