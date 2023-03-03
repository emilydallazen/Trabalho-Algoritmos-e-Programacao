
#Funções auxiliares: criadas para serem utilizadas dentro das funções dos menus.
def linha():
    print(50*'=')

#adicionado no início de todas as funções do menu, com exceção da função Incluir.
def agendaVazia():
   if len(agenda)==0:
        print('Zero compromissos. Sua agenda está vazia!')
        return True
   return False

#usada dentro da funçao Incluir
def verificaAgenda(listaAgenda, data, hora):
   for evento in listaAgenda:
        if evento['data'] == data and evento['hora']==hora:
            return True
   return False
      
   
#Funções Principais: função de cada opção do menu.

def Incluir():
    descricao=input('Descrição: ')
    data=input('Data (DD/MM/AAAA): ')
    hora=input('Hora (HH:MM):')
    duracao=input('Duração: ')
    if verificaAgenda(agenda, data, hora):
       print('------Ops, voce já tem compromisso!----')
       print('')
       return
    #se a função verificaAgenda retornar como True, é porque já existe um compromisso na mesma data e hora. Então não será dado o append do compromisso na lista da agenda.
    else:
        evento={'data': data, 'hora': hora, 'duracao': duracao, 'descricao': descricao}
        #definindo o dicionário Evento, composto por data, hora, duração e descrição.
        agenda.append(evento) #inserindo o evento na agenda.
        print('O compromisso foi marcado com sucesso! :) ')
        print('')
        
           

def Consultar():
    if agendaVazia():
       return
    print('1 - Consultar pela data e hora \n2 - Consultar somente pela data')
    Consultar_Op=int(input(" : ")) 
    if Consultar_Op == 1:
        Consultar_Data=input('Data: ')
        Consultar_Hora=input('Hora: ')
        achou=False
        for evento in agenda:
            if evento['data'] == Consultar_Data and evento['hora']==Consultar_Hora:
              achou=True
              print(f"Descrição: {evento['descricao']} \nDuração: {evento['duracao']}")
              linha()
              break
        if achou == False:
              print('Nenhum compromisso encontrado :(')
              print('')
              
    if Consultar_Op == 2:
            Consultar_Data=input('Data: ')
            achou=False
            for evento in agenda:
                if evento['data']==Consultar_Data:
                    achou=True
                    print(f"Descrição: {evento['descricao']} \nHora: {evento['hora']} \nDuração: {evento['duracao']}")
                    linha()
            if achou==False:
                print('Nenhum compromisso encontrado! :( ')
                print('')


def Alterar():
    if agendaVazia():
        return
    print('Digite as informações do evento que deseja alterar: ')
    Alterar_Data=input('Data: ')
    Alterar_Hora=input('Hora:')
    achou=False
    for evento in agenda:
        if evento['data']==Alterar_Data and evento['hora']==Alterar_Hora:
            achou=True
            linha()
            new_descricao=input('Digite a nova descrição: ')
            new_duracao=input('Nova duração: ')
            evento['descricao']=new_descricao
            evento['duracao']=new_duracao
            print('O compromisso foi alterado com sucesso!!!')
            print('')
            break
    if achou==False:
        print('Não encontrei esse compromisso :( ')
        print('')
        
    
def Excluir():
    if agendaVazia():
        return
    print('Digite as informações do evento que deseja excluir: ')
    Exclui_Data=input('Data: ')
    Exclui_Hora=input('Hora:')
    print('')
    indice=None
    achou=False
    for i, evento in enumerate(agenda):
        if evento['data']==Exclui_Data and evento['hora']==Exclui_Hora:
            indice=i
            achou=True
            
    if indice is not None:
            agenda.pop(indice)    
            print("O compromisso foi excluído da sua agenda com sucesso!")
            print('')
            return
    if achou==False:
        print('Não encontrei esse compromisso :( ')
        print('')
    
def Listar():
    if agendaVazia():
        return
    else:
        for evento in agenda:
           linha()
           print(f"Descrição: {evento['descricao']} \nData: {evento['data']} \nHora: {evento['hora']} \nDuração: {evento['duracao']}") 
           linha()

  
#Programa Principal

agenda=[]
print('----------------------AGENDA----------------------')
while True:
    linha()
    print("[1] INCLUIR \n[2] CONSULTAR \n[3] ALTERAR \n[4] EXCLUIR \n[5] LISTAR TODOS \n[6] SAIR")
    linha()
    Menu_Op = input(" : ")
    linha()
    if Menu_Op == '1':
        Incluir()
    elif Menu_Op=='2':
        Consultar()
    elif Menu_Op=='3':
        Alterar()
    elif Menu_Op == '4':
        Excluir()
    elif Menu_Op=='5':
        Listar()
    elif Menu_Op=='6':
        break
    else:
        print('Opção inválida!')
print('************************FIM***********************')    
  

       