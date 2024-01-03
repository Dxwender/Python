from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('indice.html')


@app.route('/ola/')
@app.route('/ola/<nome>')
def ola_mundo(nome="mundo", nome_recebido=None):
    return "Olá, ", nome_recebido =nome


if __name__ == '__main__':
    app.run()