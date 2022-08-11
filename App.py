# coding: utf-8
from flask import Flask, render_template
app = Flask("challenge")

@app.route("/")
def none():
    return '<meta http-equiv="refresh" content="0.1; URL=/index.html" />', 200

@app.route("/index.html")
def index():
    variaveis = {
        "motive":"Desafio da Primeira Aula",
        "table":"Produtos",
        "array":[
            {
                "name":"Garrafa",
                "value":"12.99"
            },
            {
                "name":"Calculadora",
                "value":"4.98"
            },
            {
                "name":"Impressora",
                "value":"875.65"
            },
            {
                "name":"Mouse",
                "value":"75.95"
            }
        ]
    }
    return render_template("index.html", v = variaveis), 200

if __name__ == "__main__":
    app.run()