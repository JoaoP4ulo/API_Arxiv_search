import os
import src.utils as utils
import src.controlador_menu as menu

from src.classes_dao import UsuarioDAO,ArtigoDAO


if __name__ == '__main__':

    #definição do caminho padrão do db
    db_path = 'cadastros.bd'
    #definição da senha padrão de recuperação de email
    senha = 'xxxxxxxxxxxx'
    email_from='xxxxxxxx@gmail.com'


    #verificar se o banco de dados existe
    if not os.path.exists(db_path):
        utils.criar_bancodados(db_path)

    usuario_dao = UsuarioDAO(db_path)
    artigo_dao = ArtigoDAO(db_path)
    
    #menu principal
    menu.menu_principal()
    