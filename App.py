# coding: utf-8
import re
import json
import urllib
from flask import Flask, render_template, request
app = Flask("challenge")

@app.route("/")
def none():
    return "<meta http-equiv='refresh' content='0.1; URL=/login.html'/>", 200

@app.route('/index.html')
def index():
    name = urllib.parse.unquote(re.sub(r'.*?login\_name\=(.*?)(\&.*|$)', '\g<1>', request.full_path.replace('+', ' ')))
    print(name)
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
            },
            {
                "name":"Vaso",
                "value":"80.0"
            }
        ]
    }
    variaveis = json.loads(re.sub(r'(\"value\"\s?\:\s?\"\d+\.\d)\"', '\g<1>0"', json.dumps(variaveis)))
    return render_template("index.html", n = name, v = variaveis), 200

@app.route("/login.html")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run()