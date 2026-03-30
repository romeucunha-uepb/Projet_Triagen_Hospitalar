
def adicionar_paciente(lista, paciente):
    lista.append(paciente)

def remover_paciente(lista, paciente):
    lista.remove(paciente)

def calcular_pontuacao(paciente):
    pontos = 0

    # Febre
    if paciente["febre"] >= 39:
        pontos += 3
    elif paciente["febre"] >= 37.5:
        pontos += 1

    # Dor
    if paciente["dor"] >= 8:
        pontos += 3
    elif paciente["dor"] >= 5:
        pontos += 2
    elif paciente["dor"] >= 3:
        pontos += 1

    # Pressão Sistólica
    if paciente["pressao_sistolica"] >= 160 or paciente["pressao_sistolica"] < 90:
        pontos += 3
    elif paciente["pressao_sistolica"] >= 140:
        pontos += 2

    # Pressão Diastólica
    if paciente["pressao_diastolica"] >= 100 or paciente["pressao_diastolica"] < 60:
        pontos += 2

    # Frequência Cardíaca
    if paciente["frequencia_cardiaca"] >= 120 or paciente["frequencia_cardiaca"] < 60:
        pontos += 2

    # Idade
    if paciente["idade"] >= 60:
        pontos += 2

    return pontos

def classificar_risco(pontos):
    if pontos >= 7:
        return "VERMELHO (Emergência)"
    elif pontos >= 5:
        return "LARANJA (Muito Urgente)"
    elif pontos >= 3:
        return "AMARELO (Urgente)"
    else:
        return "VERDE (Pouco Urgente)"


def atualizar_classificacao(paciente):
    pontos = calcular_pontuacao(paciente)
    paciente["pontuacao"] = pontos
    paciente["classificacao"] = classificar_risco(pontos)


def listar_pacientes(lista):
    return lista

def pegar_pontuacao(x):
    return x["pontuacao"]

def ordenar_por_prioridade(lista):
    return sorted(lista, key=pegar_pontuacao, reverse=True)


def total_pacientes(lista):
    return len(lista)


def contar_por_classificacao(lista, cor):
    contador = 0
    for p in lista:
        if cor in p["classificacao"]:
            contador += 1
    return contador


def gerar_relatorio(lista):
    relatorio = []
    ordenados = ordenar_por_prioridade(lista)

    for p in ordenados:
        relatorio.append(
        (p["nome"], p["id"], p["idade"], p["pontuacao"], p["classificacao"])
        )

    return relatorio
