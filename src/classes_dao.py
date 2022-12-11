import sqlite3
import requests
import xmltodict

from src.classes_base import Usuario, Artigo

#objeto de acesso a dados - DAO

class UsuarioDAO:
    
    def __init__(self, db_path):
        self.db_path = db_path
    
    def cadastrar_usuario(self, usuario):
            
        conexao = sqlite3.Connection(self.db_path)

        cursor = conexao.cursor()

        comando_sql = """
        INSERT INTO usuarios (cpf,nome,email,senha) 
        VALUES (?, ?, ?, ?)
        """
        
        cursor.execute(comando_sql, \
            (usuario._cpf, usuario._nome, usuario._email, usuario._senha))

        conexao.commit()

        conexao.close()

    def buscar_usuario(self, cpf):

        conexao = sqlite3.connect(self.db_path)

        cursor = conexao.cursor()

        comando_sql = """
        SELECT * FROM usuarios WHERE cpf = ?
        """
        
        cursor.execute(comando_sql, (cpf, ))

        usuario_tupla = cursor.fetchone()

        conexao.close()

        if usuario_tupla is None:
            return None
        
        usuario = Usuario(cpf=usuario_tupla[0], nome=usuario_tupla[1], \
            email=usuario_tupla[2], senha=usuario_tupla[3])


        return usuario


    def buscar_email(self, email):

        conexao = sqlite3.connect(self.db_path)

        cursor = conexao.cursor()

        comando_sql = """
        SELECT * FROM usuarios WHERE email = ?
        """
        
        cursor.execute(comando_sql, (email, ))

        usuario_tupla = cursor.fetchone()

        conexao.close()

        if usuario_tupla is None:
            return None
        
        usuario = Usuario(cpf=usuario_tupla[0], nome=usuario_tupla[1], \
            email=usuario_tupla[2], senha=usuario_tupla[3])


        return usuario


    def listar_usuarios(self):
        
        conexao = sqlite3.connect(self.db_path)

        cursor = conexao.cursor()

        comando_sql = """
        SELECT * FROM cursos
        """

        cursor.execute(comando_sql)

        usuarios_tuplas = cursor.fetchall()

        cursor.close()

        if len(usuarios_tuplas) == 0:
            return None

        usuarios = []

        for usuario_tupla in usuarios_tuplas:

            usuario = Usuario(cpf=usuario_tupla[0], nome=usuario_tupla[1], \
                email=usuario_tupla[2], senha=usuario_tupla[3])
            
            usuarios.append(usuario)
        
        return usuarios



class ArtigoDAO:
    def __init__(self,db_path):
        self._db_path=db_path

    def buscar_artigo(self,usuario,pesquisa,quantidade):
        
        requisicao = requests.get(f'http://export.arxiv.org/api/query?search_query=all:{pesquisa}&start=0&max_results={quantidade}')

        dicionario_1 = xmltodict.parse(requisicao.text)


        dicionario_2 = dicionario_1['feed']

        dicionario_3 =dicionario_2['entry']
        qtd_list = len(dicionario_3)
        lista_id = []
        lista_autores = []
        lista_titulo = []
        lista_resumo = []
        url = requisicao.url

        if (quantidade == 1): 
                dicionario_4 = dicionario_3['author']
                lista_id.append(dicionario_3['id'])
                lista_titulo.append(dicionario_3['title'])
                lista_resumo.append(dicionario_3['summary'])
                quantidade_itens = len(dicionario_4) 
                if (quantidade_itens == 1):
                    lista_autores.append(dicionario_4['name'])
                else:
                    for i in range(quantidade_itens):
                        lista_autores.append(dicionario_4[i]['name'])



        else:
        
            for n in range(qtd_list):
                lista_nome = [] 
                lista_id.append(dicionario_3[n]['id'])     
                lista_titulo.append(dicionario_3[n]['title'])
                lista_resumo.append(dicionario_3[n]['summary'])
                dicionario_4 = dicionario_3[n]['author']
                quantidade_itens = len(dicionario_4) 
                if (quantidade_itens == 1):
                    lista_autores.append(dicionario_4['name'])
                else:  
                    for i in range(quantidade_itens):
                        lista_nome.append(dicionario_4[i]['name'])
                    lista_autores.append(lista_nome)


        conexao = sqlite3.Connection(self._db_path)

        cursor = conexao.cursor()

        comando_sql = """
        INSERT INTO artigos (id,titulo,resumo,link,cpf,consulta) 
        VALUES (?, ?, ?, ?, ?, ?)
        """
        for t in range(qtd_list):
            cursor.execute(comando_sql, \
                (lista_id[t], lista_titulo[t], lista_resumo[t], url ,usuario._cpf, pesquisa))

            artigo = Artigo(lista_id[t], lista_titulo[t], lista_resumo[t], url ,usuario._cpf, pesquisa)

        conexao.commit()

        conexao.close()



    def listar_artigos(self):
        conexao = sqlite3.connect(self._db_path)

        cursor = conexao.cursor()

        comando_sql = """
        SELECT * FROM artigos
        """

        cursor.execute(comando_sql)

        artigos_tuplas = cursor.fetchall()

        cursor.close()

        if len(artigos_tuplas) == 0:
            return None

        artigos = []

        for artigo_tupla in artigos_tuplas:

            artigo = Artigo(id=artigo_tupla[0], titulo=artigo_tupla[1], \
                resumo=artigo_tupla[2], link=artigo_tupla[3], cpf=artigo_tupla[4], consulta=artigo_tupla[5])
            
            artigos.append(artigo)
        
        return artigos