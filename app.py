from flask import * 
from flask import render_template
from flask import Flask,request,url_for,redirect,session,flash
from datetime import datetime

app=Flask (__name__)
app.config.from_pyfile('config.py')
from clases import Preceptor,Padre,Estudiante,Curso,Asistencia,db

@app.route('/')
def inicio():
    return render_template('home.html')
@app.route('/alta',methods=['POST'])
def alta():
    email=request.form['email']
    clave=request.form['clave']
    usuario=Preceptor.query.filter_by(correo=email,clave=clave).first() #recorre la clase preceptor y toma el primero que cumpla estas condiciones
    
    if usuario!=None:
        session["id"]=usuario.id
        return render_template('preceptor.html')
    return render_template('home.html',mensaje='Usuario incorrecto')

@app.route('/VerAlumnos',methods=['POST','GET'])
def VerAlumnos():
    cursos=Curso.query.filter(Curso.idpreceptor==session["id"]).all()
    return render_template('seleccionarcurso.html',cursos=cursos)

@app.route('/infoAsistencia',methods=['POST','GET'])
def informes():
    return("Ingreso a informes")
@app.route('/cursoseleccionado',methods=['POST','GET'])
def cursoseleccionado():
    estudiantes=Estudiante.query.filter(Estudiante.idCurso==request.form.get("curso")).all()
    return render_template('cursoseleccionado.html',estudiantes=estudiantes)
@app.route('/registrarAsistencia',methods=['POST','GET'])
def registrarAsistencia():
    idcurso = request.form.get('idcurso')
    alumnos=Estudiante.query.filter(Estudiante.idCurso==idcurso).all()
    return render_template('alumnosAsistencia.html', alumnos=alumnos)

    
@app.route('/marcarAsistencia', methods=['POST','GET'])
def marcarAsistencia():
    cursos=Curso.query.all()
    correo_preceptor = session.get("preceptor")
    preceptor = Preceptor.query.filter_by(correo=correo_preceptor).first()
    return redirect(url_for('registrar_asistencia', cursos=cursos,preceptor=preceptor))
@app.route('/confirmarAsistencia',methods=['POST','GET'])
def confirmarAsistencia():
    asistencia = Asistencia(fecha=request.form['fecha'], codigoclase=request.form['tipoclase'], asistio=request.form['asis'], justificacion=request.form['justificacion'], idestudiante=request.form.get('idalumno'))
    db.session.add(asistencia)
    db.session.commit()
    return redirect()
      

# from flask import * 
# from flask import render_template
# from flask import Flask,request,url_for,redirect,session,flash
# from datetime import datetime

# app=Flask (__name__)
# app.config.from_pyfile('config.py')
# from clases import Preceptor,Padre,Estudiante,Curso,Asistencia,db

# @app.route('/')
# def inicio():
#     return render_template('home.html')
# @app.route('/alta',methods=['POST'])
# def alta():
#     email=request.form['email']
#     clave=request.form['clave']
#     usuario=Preceptor.query.filter_by(correo=email,clave=clave).first() #recorre la clase preceptor y toma el primero que cumpla estas condiciones
    
#     if usuario!=None:
#         session["id"]=usuario.id
#         return render_template('preceptor.html')
#     return render_template('home.html',mensaje='Usuario incorrecto')

# @app.route('/VerAlumnos',methods=['POST','GET'])
# def VerAlumnos():
#     cursos=Curso.query.filter(Curso.idpreceptor==session["id"]).all()
#     return render_template('seleccionarcurso.html',cursos=cursos)

# @app.route('/infoAsistencia',methods=['POST','GET'])
# def informes():
#     return("Ingreso a informes")
# @app.route('/cursoseleccionado',methods=['POST','GET'])
# def cursoseleccionado():
#     estudiantes=Estudiante.query.filter(Estudiante.idCurso==request.form.get("curso")).all()
#     return render_template('cursoseleccionado.html',estudiantes=estudiantes)
# @app.route('/registrarAsistencia',methods=['POST','GET'])
# def registrarAsistencia():
#     idcurso = request.args.get('idcurso')
#     asistencia = Asistencia(fecha=request.form['fecha'], codigoclase=request.form['tipoclase'], asistio=request.form['asis'], justificacion=request.form['justificacion'], idestudiante=request.form.get('idalumno'))
#     db.session.add(asistencia)
#     db.session.commit()
#     cursos=Curso.query.all()
#     correo_preceptor = session.get("preceptor")
#     preceptor = Preceptor.query.filter_by(correo=correo_preceptor).first()
#     return redirect(url_for('registrar_asistencia', cursos=cursos,preceptor=preceptor))
    
    
        
        
        
       

if __name__=='__main__':
    app.run()
