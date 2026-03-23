import services
import models


pacientes = []


def menu():
    print("\n===== TRIAGEM HOSPITALAR =====")
    print("1 - Cadastrar paciente")
    print("2 - Listar pacientes")
    print("3 - Remover paciente")
    print("4 - Relatório final")
    print("5 - Estatísticas")
    print("0 - Sair")


def main():
    while True:
        menu()
        opcao = input("Escolha: ")

        if opcao == "1":
            try:
                id = int(input("ID: "))
            except:
                print("ID deve ser número!")
                continue

            if not services.validar_id(id, pacientes):
                print("ID já existe!")
                continue

            nome = input("Nome: ")
            if not services.validar_nome(nome):
                print("Nome inválido!")
                continue

            try:
                idade = int(input("Idade: "))
            except:
                print("Idade deve ser número!")
                continue

            if not services.validar_idade(idade):
                print("Idade inválida!")
                continue

            try:
                febre = float(input("Temperatura: "))
            except:
                print("Temperatura inválida!")
                continue

            if not services.validar_febre(febre):
                print("Temperatura fora do intervalo!")
                continue

            try:
                dor = int(input("Nível de dor (0-10): "))
            except:
                print("Dor inválida!")
                continue

            if not services.validar_dor(dor):
                print("Dor fora do intervalo!")
                continue

            try:
                pressao_sistolica = int(input("Pressão Sistólica: "))
            except:
                print("Pressão Sistólica inválida!")
                continue

            if not services.validar_pressao_sistolica(pressao_sistolica):
                print("Pressão Sistólica fora do intervalo (70-200)!")
                continue

            try:
                pressao_diastolica = int(input("Pressão Diastólica: "))
            except:
                print("Pressão Diastólica inválida!")
                continue

            if not services.validar_pressao_diastolica(pressao_diastolica):
                print("Pressão Diastólica fora do intervalo (40-120)!")
                continue

            try:
                frequencia_cardiaca = int(input("Frequência Cardíaca (bpm): "))
            except:
                print("Frequência Cardíaca inválida!")
                continue

            if not services.validar_frequencia_cardiaca(frequencia_cardiaca):
                print("Frequência Cardíaca fora do intervalo (40-200 bpm)!")
                continue

            paciente = services.criar_paciente(
                id, nome, idade, febre, dor, pressao_sistolica, pressao_diastolica, frequencia_cardiaca)
            models.atualizar_classificacao(paciente)
            models.adicionar_paciente(pacientes, paciente)

            print("Paciente cadastrado com sucesso!")

        elif opcao == "2":
            if not pacientes:
                print("Nenhum paciente cadastrado.")
            for p in models.listar_pacientes(pacientes):
                print(f"{p['nome']} | {p['classificacao']}")

        elif opcao == "3":
            try:
                id = int(input("ID: "))
            except:
                print("ID inválido!")
                continue

            paciente = services.buscar_paciente(id, pacientes)
            if paciente:
                models.remover_paciente(pacientes, paciente)
                print("Removido!")
            else:
                print("Paciente não encontrado!")

        elif opcao == "4":
            print("\n===== RELATÓRIO FINAL =====")
            for nome, idade, pontos, classe in models.gerar_relatorio(pacientes):
                print(f"{nome} | Idade: {idade} | Pontos: {pontos} | {classe}")

        elif opcao == "5":
            print("\n===== ESTATÍSTICAS =====")
            print("Total de pacientes:", models.total_pacientes(pacientes))
            print("Vermelhos:", models.contar_por_classificacao(
                pacientes, "VERMELHO"))
            print("Laranjas:", models.contar_por_classificacao(
                pacientes, "LARANJA"))
            print("Amarelos:", models.contar_por_classificacao(
                pacientes, "AMARELO"))
            print("Verdes:", models.contar_por_classificacao(pacientes, "VERDE"))

        elif opcao == "0":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida!")


main()
