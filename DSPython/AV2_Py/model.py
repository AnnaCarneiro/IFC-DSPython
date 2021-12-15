from config import *

class Funcionario(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    cpf = db.Column(db.String(254))    
    
    def __str__(self):
        return self.nome + "[id="+str(self.id)+ "], " +\
            self.cpf 
    
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "cpf": self.cpf,
            
        }

class VendedorExterno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cnh = db.Column(db.String(254)) 
    
    def __str__(self):
        return f"{self.cnh} [{self.id}]"  
    def json(self):
        return {
            "id":self.id,
            "cnh":self.cnh            
        }
    
class EngenheiroCivil(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numCrea = db.Column(db.String(254))
    
    funcionario_id = db.Column(db.Integer, db.ForeignKey(Funcionario.id))
    vendedorExterno_id =  db.Column(db.Integer, db.ForeignKey(VendedorExterno.id))
    funcionario = db.relationship("Funcionario")    
    vendedorExterno = db.relationship("VendedorExterno")
    

   
    def __str__(self): # expressão da classe em forma de texto
        return f"{self.numCrea}, {self.funcionario}, {self.vendedorExterno}" 

    def json(self):
        return {
            "id":self.id,
            "numCrea":self.numCrea,            
            "funcionario_id":self.funcionario_id,
            "funcionario":self.funcionario.json(),
            "vendedorExterno_id":self.vendedorExterno_id,
            "vendedorExterno":self.vendedorExterno.json()
        }


# teste    
if __name__ == "__main__":
    # apagar o arquivo, se houver
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # criar tabelas
    db.create_all()

    # criar funcionario
    f1 = Funcionario(nome = "Jose Santos", cpf = "000.001.002-00")
    f2 = Funcionario(nome = "Larissa Massala", cpf = "001.002.003-01")        
    db.session.add(f1)
    db.session.add(f2)
    db.session.commit()
    
    # criar vendedor externo
    v1 = VendedorExterno(cnh="01394637515")
    v2 = VendedorExterno(cnh="21400788563")    
    db.session.add(v1)
    db.session.add(v2)
    db.session.commit()
    
     # criar engenheiro civil
    ec1 = EngenheiroCivil(numCrea = "010203040-0", funcionario = f1, vendedorExterno = v1) 
    ec2 = EngenheiroCivil(numCrea = "050607080-1", funcionario = f2, vendedorExterno = v2)  
    db.session.add(ec1)
    db.session.add(ec2)
    db.session.commit()
    
    #exibir    
    print(ec1)
    print(ec2)
    print(ec1.json())
    print(ec2.json())
    
    
   