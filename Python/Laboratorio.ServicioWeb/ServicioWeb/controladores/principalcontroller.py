from flask import render_template, request
from flask import request, redirect
from flask.views import MethodView   
from modelos.usuario import Usuario
from static.constantes import TEMPLATE_INDEX_CONSTANTE, TEMPLATE_REGISTRO_CONSTANTE

class Principalcontroller(MethodView):

    def __init__(self, rpi, principal_controller_log):
        self.__principal_log = principal_controller_log
        self.rpi = rpi

    def get(self):
        return render_template(TEMPLATE_REGISTRO_CONSTANTE)