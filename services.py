
def criar_paciente(id, nome, idade, febre, dor, pressao_sistolica, pressao_diastolica, frequencia_cardiaca):
    return {
        "id": id,
        "nome": nome,
        "idade": idade,
        "febre": febre,
        "dor": dor,
        "pressao_sistolica": pressao_sistolica,
        "pressao_diastolica": pressao_diastolica,
        "frequencia_cardiaca": frequencia_cardiaca,
        "pontuacao": 0,
        "classificacao": ""
    }


def validar_nome(nome):
    return nome.isalpha() #isalpha() verifica se o nome tem apenas letras.


def validar_id(id, pacientes):
    for p in pacientes:
        if p["id"] == id:
            return False
    return True


def validar_idade(idade):
    return idade > 0


def validar_febre(temp):
    return 34 <= temp <= 42


def validar_dor(dor):
    return 0 <= dor <= 10


def validar_pressao_sistolica(pressao_sistolica):
    return 70 <= pressao_sistolica <= 200


def validar_pressao_diastolica(pressao_diastolica):
    return 40 <= pressao_diastolica <= 120


def validar_frequencia_cardiaca(frequencia):
    return 40 <= frequencia <= 200


def buscar_paciente(id, pacientes):
    for p in pacientes:
        if p["id"] == id:
            return p
    return None
