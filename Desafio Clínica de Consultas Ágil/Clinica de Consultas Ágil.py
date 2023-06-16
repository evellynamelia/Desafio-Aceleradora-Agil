from datetime import datetime

# Lista de armarzenamento dos pacientes cadastrados
PacientesCadastrados = []

# Lista de armazenamento dos Agendamentos
Agendamentos = []

# Cadastro Paciente
def CadastroPaciente():
    nome = input("Digite o nome do paciente: ")
    if any(char.isdigit() for char in nome):
        print("\nOpção inválida. O nome do Paciente não pode conter números.")
        return
        
    
    telefone = input("Digite o telefone do paciente: ")
    for paciente in PacientesCadastrados:
        if paciente["telefone"] == telefone:
            print("Paciente já cadastrado!")
            return
        
    paciente = { "nome": nome, "telefone": telefone }
    print("Paciente cadastrado com sucesso!")

    PacientesCadastrados.append(paciente)

# Listas Paciente
def PacienteLista():
        print("\n============ Pacientes Cadastrados ============")
        for i, Paciente in enumerate(PacientesCadastrados, start=1):
            print(f"{i}. Paciente: {Paciente['nome']}, Telefone: {Paciente['telefone']}")

# Marcações das Consultas
def Consultas():
    if len(PacientesCadastrados) == 0:
         print("Não á nenhum paciente cadastrado na clinica.")
         return
    
    print(PacienteLista())
    NumeroPaciente = int(input("Digite o número do paciente: "))
    if NumeroPaciente < 1 or NumeroPaciente > len(PacientesCadastrados):
        print("Número inválido.")
        return
    
    Paciente = PacientesCadastrados[NumeroPaciente - 1]
    ConsultaDesejada = input("Digite a consulta Desejada: ")
    DiaConsulta = input("Digite o dia desejado para o agendamento da Consulta (formato: dd/mm/aaaa): ")
    HoraConsulta = input("Digite a Hora desejada: (formato: hh:mm): ")

    DataHora = datetime.strptime(DiaConsulta + " " + HoraConsulta, "%d/%m/%Y %H:%M")
    DataHoraAtual = datetime.now()

    if DataHora < DataHoraAtual:
        print("Não é possível agendar consultas retroativas.")
        return

    for agendamento in Agendamentos:
        DataHoraCadastrada = datetime.strptime(agendamento["Dia"] + " " + agendamento["Hora"], "%d/%m/%Y %H:%M")
        if DataHora == DataHoraCadastrada:
            print("Data e hora indisponíveis para agendamento.")
            return

    Agendamentos.append({ "Consulta": ConsultaDesejada, "Paciente": Paciente, "Dia": DiaConsulta, "Hora": HoraConsulta })
    print("Consulta marcada com sucesso.")

# Cancelamento das Consultas
def cancelamentoConsulta():
    if len(Agendamentos) == 0:
        print("Não há agendamentos para cancelar.")
        return

    print("\n============ Agendamentos ============")
    for i, agendamento in enumerate(Agendamentos, start=1):
        print(f"{i}. Paciente: {agendamento['Paciente']['nome']}, Telefone: {agendamento['Paciente']['telefone']}, Dia: {agendamento['Dia']}, Hora: {agendamento['Hora']}, Consulta: {agendamento['Consulta']}")
    
    agendamento_numero = int(input("Digite o número do agendamento para cancelar: "))
    if agendamento_numero < 1 or agendamento_numero > len(Agendamentos):
        print("Número inválido.")
        return
    
    agendamento = Agendamentos[agendamento_numero - 1]
    print("\nAgendamento selecionado:")
    print(f"Paciente: {agendamento['Paciente']['nome']}, Telefone: {agendamento['Paciente']['telefone']}, Dia: {agendamento['Dia']}, Hora: {agendamento['Hora']}, Consulta: {agendamento['Consulta']}")
    
    confirmacao = input("\nDeseja cancelar a consulta? [ 1-Sim ] [ 2-Não ]: ")
    if confirmacao.upper() == "1":
        Agendamentos.pop(agendamento_numero - 1)
        print("Consulta cancelada com sucesso.")

def menu_principal():
    while True:
        print("\n============ Clinica de Consultas Ágil ============")
        print("|                                                   |")
        print("|1. Cadastrar paciente;                             |")
        print("|2. Marcar Consulta;                                |")
        print("|3. Cancelar Consulta;                              |")
        print("|0. Sair.                                           |")
        print("|                                                   |")
        print("=====================================================")
        
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            CadastroPaciente()
        elif opcao == "2":
            Consultas()
        elif opcao == "3":
            cancelamentoConsulta()
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Chama a função do menu principal para iniciar o programa
menu_principal()

print("Obrigado por usar a Clínica de Consultas Ágil. Até logo!")
