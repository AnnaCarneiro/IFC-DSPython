from config import *
from modelo import TurmaDaMonica

@app.route("/")
def inicio():
    return 'Sistema de Cadastro da Turma da Mônica' +\
        '<a href= "/listar_turmadamonica">Operação listar</a>'


@app.route("/listar_turmadamonica")
def listar_turmadamonica():
    #Obter Turminha do cadastro
    turmadamonica = db.session.query(TurmaDaMonica).all()
    #Aplica Json a cada elemento da Lista Turma Da Monica
    turmadamonica_em_json = [x.json() for x in turmadamonica]
    #Converte a lista Python para Json
    resposta = jsonify(turmadamonica_em_json)
    #Permite enviar para qualquer solicitante
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    #Retorno
    return resposta

app.run(debug=True)