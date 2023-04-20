import sqlite3
from src.classes_dao import UsuarioDAO, ArtigoDAO
from src.classes_base import Usuario, Artigo
import app


#funções chamdas pelo menu de usuario


def menu_sistema(usuario_existente):
    while True:

        print('\n\n\n --------- Sistema de Cadastro --------- \n')

        print('  1 – Realizar Busca Arxiv')
        print('  2 – Listar Artigos')
        print('  3 – Atualizar Dados')
        print('  4 – Voltar Menu Principal')
    

        opcao = input('\n  Digite a opção desejada: ')

        if opcao == '1':
            sistema_fazer_busca(app.artigo_dao,usuario_existente)
        elif opcao == '2':
            sistema_listar_artigos(app.artigo_dao)
        elif opcao == '3':
            atualizar_dados(app.usuario_dao,usuario_existente)
        elif opcao == '4':
            print('\n\n  Saindo do sistema ...')
            break
        else:
            print('\n\n  Opção Inválida!')

def atualizar_dados(usuario_dao,usuario):

    conexao = sqlite3.connect(usuario_dao.db_path)

    cursor = conexao.cursor()


    op_nome=input('\n Deseja alterar o nome (y/n): ')
    if op_nome=='y':
        nome=input("\n Nome: ")
        usuario.set_nome(nome)

        comando_sql_nome = """
        UPDATE usuarios SET nome = ? WHERE cpf = ?
        """
        cursor.execute(comando_sql_nome, (nome,usuario._cpf))
        conexao.commit()

    op_email=input('\n Deseja alterar o email (y/n): ')
    if op_email=='y':
        email=input("\n Email: ")
        usuario.set_email(email)

        comando_sql_email = """
        UPDATE usuarios SET email = ? WHERE cpf = ?
        """
        cursor.execute(comando_sql_email, (email,usuario._cpf))
        conexao.commit()

    op_senha=input('\n Deseja alterar a senha (y/n): ')
    if op_senha=="y":
        senha=input("\n Senha: ")
        usuario.set_senha(senha)

        comando_sql_senha = """
        UPDATE usuarios SET senha = ? WHERE cpf = ?
        """
        cursor.execute(comando_sql_senha, (senha,usuario._cpf))
        conexao.commit()

    conexao.close()
    
def sistema_fazer_busca(artigo_dao,usuario):

    pesquisa = input('Digite o termo que deseja pesquisar: ')

    quantidade = int(input('Digite a quantidade (limite = 100) de artigos que deseja recuperar: '))

    if (quantidade>100):
        quantidade  = 100
        
    elif(quantidade<0):
        print('Só se pode pesquisar quantidades positivas, pensando nisso ja estamos calculando e pesquisando para você!')
        quantidade = quantidade*(-1)

    artigo_dao.buscar_artigo(usuario,pesquisa,quantidade)



def sistema_listar_artigos(artigos_dao):

    artigos = artigos_dao.listar_artigos()

    if artigos is not None:
        print('\n\n  Total de artigos:', len(artigos))
        print('\n  --------------- artigos ---------------\n')
        for artigo in artigos:
            print('\n    id:', artigo._id)
            print('      titulo:', artigo._titulo)
            print('      resumo:', artigo._resumo)
            print('      link:', artigo._link)
            print('      cpf:', artigo._cpf)
            print('      consulta:', artigo._consulta)
    else:
        print('\n\n  Nenhum artigo cadastrado!')