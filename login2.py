from tkinter import *
from csv import *
import random
import string

janelaL = Tk() #janela login


janelaL.geometry("300x180")

janelaL.configure(bg='#6495ED')
 


janelaL.title("Login")



nome = Label(janelaL, text="Nome:", font="10", bg='#6495ED')
nome.place(x=50, y=0)



senhaL = Label(janelaL, text="Senha:", font="10", bg='#6495ED')
senhaL.place(x=50, y=30)



nomeE = Entry(janelaL, bg='#D3D3D3')
nomeE.place(x=110, y=3)



senhaE = Entry(janelaL, bg='#D3D3D3')
senhaE.place(x=110, y=33)


global nome2
global senha2

def TelaGerador():
    global nome2
    global senha
    global entrad
    global plat

    janelaG = Toplevel(janelaL)

    janelaG.geometry("400x200")



    janelaG.title("Gerador de senhas")

    janelaG.configure(bg='#DCDCDC')


    txt1 = Label(janelaG, bg='#DCDCDC', text = "quantidade de digitos da sua senha:", font="55")
    txt1.place(x=10, y=10)

    entrad = Entry(janelaG, bg='#D3D3D3', width=20)
    entrad.place(x=270, y=14)

    us = Label(janelaG, bg='#DCDCDC', text = "que plataforma vai ser a sua senha?:", font="55")
    us.place(x=10, y=40)


    a = list(range(1, 21))

    senha = Label(janelaG, bg='#DCDCDC', font="90")
    senha.place(x=180, y=80)

    

    print = "sinto muito mas esse progama so\nsuporta senhas de ate 20 digitos"

    


    botão = Button(janelaG, bg='#D3D3D3', text = "Gerar Senha", width=10, font=50, command=gerarS)
    botão.place(x=155, y=114)

    plat = Entry(janelaG, bg='#D3D3D3', width=20) #ultilidade da senha
    plat.place(x=270, y=43)
    botaoS = Button(janelaG, text="ver suas senhas salvas", command=listarS, bg="#D3D3D3")
    botaoS.place(x=142, y=155)



def limparS():
    with open("suas_senha.csv", "w", newline='')as file:
        file.write('')



def listarS():
    global plat
    global nome2
    global senha

    janelaS = Toplevel(janelaL)
    janelaS.geometry("370x150")

    janelaS.configure(bg="#A9A9A9")

    janelaS.title("Suas Senhas")

    plataforma1 = Label(janelaS, text="googleeee", font="60", bg="#A9A9A9", width="20")
    plataforma1.grid(column=0, row=0)


    plataforma2 = Label(janelaS, text="", font='60', bg="#A9A9A9", width="20")
    plataforma2.grid(column=0, row=1)
    #paltaforma2.place(x=10, y=35)

    plataforma3 = Label(janelaS, text="", font='60', bg="#A9A9A9", width="20")
    plataforma3.grid(column=0, row=2)
    #paltaforma3.place(x=10, y=60)

    plataforma4 = Label(janelaS, text="", font='60', bg="#A9A9A9", width="20")
    plataforma4.grid(column=0, row=3)
    #plataforma4.place(x=10, y=85)

    paltaforma5 = Label(janelaS, text="", font='60', bg="#A9A9A9", width="20")
    paltaforma5.grid(column=0, row=4)
    #paltaforma5.place(x=10, y=110)

    senhas1 = Label(janelaS, text="", font='60', bg="#A9A9A9", width="20")
    senhas1.grid(column=1, row=0)
    #senhas1.place(x=50, y=10)

    senhas2 = Label(janelaS, text="", font='60', bg="#A9A9A9", width="20")
    senhas2.grid(column=1, row=1)
    #senhas2.place(x=50, y=35)

    senhas3 = Label(janelaS, text="", font='60', bg="#A9A9A9", width="20")
    senhas3.grid(column=1, row=2)
    #senhas3.place(x=50, y=60)

    senhas4 = Label(janelaS, text="", font='60', bg="#A9A9A9", width="20")
    senhas4.grid(column=1, row=3)
    #senhas4.place(x=50, y=85)

    senhas5 = Label(janelaS, text="", font='60', bg="#A9A9A9", width="20")
    senhas5.grid(column=1, row=4)
    #senhas5.place(x=50, y=110)

    limparSb = Button(janelaS, text="limpar senhas", command=limparS)
    limparSb.grid(column=1, row=5)

    lista_plataforma = ["","","","",""]

    lista_senhas = ["","","","",""]


    with open("suas_senha.csv", "r", newline='')as file:
        verNome = reader(file)
        i = 0
        for row in verNome:
            print(row[2])
            if (nome2 == row[2]):
                if (i > 4):
                    break
                lista_plataforma.insert(i, row[0])
                lista_senhas.insert(i, row[1])
                i = i + 1
    plataforma1.configure(text=lista_plataforma[0])
    plataforma2.configure(text=lista_plataforma[1])
    plataforma3.configure(text=lista_plataforma[2])
    plataforma4.configure(text=lista_plataforma[3])
    paltaforma5.configure(text=lista_plataforma[4])
    senhas1.configure(text=lista_senhas[0])
    senhas2.configure(text=lista_senhas[1])
    senhas3.configure(text=lista_senhas[2])
    senhas4.configure(text=lista_senhas[3])
    senhas5.configure(text=lista_senhas[4])
    

def aviso():
    janelaA = Toplevel(janelaL)

    janelaA.configure(bg='#DCDCDC')

    janelaA.geometry("430x150")

    aviso = Label(janelaA, bg='#DCDCDC', font="30", text="esse programa está na vessão beta no momento\npor isso é possível salvar até 5 senhas para que a execução do\nnosso sistema ocorra bem")
    aviso.place(x=5, y=10)

    botão = Button(janelaA, text="Continuar", font="50", command=TelaGerador, bg='#696969')
    botão.place(x=175, y=80)





def gerarS():
        global nome2
        global senha2
        global senha
        global entrad
        global plat

        conteudo = int(entrad.get())
        plataforma = plat.get()
        print(nome2)
        if(conteudo <= 20):
            letters = string.ascii_letters
            res = ''.join(random.choice(letters) for i in range(conteudo))
            senha.config(text = str(res))

            c = [plataforma, str(res), nome2]

            with open("suas_senha.csv", "a", newline='')as file:
                salvarS = writer(file)
                salvarS.writerow(c)
            
        else:
            senha.config(text = print)
global l
def cadastrar():
    global l
    global nome2
    global senha2

    nome2 = nomeE.get()
    senha2 = senhaE.get()

    with open("dados_l.csv", "r") as file:
        cs_reader = reader(file)
        for row in cs_reader:
            if nome2 == row[0]:
                l.configure(text="")
                l.configure(text="nome ja cadastrado")
                return  
            
    with open("dados_l.csv", "a", newline='')as file:
        Writer = writer(file)
        if(len(senha2) <= 7):
            l.configure(text="")
            l.configure(text="senha deve ter no\nmínimo 8 digitos")
        
        else:
            l.configure(text="")
            l.configure(text="bem vindo", font="80", fg='#00FF00')
            Writer.writerow([nome2, senha2])
            aviso()

        

        
    
    


botãoC = Button(janelaL, text = 'cadastrar', font="70", command=cadastrar, bg='#D3D3D3')
botãoC.place(x=110, y=70)

    
def entrar():
    global l
    global nome2
    global senha2
    nome2 = nomeE.get()
    senha2 = senhaE.get()

    with open("dados_l.csv", "r") as file:
        cs_reader = reader(file)
        for row in cs_reader:
            if((nome2 == row[0]) and (senha2 == row[1])):
                l.configure(text="")
                l.configure(text="bem vindo de volta", bg="#6495ED", fg='#00FF00')
                aviso()
                return
            
    l.configure(text="")       
    l.configure(text="senha ou nome incorreto", bg="#6495ED", fg='#FF0000')


l = Label(janelaL, font="50", fg="#FF0000", bg='#6495ED', anchor="center")
l.place(x=75, y=135)
botãoE = Button(janelaL, text = 'entrar', font="100", command=entrar, bg='#D3D3D3')
botãoE.place(x=120, y=105)



janelaL.mainloop()