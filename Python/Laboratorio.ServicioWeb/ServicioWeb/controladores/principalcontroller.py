from flask import render_template, request
from flask import request, redirect
from flask.views import MethodView   
from modelos.usuario import Usuario
from static.constantes import TEMPLATE_INDEX_CONSTANTE, TEMPLATE_PRINCIPAL_CONSTANTE

class Principalcontroller(MethodView):

    def __init__(self, autenticacion , rpi, principal_controller_log):
        self.__servicio_autenticacion = autenticacion
        self.__principal_log = principal_controller_log
        self.__rpi = rpi

    def get(self):
        if (self.__servicio_autenticacion.usuario_autenticado == True):
            return render_template(TEMPLATE_PRINCIPAL_CONSTANTE)
        else:
            return render_template(TEMPLATE_INDEX_CONSTANTE)
