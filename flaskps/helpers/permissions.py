from flask import session

def usuarioTienePermiso(nombrePermiso):
        ok = False
        for p in session['permisos']:
            if p['nombre'] == nombrePermiso:
                ok = True
                break
        return ok