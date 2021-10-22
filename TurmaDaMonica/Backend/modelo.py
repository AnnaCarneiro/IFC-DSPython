from config import *

class TurmaDaMonica(db.Model):
    # atributos da Turma Da Monica
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    idade = db.Column(db.String(254))
    altura = db.Column(db.String(254))
    especialidade = db.Column(db.String(254))

    # método para mostrar em formato de texto
    def __str__(self):
        return str(self.id)+") "+ self.nome + ", " +\
            self.idade + ", " + self.altura + ", " + self.especialidade
            
    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "altura": self.altura,
            "especialidade": self.especialidade
        }

# teste    
if __name__ == "__main__":
    # apagar o arquivo, se houver
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # criar tabelas
    db.create_all()

    # teste da classe TurmaDaMonica
    t1 = TurmaDaMonica(nome = "Cebolinha", idade = "7", 
        altura = "1,23", especialidade="Planos infalíveis")
    t2 = TurmaDaMonica(nome = "Cascão", idade = "7", 
        altura = "1,20", especialidade="Escapar da água")   
    t3 = TurmaDaMonica(nome = "Mônica", idade = "7", 
        altura = "1,10", especialidade="Dar coelhadas")     
    t4 = TurmaDaMonica(nome = "Magali", idade = "7", 
        altura = "1,20", especialidade="Comer")
    t5 = TurmaDaMonica(nome = "Franjinha", idade = "9", 
        altura = "1,30", especialidade="Cientista")
    
    # persistir
    db.session.add(t1)
    db.session.add(t2)
    db.session.add(t3)
    db.session.add(t4)
    db.session.add(t5)
    db.session.commit()
    
    # exibir a turminha
    print(t1)
    print(t2)
    print(t3)
    print(t4)
    print(t5)
    
    #exibir turminha json
    print(t1.json())
    print(t2.json())
    print(t3.json())
    print(t4.json())
    print(t5.json())