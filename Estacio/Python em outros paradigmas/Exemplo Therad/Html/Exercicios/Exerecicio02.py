from flask import Flask

app =Flask(__name__)

@app.route('/')
def cumprimento():
    boas_vindas='<h1> Olá , progamadorees</h1>'
    link = '<p><a href="user/Usuario">Clique aqui</a></p>'
    return boas_vindas+link

@app.route('/user/')
@app.route('/user/<nome>')
def user(nome="Usuario"):
    personalizar=f'<h1>,{nome}</h1>'
    introducao ='<p>Altere o nome no <en> endereço do browser</em>\ e recarregue a pagina.</p>'
    return personalizar+introducao




if __name__ =="__main__":
    app.run(debug=True)