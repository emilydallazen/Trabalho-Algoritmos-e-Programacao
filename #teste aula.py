
# Função para verificar se uma data e hora já estão ocupadas na agenda
def verificar_disponibilidade(compromissos, data, hora):
    for compromisso in compromissos:
        if compromisso['data'] == data and compromisso['hora'] == hora:
            return False
    return True

# Função pra incluir um novo compromisso na agenda
    #Uso da função para verificar disponibilidade do compromisso, caso já tenha sido cadastrado, exibir a mensagem de indisponibilidade

def incluir_compromisso():
    data = input("Digite a data do evento (dd/mm/aaaa): ")
    hora = input("Digite a hora do evento (hh:mm): ")
    duracao = float(input("Digite a duração do evento (em horas): "))
    descricao = input("Digite a descrição do evento: ")
    data_hora = f"{data} {hora}"
    if not verificar_disponibilidade(agenda, data, hora):
        print("Já existe um evento agendado para esta data e hora.")
    else:
        compromisso = {'data': data, 'hora': hora, 'duracao': duracao, 'descricao': descricao}
        agenda.append(compromisso)
        print("Evento adicionado à agenda com sucesso.")