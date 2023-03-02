#se quiere que la pagina sea invocada
from flask import Flask, render_template
from flask import request
from flask import make_response
from flask import flash
from flask_wtf import CSRFProtect

import forms
app=Flask(__name__)

app.config['SECRET_KEY'] = 'esta es tu clave encriptada'
csrf = CSRFProtect()

@app.route("/calcular", methods=['GET'])
def calcular():
    return render_template("calcular.html")

@app.route("/cookie", methods = ['GET', 'POST'])
def cookie():
    reg_user = forms.LoginForm(request.form)
    response = make_response(render_template('cookie.html', form = reg_user))
    if request.method == 'POST' and reg_user.validate():
        user = reg_user.username.data
        pasw = reg_user.password.data
        datos = user + "@" + pasw
        succes_message = 'Bienvenido {}'.format(user)
        response.set_cookie('datos_user', datos)
        flash(succes_message)
    return response


@app.route('/Alumnos', methods=['GET', 'POST'])
def alumnos():
    reg_alum = forms.UserForm(request.form)
    mat = ''
    nom = ''
    if request.method == 'POST' and reg_alum.validate():
        mat = reg_alum.matricula.data
        nom = reg_alum.nombre.data
    return render_template('Alumnos.html', form = reg_alum, mat = mat, nom = nom)


@app.route('/Traductor', methods=['GET', 'POST'])
def diccionario():
    reg_language = forms.IdiomasForm(request.form)
    esp = ""
    eng = ""
    opc = ""
    bus = ""
    palabra = ""
    idioma = ""
    if request.method == 'POST':
        esp = reg_language.esp.data
        eng = reg_language.eng.data
        opc = reg_language.opc.data
        bus = reg_language.bus.data
        if esp != None and eng != None:
            add_dictionary(eng, esp)
        if opc != None and bus != None:
            palabra = search_dictionary(opc, bus)
            if opc == "eng":
                idioma = "English"
            else:
                idioma = "Español"
    return render_template('traductorh.html',form = reg_language, palabra = palabra, idioma = idioma)


@app.route('/Resistencias', methods=['GET', 'POST'])
def diccionario():
    reg_language = forms.Resistencias(request.form)
    esp = ""
    eng = ""
    opc = ""
    bus = ""
    palabra = ""
    idioma = ""
    if request.method == 'POST':
        esp = reg_language.esp.data
        eng = reg_language.eng.data
        opc = reg_language.opc.data
        bus = reg_language.bus.data
        if esp != None and eng != None:
            add_dictionary(eng, esp)
        if opc != None and bus != None:
            palabra = search_dictionary(opc, bus)
            if opc == "eng":
                idioma = "English"
            else:
                idioma = "Español"
    return render_template('traductorh.html',form = reg_language, palabra = palabra, idioma = idioma)











def add_dictionary(eng, esp):
    file = open('traduccion.txt','a')
    file.write(eng.lower())
    file.write("\n")
    file.write(esp.lower())
    file.write("\n")
    file.close()

def search_dictionary(opc, bus):
    file = open('traduccion.txt','r')
    resultado = file.read()
    datos = resultado.lower().split() # convertir todo a minúsculas
    i = 0
    palabra = ""
    
    if opc == "eng":
        for x in datos:
            if x == bus.lower(): # comparar en minúsculas
                palabra = datos[i-1] 
                if i%2 == 0:
                    palabra = "Term in English"
            if palabra == "":
                palabra = "Word not found"
            i += 1
    else:
        for x in datos:
            if x == bus.lower(): # comparar en minúsculas
                palabra = datos[i+1]
                if i%2 != 0:
                    palabra = ""
            if palabra == "":
                palabra = "Palabra no encontrada"
            i += 1
            
    return palabra

                


if __name__ == "__main__":
    
    app.run(debug=True,port=3000)
