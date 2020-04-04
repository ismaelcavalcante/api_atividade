from models import Pessoas, db_session
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

if __name__ == '__main__':
    #inserir_pessoa()
    consultar_pessoas()
    #alterar_pessoa()
    #exluir_pessoa()