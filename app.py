import requests

from flask import Flask, render_template

from flask_pymongo import PyMongo

from flask import jsonify, request

from bs4 import BeautifulSoup

from bson.json_util import dumps

from bson.objectid import ObjectId

from datetime import date

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/Noticias"
# mongo = PyMongo(app)
# id = mongo.db.Noticia.insert({'uri': "http://google.html", 'dado' : "lrijerijeiofjdoidfjogdfjgiodjfgiodfjgoidfjgoidjg", 'date': '01/01/2020'})

def veja():
    url='https://veja.abril.com.br/'
    r = requests.get(url)

    soup = BeautifulSoup(r.text,'lxml')

    tagMain = soup.find_all('main') 

    for lista_div in tagMain:
        lista_div2 = lista_div.find_all('div', class_="row")
        for lista_div3 in lista_div2:
            lista_div4 = lista_div3.find_all('div', class_="row")
            for lista_div5 in lista_div4:
                lista_div6 = lista_div5.find_all('div', class_="row")
                for lista_div7 in lista_div6:
                    elememt = lista_div7.find_all('div', class_="col-s-12 col-l-4")
                    for item in elememt:                        
                        link = item.a.get('href')
                        title = item.a.span.text
                        dado = item.a.h3.text
                        try:
                            img = item.a.img.get('data-src')
                        except:
                            img = 'data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%22286%22%20height%3D%22180%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%20286%20180%22%20preserveAspectRatio%3D%22none%22%3E%3Cdefs%3E%3Cstyle%20type%3D%22text%2Fcss%22%3E%23holder_1720a7699ad%20text%20%7B%20fill%3Argba(255%2C255%2C255%2C.75)%3Bfont-weight%3Anormal%3Bfont-family%3AHelvetica%2C%20monospace%3Bfont-size%3A14pt%20%7D%20%3C%2Fstyle%3E%3C%2Fdefs%3E%3Cg%20id%3D%22holder_1720a7699ad%22%3E%3Crect%20width%3D%22286%22%20height%3D%22180%22%20fill%3D%22%23777%22%3E%3C%2Frect%3E%3Cg%3E%3Ctext%20x%3D%2299.4140625%22%20y%3D%2296.24375%22%3EImage%20cap%3C%2Ftext%3E%3C%2Fg%3E%3C%2Fg%3E%3C%2Fsvg%3E'
                        
                        mongo = PyMongo(app)
                        possui = mongo.db.Noticia.find_one({'title': title, 'uri': link, 'dado': dado, 'tipoSite': 'veja'})               

                        if possui == None:
                            mongo.db.Noticia.insert({'uri': link, 'dado': dado, 'date': date.today().strftime("%d/%m/%Y"), 'title': title, 'img': img, 'tipoSite': 'veja'})
                        
def uol():
    url='https://www.uol.com.br/'
    r = requests.get(url)

    soup = BeautifulSoup(r.text,'lxml')

    divHibrido = soup.find_all('div', class_="topo-hibrido-hardnews-col1")

    for lista_subManchete in divHibrido:
        listasubmancheteCols = lista_subManchete.find_all('div', class_="mod-hibrido-submanchete")
        for listasubmancheteCol in listasubmancheteCols:
            submanchetes = listasubmancheteCol.find_all('div', class_="submanchete-col")
            for submanchete in submanchetes:
                divs = submanchete.find_all('div', class_="submanchete")
                for div in divs:                    
                    link = div.a.get('href')
                    title = div.a.strong.text
                    dado = div.a.h2.text
                    try:
                        img = div.a.figure.img.get('data-src')
                    except:
                        img = 'data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%22286%22%20height%3D%22180%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%20286%20180%22%20preserveAspectRatio%3D%22none%22%3E%3Cdefs%3E%3Cstyle%20type%3D%22text%2Fcss%22%3E%23holder_1720a7699ad%20text%20%7B%20fill%3Argba(255%2C255%2C255%2C.75)%3Bfont-weight%3Anormal%3Bfont-family%3AHelvetica%2C%20monospace%3Bfont-size%3A14pt%20%7D%20%3C%2Fstyle%3E%3C%2Fdefs%3E%3Cg%20id%3D%22holder_1720a7699ad%22%3E%3Crect%20width%3D%22286%22%20height%3D%22180%22%20fill%3D%22%23777%22%3E%3C%2Frect%3E%3Cg%3E%3Ctext%20x%3D%2299.4140625%22%20y%3D%2296.24375%22%3EImage%20cap%3C%2Ftext%3E%3C%2Fg%3E%3C%2Fg%3E%3C%2Fsvg%3E'

                    mongo = PyMongo(app)
                    possui = mongo.db.Noticia.find_one({'title': title, 'uri': link, 'dado': dado, 'tipoSite': 'uol'})               

                    if possui == None:
                        mongo.db.Noticia.insert({'uri': link, 'dado': dado, 'date': date.today().strftime("%d/%m/%Y"), 'title': title, 'img': img, 'tipoSite': 'uol'})

def olharDigital():
    url='https://olhardigital.com.br/'
    r = requests.get(url)

    soup = BeautifulSoup(r.text,'lxml')

    items = soup.find_all('div', class_="blk-items")
    for item in items:
        a = item.find_all('a')
        for noticia in a:
            link = noticia.get('href')
            
            divImg = noticia.find_all('div', class_="ite-img")

            try:
                img = divImg[0].img.get('src')
            except:
                img = 'data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%22286%22%20height%3D%22180%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%20286%20180%22%20preserveAspectRatio%3D%22none%22%3E%3Cdefs%3E%3Cstyle%20type%3D%22text%2Fcss%22%3E%23holder_1720a7699ad%20text%20%7B%20fill%3Argba(255%2C255%2C255%2C.75)%3Bfont-weight%3Anormal%3Bfont-family%3AHelvetica%2C%20monospace%3Bfont-size%3A14pt%20%7D%20%3C%2Fstyle%3E%3C%2Fdefs%3E%3Cg%20id%3D%22holder_1720a7699ad%22%3E%3Crect%20width%3D%22286%22%20height%3D%22180%22%20fill%3D%22%23777%22%3E%3C%2Frect%3E%3Cg%3E%3Ctext%20x%3D%2299.4140625%22%20y%3D%2296.24375%22%3EImage%20cap%3C%2Ftext%3E%3C%2Fg%3E%3C%2Fg%3E%3C%2Fsvg%3E'

            divText = noticia.find_all('div', class_="ite-meta")
            dado = divText[0].h3.text            
            title = divText[0].h3.text[0:15]

            mongo = PyMongo(app)
            possui = mongo.db.Noticia.find_one({'title': title, 'uri': link, 'dado': dado, 'tipoSite': 'olharDigital'})               

            if possui == None:
                mongo.db.Noticia.insert({'uri': link, 'dado': dado, 'date': date.today().strftime("%d/%m/%Y"), 'title': title, 'img': img, 'tipoSite': 'olharDigital'})



@app.route('/')
def index():
    veja()
    uol()
    olharDigital()
    texto = ['<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">\n']    
    mongo = PyMongo(app)
    
    texto.append('<div class="navbar navbar-expand navbar-dark flex-column flex-md-row bd-navbar" style="background-color: #563d7c">')
    
    texto.append('<ul class="nav nav-pills">')
    texto.append('<li class="nav-item">')
    texto.append('<a class="nav-link active" href="/">Todas</a>')
    texto.append('</li>')
    texto.append('<li class="nav-item">')
    texto.append('<a class="nav-link" href="/uol" style="color: #FFFFFF">Uol</a>')
    texto.append('</li>')

    texto.append('<li class="nav-item">')
    texto.append('<a class="nav-link" href="/veja" style="color: #FFFFFF">Veja</a>')
    texto.append('</li>')

    texto.append('<li class="nav-item">')
    texto.append('<a class="nav-link" style="color: #FFFFFF" href="/olhard">Olhar Digital</a>')
    texto.append('</li>')
    
    texto.append('</ul>')
    texto.append('</div>')
    


    texto.append('<div class="container">')
    texto.append('<div class="row">')
    for notice in mongo.db.Noticia.find().sort('date', -1).sort('title', 1):
        texto.append(f'<div class="col-3" style="margin-top: 10px;margin-bottom: 10px;">')
        texto.append(f'<div class="card border-light" mb-3>')
        texto.append(f'<h5 class="card-header" style="text-align:center;">{notice["title"]}</h5>')
        texto.append(f'<img class="card-img-top" src="{notice["img"]}" alt="Card image cap">')
        texto.append(f'<div class="card-body">')
        texto.append(f'<p class="card-text">{notice["dado"]}</p>')
        texto.append(f'<p class="card-text"><small class="text-muted">{notice["date"]} - {notice["tipoSite"]}</small></p>')
        texto.append(f'<a href="{notice["uri"]}" class="btn btn-primary">Veja mais</a>')
        texto.append(f'</div>')
        texto.append(f'</div>')
        texto.append(f'</div>')        
    
    texto.append('</div>')
    texto.append('</div>')

    return '\n'.join(texto)

@app.route('/uol')
def pguol():
    uol()
    texto = ['<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">\n']    
    mongo = PyMongo(app)
    
    texto.append('<div class="navbar navbar-expand navbar-dark flex-column flex-md-row bd-navbar" style="background-color: #563d7c">')
    
    texto.append('<ul class="nav nav-pills">')
    texto.append('<li class="nav-item">')
    texto.append('<a class="nav-link" href="/" style="color: #FFFFFF">Todas</a>')
    texto.append('</li>')
    texto.append('<li class="nav-item">')
    texto.append('<a class="nav-link active" href="/uol">Uol</a>')
    texto.append('</li>')

    texto.append('<li class="nav-item">')
    texto.append('<a class="nav-link" href="/veja" style="color: #FFFFFF">Veja</a>')
    texto.append('</li>')

    texto.append('<li class="nav-item">')
    texto.append('<a class="nav-link" style="color: #FFFFFF" href="/olhard">Olhar Digital</a>')
    texto.append('</li>')
    
    texto.append('</ul>')
    texto.append('</div>')

    texto.append('<div class="container">')
    texto.append('<div class="row">')
    for notice in mongo.db.Noticia.find({'tipoSite': 'uol'}).sort('date', -1).sort('title', 1):
        texto.append(f'<div class="col-3" style="margin-top: 10px;margin-bottom: 10px;">')
        texto.append(f'<div class="card border-light" mb-3>')
        texto.append(f'<h5 class="card-header" style="text-align:center;">{notice["title"]}</h5>')
        texto.append(f'<img class="card-img-top" src="{notice["img"]}" alt="Card image cap">')
        texto.append(f'<div class="card-body">')
        texto.append(f'<p class="card-text">{notice["dado"]}</p>')
        texto.append(f'<p class="card-text"><small class="text-muted">{notice["date"]} - {notice["tipoSite"]}</small></p>')
        texto.append(f'<a href="{notice["uri"]}" class="btn btn-primary">Veja mais</a>')
        texto.append(f'</div>')
        texto.append(f'</div>')
        texto.append(f'</div>')        
    
    texto.append('</div>')
    texto.append('</div>')
    return '\n'.join(texto)

@app.route('/veja')
def pgveja():
    veja()
    texto = ['<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">\n']    
    mongo = PyMongo(app)
    
    texto.append('<div class="navbar navbar-expand navbar-dark flex-column flex-md-row bd-navbar" style="background-color: #563d7c">')
    
    texto.append('<ul class="nav nav-pills">')
    texto.append('<li class="nav-item">')
    texto.append('<a class="nav-link" href="/" style="color: #FFFFFF">Todas</a>')
    texto.append('</li>')
    texto.append('<li class="nav-item">')
    texto.append('<a class="nav-link" href="/uol" style="color: #FFFFFF">Uol</a>')
    texto.append('</li>')

    texto.append('<li class="nav-item">')
    texto.append('<a class="nav-link active" href="/veja">Veja</a>')
    texto.append('</li>')

    texto.append('<li class="nav-item">')
    texto.append('<a class="nav-link" style="color: #FFFFFF" href="/olhard">Olhar Digital</a>')
    texto.append('</li>')
    
    texto.append('</ul>')
    texto.append('</div>')

    texto.append('<div class="container">')
    texto.append('<div class="row">')
    for notice in mongo.db.Noticia.find({'tipoSite': 'veja'}).sort('date', -1).sort('title', 1):
        texto.append(f'<div class="col-3" style="margin-top: 10px;margin-bottom: 10px;">')
        texto.append(f'<div class="card border-light" mb-3>')
        texto.append(f'<h5 class="card-header" style="text-align:center;">{notice["title"]}</h5>')
        texto.append(f'<img class="card-img-top" src="{notice["img"]}" alt="Card image cap">')
        texto.append(f'<div class="card-body">')
        texto.append(f'<p class="card-text">{notice["dado"]}</p>')
        texto.append(f'<p class="card-text"><small class="text-muted">{notice["date"]} - {notice["tipoSite"]}</small></p>')
        texto.append(f'<a href="{notice["uri"]}" class="btn btn-primary">Veja mais</a>')
        texto.append(f'</div>')
        texto.append(f'</div>')
        texto.append(f'</div>')        
    
    texto.append('</div>')
    texto.append('</div>')
    return '\n'.join(texto)


@app.route('/olhard')
def pgolhard():
    olharDigital()
    texto = ['<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">\n']    
    mongo = PyMongo(app)
    
    texto.append('<div class="navbar navbar-expand navbar-dark flex-column flex-md-row bd-navbar" style="background-color: #563d7c">')
    
    texto.append('<ul class="nav nav-pills">')
    texto.append('<li class="nav-item">')
    texto.append('<a class="nav-link" href="/" style="color: #FFFFFF">Todas</a>')
    texto.append('</li>')
    texto.append('<li class="nav-item">')
    texto.append('<a class="nav-link" href="/uol" style="color: #FFFFFF">Uol</a>')
    texto.append('</li>')

    texto.append('<li class="nav-item">')
    texto.append('<a class="nav-link" href="/veja" style="color: #FFFFFF">Veja</a>')
    texto.append('</li>')

    texto.append('<li class="nav-item">')
    texto.append('<a class="nav-link active" href="/olhard">Olhar Digital</a>')
    texto.append('</li>')
    
    texto.append('</ul>')
    texto.append('</div>')

    texto.append('<div class="container">')
    texto.append('<div class="row">')
    for notice in mongo.db.Noticia.find({'tipoSite': 'olharDigital'}).sort('date', -1).sort('title', 1):
        texto.append(f'<div class="col-3" style="margin-top: 10px;margin-bottom: 10px;">')
        texto.append(f'<div class="card border-light" mb-3>')
        texto.append(f'<h5 class="card-header" style="text-align:center;">{notice["title"]}</h5>')
        texto.append(f'<img class="card-img-top" src="{notice["img"]}" alt="Card image cap">')
        texto.append(f'<div class="card-body">')
        texto.append(f'<p class="card-text">{notice["dado"]}</p>')
        texto.append(f'<p class="card-text"><small class="text-muted">{notice["date"]} - {notice["tipoSite"]}</small></p>')
        texto.append(f'<a href="{notice["uri"]}" class="btn btn-primary">Veja mais</a>')
        texto.append(f'</div>')
        texto.append(f'</div>')
        texto.append(f'</div>')        
    
    texto.append('</div>')
    texto.append('</div>')
    return '\n'.join(texto)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)


