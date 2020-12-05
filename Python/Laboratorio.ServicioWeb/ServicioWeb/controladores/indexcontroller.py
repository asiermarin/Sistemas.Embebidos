from servicios.weblogging import Applogging
from flask import render_template, request
from flask import request, redirect
from comun.singleton import Singleton

"""  
# from main import app
from flask_classful import FlaskView, route

# app_modelue = app

class Indexcontroller(FlaskView):
# class Indexcontroller:

    #def __init__(self, autenticacion):
    def __init__(self):
        self.__controlador_log = Applogging("Controlador Index")
        # self.__autenticacion = autenticacion
        self.__TEMPLATE_INDEX_CONSTANTE = 'index.html'
        self.__TEMPLATE_TEMPERATURA = None

    @route("/index", methods=["GET"])
    def get(self):
        return render_template(self.__TEMPLATE_INDEX_CONSTANTE)

    @route("/index", methods=["POST"])
    def post(self):
        informacion_request = request.form
        usuario_form = request.get("username")
        contrasenia_form = request.get("password")

        campos_vacios = self.__algun_campo_vacio()
        if (campos_vacios):
            self.__controlador_log.info_log("Se han encontrado campos vacios")
            feedback = f"Campos vacios en {', '.join(campos_vacios)}"
            return render_template(self.__TEMPLATE_INDEX_CONSTANTE, feedback=feedback)
        else:
            autenticacion_aceptada = self.__autenticacion.comprobar_autenticacion(usuario_form, contrasenia_form)
            if (autenticacion_aceptada):
                return render_template(self.__TEMPLATE_INDEX_CONSTANTE, feedback=feedback)

    def __algun_campo_vacio(self, request):
        campos_requeridos = list()
        for k, v in request.items():
            if v == "":
                campos_requeridos.append(k)
        return campos_requeridos
"""
