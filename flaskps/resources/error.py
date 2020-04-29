from flask import redirect, render_template, request, url_for, flash
from flaskps.db import get_db
from flaskps.resources import pages
# from flaskps.models.issue import Issue

def notfound():
    return render_template('error/404.html')

def mantenimiento():
    return render_template('error/mantenimiento.html')

def handle_bad_request(e):
    flash("Acceda apropiadamente funcionalidad.","danger")
    return pages.home()