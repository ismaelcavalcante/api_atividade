from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Atividades

app = Flask(__name__)
api = Api(app)

class Pessoa(Resource):
    # Pesquisar uma pessoa específica cadastrada
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id
            }
        except AttributeError:
            response = {
                'status': 'Erro',
                'mensagem': 'Pessoa não encontrada'
            }
        return response

    # Modificar os dados de uma pessoa
    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {
            'nome': pessoa.nome,
            'idade': pessoa.idade,
            'id': pessoa.id
        }
        return response

    #Ecluir uma pessoa
    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        pessoa.delete()
        return {'status': 'sucesso', 'mensagem': f'pessoa {pessoa.nome} excluída com sucesso.'}

class ListaPessoas(Resource):
    #Pesquisar todas as pessoas cadastradas
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id':i.id, 'nome':i.nome, 'idade':i.idade} for i in pessoas]
        return response

    #Inserir uma pessoa
    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
            'nome': pessoa.nome,
            'idade': pessoa.idade,
            'id': pessoa.id
        }
        return response

class ListaAtividade(Resource):
    def get(self):
        atividades = Atividades.query.all()
        response = [{'id': i.id, 'nome': i.nome, 'pessoa': i.pessoa.nome} for i in atividades]
        return response

    # Inserir uma atividade
    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa': atividade.pessoa.nome,
            'nome': atividade.nome,
            'id': atividade.id
        }
        return response


api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(ListaPessoas, '/pessoa/')
api.add_resource(ListaAtividade, '/atividade/')

if __name__ == '__main__':
    app.run(debug=True)