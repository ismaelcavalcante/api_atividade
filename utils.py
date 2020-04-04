from models import Pessoas, db_session, Usuarios


# insere uma pessoa na tabela pessoas
def inserir_pessoa():
    pessoa = Pessoas(nome='Nicole', idade=0)
    print(pessoa)
    pessoa.save()

# consulta pessoas na tabela pessoas
def consultar_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Ismael').first()
    print(pessoa.idade)

# altera uma pessoa na tabela pessoas
def alterar_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Ismael').first()
    pessoa.idade = 30
    pessoa.save()

# exclui uma pessoa na tabela pessoas
def exluir_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Nicole').first()
    pessoa.delete()

def inserir_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consultar_usuarios():
    usuario = Usuarios.query.all()
    print(usuario)

if __name__ == '__main__':
    #inserir_usuario('ismael', '123')
    #inserir_usuario('cavalcante', '123')
    consultar_usuarios()
    #inserir_pessoa()
    #consultar_pessoas()
    #alterar_pessoa()
    #exluir_pessoa()