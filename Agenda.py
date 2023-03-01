
#Funções auxiliares: criadas para serem utilizadas dentro das funções dos menus.
def linha():
    print(48*'=')

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
       return
    else:
        evento={'data': data, 'hora': hora, 'duracao': duracao, 'descricao': descricao}
        agenda.append(evento)
        print('-----O compromisso foi marcado com sucesso! :)----- ')
        
           

def Consultar():
    if agendaVazia():
       return
    print('1 - Consultar pela data e hora \n2 - Consultar somente pela data')
    Consultar_Op=int(input(": ")) 
    if Consultar_Op == 1:
        Consultar_Data=input('Data: ')
        Consultar_Hora=input('Hora: ')
        achou=False
        for evento in agenda:
            if evento['data'] == Consultar_Data and evento['hora']==Consultar_Hora:
              achou=True
              print(f"Descrição: {evento['descricao']} \nDuração: {evento['duracao']}")
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
print('---------------------AGENDA---------------------')
while True:
    linha()
    print("[1] INCLUIR \n[2] CONSULTAR \n[3] ALTERAR \n[4] EXCLUIR \n[5] LISTAR TODOS \n[6] SAIR")
    linha()
    Menu_Op = int(input(" :"))
    if Menu_Op == 1:
        Incluir()
    elif Menu_Op==2:
        Consultar()
    elif Menu_Op==3:
        Alterar()
    elif Menu_Op == 4:
        Excluir()
    elif Menu_Op==5:
        Listar()
    elif Menu_Op==6:
        break
    else:
        print('Opção inválida!')
        
    
  

       