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
    # soup2 = BeautifulSoup(tagMain.text, 'lxml')
    # tagDivRow = soup2.find_all('div', class_="row")  

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
                        img = item.a.img.get('data-src')

                        mongo = PyMongo(app)
                        mongo.db.Noticia.insert({'uri': link, 'dado' : dado, 'date': date.today().strftime("%d/%m/%Y"), 'title': title, 'img': img})
                        return



@app.route('/')
def index():
    veja()
    texto = ['<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">\n']    
    mongo = PyMongo(app)
    #dbnoticias = mongo.db.Noticia.find()
    texto.append('<div class="container">')
    texto.append('<div class="row">')
    for notice in mongo.db.Noticia.find():
        texto.append(f'<div class="col-3">')
        texto.append(f'<div class="card">')
        texto.append(f'<h5 class="card-title">{notice["uri"]}</h5>')
        texto.append(f'<p class="card-text">{notice["dado"]}</p>')
        texto.append(f'<a href="{notice["uri"]}" class="btn btn-primary">Veja mais</a>')
        texto.append(f'</div>')
        texto.append(f'</div>')        
    
    texto.append('</div>')
    texto.append('</div>')

    return '\n'.join(texto)



if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)


