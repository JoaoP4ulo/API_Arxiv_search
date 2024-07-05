import os
import src.utils as utils
import src.controlador_menu as menu

from src.classes_dao import UsuarioDAO,ArtigoDAO



#definição do caminho padrão do db
db_path = 'cadastros.bd'
#definição da senha padrão de recuperação de email
senha = ''
email_from=''
usuario_dao = UsuarioDAO(db_path)
artigo_dao = ArtigoDAO(db_path)

if __name__ == '__main__':
    #verificar se o banco de dados existe
    if not os.path.exists(db_path):
        utils.criar_banco_de_dados(db_path)

        
    #menu principal
    menu.menu_principal()
        
