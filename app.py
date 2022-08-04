from flask import Flask

app=Flask(__name__)

@app.route('/')
def titulo():
    return "Desarrollo de Sistemas Web"