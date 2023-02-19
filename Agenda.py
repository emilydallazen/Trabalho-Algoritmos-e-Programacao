class Compromisso:
    descricao=''
    data=''
    hora=''
    duracao=''

def Menu():
    print("1 - Incluir \n2- Consultar \n3 - Alterar \n4 - Excluir \n5 - Listar todos \n6 - Sair")
    Menu_Op = int(input(" :"))
    return Menu_Op
    #Variável Menu_Op serve pra armazenar a opção que o usuário quer.
    #E o return Menu_Op faz com que a função retorne o que o usuário escolheu.

def Incluir(l):
    c=Compromisso()
    c.descricao=input('Descrição: ')
    c.data=input('Data (DD/MM/AAAA): ')
    c.hora=input('Hora (HH:MM):')
    c.duracao=input('Duração: ')
    l.append(c)
    

def Consultar(l):
    print('1 - Consular pela data e hora \n2 - Consultar somente pela data')
    Consultar_Op=int(input(": ")) 
    if Consultar_Op == 1:
        Consultar_Data=input('Data: ')
        Consultar_Hora=input('Hora: ')
        #ainda nao sei
    else:
        if Consultar_Op == 2:
            Consultar_Hora=input('Hora: ')

#Programa Principal
agenda=[]
Menu_Op= 10
while Menu_Op!=0:
  Menu_Op=Menu()
  if Menu_Op == 1:
    Incluir(agenda)
  if Menu_Op == 2:
    Consultar(agenda)
       