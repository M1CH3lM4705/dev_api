from flask_restful import Resource

lista_Habilidades = [
    'Python',
    'C++',
    'C#',
    'Css',
]

class Habilidades(Resource):
    def get(self):
        return lista_Habilidades