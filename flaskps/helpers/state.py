from flaskps.db import get_db
from flaskps.models.pages import Pages

def pageState():
    Pages.db = get_db()
    estado = Pages.getEstado()
    return int(estado['cuerpo'])