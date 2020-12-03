from servicios.weblogging import Applogging
from flask import render_template, request
from flask import request, redirect


# from flask_classful import FlaskView
app_modelue = None
# class Indexcontroller(FlaskView):
class Indexcontroller:

    def __init__(self, autenticacion, app):
        self.__app = app
        app_module = self.__app
        self.__controlador_log = Applogging("Controlador Index")
        self.__autenticacion = autenticacion
        self.__TEMPLATE_INDEX_CONSTANTE = 'index.html'
        self.__TEMPLATE_TEMPERATURA = None

    @app_modelue.route("/", methods=["GET"])
    def get_index(self):
        return render_template(self.__TEMPLATE_INDEX_CONSTANTE)

    @app_modelue.route("/", methods=["POST"])
    def post_index(self):
        informacion_request = request.form
        usuario_form = req.get("username")
        # email_form = req.get("email")
        contrasenia_form = req.get("password")

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

