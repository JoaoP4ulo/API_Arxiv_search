
#classes padrão

class Usuario:

    def __init__(self, cpf, nome, email, senha):
        self._cpf=cpf
        self._nome=nome
        self._email=email
        self._senha=senha
    
   
    def get_cpf(self):
        return self._cpf   
    def set_cpf(self, novo_cpf):
        if novo_cpf <= 11:
            self._cpf = novo_cpf

    def get_nome(self):
        return self._nome  
    def set_nome(self, novo_nome):
        self._nome = novo_nome

    def get_email(self):
        return self._email
    def set_email(self, novo_email):
        self._email = novo_email
    
    def get_senha(self):
        return self._senha
    def set_senha(self, novo_senha):
        self._senha = novo_senha
    
    def __repr__(self):
        return f'CPF: {self._cpf}\nNome: {self._nome}\nEmail: {self._email}\nSenha: {self._senha}'


class Artigo:
    def __init__(self,id,titulo,resumo,link,cpf,consulta):
        self._id=id
        self._titulo=titulo
        self._resumo=resumo
        self._link=link
        self._cpf=cpf
        self._consulta=consulta

    def get_id(self):
        return self._id   
    def set_id(self, novo_id):   
        self._id = novo_id

    def get_titulo(self):
        return self._titulo   
    def set_titulo(self, novo_titulo):   
        self._titulo = novo_titulo

    def get_resumo(self):
        return self._resumo   
    def set_resumo(self, novo_resumo):   
        self._resumo = novo_resumo

    def get_link(self):
        return self._link   
    def set_link(self, novo_link):   
        self._link = novo_link

    def get_cpf(self):
        return self._cpf   
    def set_cpf(self, novo_cpf):   
        self._cpf = novo_cpf

    def get_consulta(self):
        return self._consulta   
    def set_consulta(self, nova_consulta):   
        self._consulta = nova_consulta