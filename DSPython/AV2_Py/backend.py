from config import *
from model import Funcionario, VendedorExterno, EngenheiroCivil

@app.route("/")
def inicio():
    return 'Sistema de cadastro de Engenheiros Civil da Cosntrutora AXA. '+\
        '<a href="/listar_funcionarios">Operação listar</a>'

# Funções para classe Funcionario

@app.route("/listar_funcionarios")
def listar_funcionarios():
    
    funcionarios = db.session.query(Funcionario).all()    
    funcionarios_em_json = [ x.json() for x in funcionarios ]
    # converter a lista do python para json
    resposta = jsonify(funcionarios_em_json)
    # PERMITIR resposta para outras pedidos oriundos de outras tecnologias
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # retornar...

@app.route("/incluir_funcionario", methods=['post'])
def incluir_funcionario():
    # preparar uma resposta otimista
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    
    dados = request.get_json() #(force=True) dispensa Content-Type na requisição
    try: 
      nova = Funcionario(**dados) 
      db.session.add(nova) 
      db.session.commit() 
    except Exception as e:
     
      resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # responder!

@app.route("/excluir_funcionario/<int:funcionario_id>", methods=['DELETE'])
def excluir_funcionario(funcionario_id):
    # preparar uma resposta otimista
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    try:
        # excluir 0 funcionario do ID informado
        Funcionario.query.filter(Funcionario.id == funcionario_id).delete()
        # confirmar a exclusão
        db.session.commit()
    except Exception as e:        
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # responder!

#-----------------------------------------------------------------------------------

# Funções para classe VendedorExterno

@app.route("/listar_vendedoresExternos")
def listar_vendedoresExternos():
    
    vendedoresExternos = db.session.query(VendedorExterno).all()    
    vendedoresExternos_em_json = [ x.json() for x in vendedoresExternos ]
    
    resposta = jsonify(vendedoresExternos_em_json)
    # PERMITIR resposta para outras pedidos oriundos de outras tecnologias
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # retornar...

@app.route("/incluir_vendedorExterno", methods=['post'])
def incluir_vendedorExterno():
    # preparar uma resposta otimista
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    
    dados = request.get_json()
    try: 
      nova = VendedorExterno(**dados) 
      db.session.add(nova) 
      db.session.commit() 
    except Exception as e:
      
      resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # responder!

#--------------------------------------------------------------------

#Funções para classe EngenheiroCivil

@app.route("/listar_engenheiros")
def listar_engenheiros():    
    engenheiros = db.session.query(EngenheiroCivil).all()
    # converter dados para json
    lista_jsons = [ x.json() for x in engenheiros]
    # converter a lista do python para json
    resposta = jsonify(lista_jsons)
    # PERMITIR resposta para outras pedidos oriundos de outras tecnologias
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

app.run(debug=True)