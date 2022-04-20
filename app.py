from flask import Flask, render_template,abort
import os
import json
with open ("books.json") as fichero:
    datos=json.load(fichero)
app = Flask(__name__)

@app.route('/')
def inicio():
    libros=[]
    for var in datos:
        dic={"titulo":var.get("title"),"isbn":var.get("isbn")}
        libros.append(dic)
    return render_template("index.html",libros=libros)

@app.route('/libro/<num1>')
def cont(num1):
    cont=0
    for var in datos:
        if var.get("isbn") == num1:
            titulo=var.get("title")
            imagen=var.get("thumbnailUrl")
            autores=var.get("authors")
            descripcion=var.get("longDescription")
            categorias=var.get("categories")
            status=var.get("status")
            numpag=var.get("pageCount")
            cont=1
    if cont==0:
        abort(404)
    return render_template("libro.html",titulo=titulo,imagen=imagen,autores=autores,descripcion=descripcion,categorias=categorias,status=status,numpag=numpag)

@app.route('/categoria/<cat>')
def categoria(cat):
    libros=[]
    for var in datos:
        for var2 in var.get("categories"):
            if var2 == cat:
                dic={"titulo":var.get("title"),"isbn":var.get("isbn")}
                libros.append(dic)
    return render_template("librocategoria.html",libros=libros,cat=cat)



app.run('0.0.0.0',debug=True)
    