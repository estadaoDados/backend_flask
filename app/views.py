from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Diego' } # fake user
    app = {
            'title': "Cruzador de Opiniões",
            "name": "Cruzador de Opiniões",
            "description": "Cruzador de Opiniões: Ferramenta para bla bla bla",
            "linha_fina": "Escolha sua pergunta e o eleitorado e veja seu comportamento",
            "keywords": ["opinião","ibope","pesquisa","eleição2014"],
            "image": "logo_estadao_dados.png",
            "cssFiles": ["estadaodados.css"],
            "jsFiles": ["signals.min.js","crossroads.js"]}
    return render_template("index.html",
        title = 'Home',
        user = user,
        app = app)
@app.route('/doacoes2014')
def doacoes2014():
    user = { 'nickname': 'Diego' } # fake user
    app = {
            'title': "Doações 2014",
            "name": "Doações 2014",
            "description": "Navegue no mapa das doações eleitorais.",
            "linha_fina": "Navegue no mapa das doações eleitorais.",
            "keywords": ["eleições 2014","doações","financiamento","campanha"],
            "image": "logo_estadao_dados.png",
            "cssFiles": ["doacoes2014.css"],
            "jsFiles": ["d3.v3.min.js","doacoes2014.js"]}
    return render_template("doacoes2014.html",
        title = 'Doações 2014',
        user = user,
        app = app)

