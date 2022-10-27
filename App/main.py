
from asyncio.windows_events import NULL
from email.mime import image
from threading import local
from tkinter import *
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
from webbrowser import BackgroundBrowser
from PIL import ImageTk, Image
from tkcalendar import Calendar, DateEntry
from datetime import date
from tkinter import filedialog as fd
#importando viwes
from view import *


#CORES
co0 = "#000000" #preto
co1 = "#FFFFFF" #branco 
co2 = "#32CD32" #verde 
co3 = "#DAA520" #amarelo
co4 = "#000000" #letra
co5 = "" #profit
co6 = "#1E90FF" #azul
co7 = "" #verde
co8 = "" #+verde
co9 = "#DCDCDC" #cinza de fundo

#JANELA
janela = Tk()
janela.title('')
janela.geometry('900x600')
janela.configure(background= co9)
janela.resizable(width=False, height=False)

#estilo
estilo = ttk.Style(janela)
estilo.theme_use('clam')

FrameTopo = Frame(janela, width=1043, height=50,bg=co1, relief=FLAT)
FrameTopo.grid(row=0,column=0)

FrameMeio = Frame(janela, width=1043, height=303, bg=co1,pady=20, relief=FLAT)
FrameMeio.grid(row=1,column=0,pady=1, padx=0,sticky=NSEW)

FrameBaixo = Frame(janela, width=1043, height=300, bg=co1, relief=FLAT)
FrameBaixo.grid(row=2,column=0,pady=0, padx=1,sticky=NSEW)

#Funções
global tree
#func inserir
def inserir():
    global imagem, imagem_string, l_imagem

    nome = e_nome.get()
    local = e_area.get()
    descricao = e_des.get()
    marca = e_model.get()
    data_da_compra = e_data.get()
    valor_da_compra = e_vl_compra.get()
    serie = e_serie.get()
    imagem = imagem_string

    lista_inserir = [nome,local,descricao,marca,data_da_compra,valor_da_compra,serie,imagem]

    for i in lista_inserir:
        if i == '':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
    
    inserir_form(lista_inserir)
    messagebox.showinfo('Sucesso!','Item adicionado')

    e_nome.delete(0,'end')
    e_area.delete(0,'end')
    e_des.delete(0,'end')
    e_model.delete(0,'end')
    e_data.delete(0,'end')
    e_vl_compra.delete(0,'end')
    e_serie.delete(0,'end')


    mostrar()

#Func escolher imagem
global imagem, imagem_string, l_imagem
def escolher_imagem():
    global imagem, imagem_string, l_imagem
    imagem = fd.askopenfilename()
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((170,170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(FrameMeio, image=imagem, bg=co1, fg=co0)
    l_imagem.place(x=700,y=10)


#Imagem
app_img = Image.open('icone_main.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(FrameTopo, image=app_img, text=' Inventário do doméstico', width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co0)
app_logo.place(x=0,y=0)

#inputs
#Nome
l_nome = Label(FrameMeio, text='Nome', height=1, anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co0)
l_nome.place(x=10,y=10)
e_nome = Entry(FrameMeio, width=30, justify='left', relief=SOLID)
e_nome.place(x=130,y=11)

#Área
l_area = Label(FrameMeio, text='Área', height=1, anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co0)
l_area.place(x=10,y=40)
e_area = Entry(FrameMeio, width=30, justify='left', relief=SOLID)
e_area.place(x=130,y=41)

#Descrição
l_des = Label(FrameMeio, text='Descrição', height=1, anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co0)
l_des.place(x=10,y=70)
e_des = Entry(FrameMeio, width=30, justify='left', relief=SOLID)
e_des.place(x=130,y=71)

#Marca/Modelo
l_model = Label(FrameMeio, text='Marca/Modelo', height=1, anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co0)
l_model.place(x=10,y=100)
e_model = Entry(FrameMeio, width=30, justify='left', relief=SOLID)
e_model.place(x=130,y=101)

#Data da compra
l_data = Label(FrameMeio, text='Data da compra', height=1, anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co0)
l_data.place(x=10,y=130)
e_data = DateEntry(FrameMeio, width=12,Background= 'darkblue',bordewidth=2, year= 2022)
e_data.place(x=130,y=131)

#Valor da compra
l_vl_compra = Label(FrameMeio, text='Valor da compra', height=1, anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co0)
l_vl_compra.place(x=10,y=160)
e_vl_compra = Entry(FrameMeio, width=30, justify='left', relief=SOLID)
e_vl_compra.place(x=130,y=161)

#Número de série
l_serie = Label(FrameMeio, text='Número de série', height=1, anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co0)
l_serie.place(x=10,y=190)
e_serie = Entry(FrameMeio, width=30, justify='left', relief=SOLID)
e_serie.place(x=130,y=191)

#Botões
#Carregar
l_imagem = Label(FrameMeio, text='Imagem do item', height=1, anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co0)
l_imagem.place(x=10,y=220)
b_carregar = Button(FrameMeio,command=escolher_imagem,width=30, overrelief=RIDGE,text='CARREGAR',compound=CENTER, anchor=CENTER, font=('Ivy 8'), bg=co1, fg=co0)
b_carregar.place(x=130,y=221)

#Adicionar
img_add = Image.open('icone_add.png')
img_add = img_add.resize((20,20))
img_add = ImageTk.PhotoImage(img_add)

b_add = Button(FrameMeio,image=img_add,command=inserir  ,width=95, overrelief=RIDGE,text='  ADICIONAR',compound=LEFT, anchor=NW, font=('Ivy 8'), bg=co1, fg=co0)
b_add.place(x=330,y=10)

#Atualizar
img_att = Image.open('icone_atualizar.png')
img_att = img_att.resize((20,20))
img_att = ImageTk.PhotoImage(img_att)

b_att = Button(FrameMeio,image=img_att, width=95, overrelief=RIDGE,text='  ATUALIAZAR',compound=LEFT, anchor=NW, font=('Ivy 8'), bg=co1, fg=co0)
b_att.place(x=330,y=50)

#Excluir
img_del = Image.open('icone_del.png')
img_del = img_del.resize((20,20))
img_del = ImageTk.PhotoImage(img_del)

b_del = Button(FrameMeio,image=img_del, width=95, overrelief=RIDGE,text='  DELETAR',compound=LEFT, anchor=NW, font=('Ivy 8'), bg=co1, fg=co0)
b_del.place(x=330,y=90)

#Ver item
img_ver_item = Image.open('icone_itens.png')
img_ver_item = img_ver_item.resize((20,20))
img_ver_item = ImageTk.PhotoImage(img_ver_item)

b_del = Button(FrameMeio,image=img_ver_item, width=95, overrelief=RIDGE,text='  VER ITENS',compound=LEFT, anchor=NW, font=('Ivy 8'), bg=co1, fg=co0)
b_del.place(x=330,y=220)

#Dashboard
#valores
l_total = Label(FrameMeio, text='',width=14, height=2, anchor=CENTER,font=('Ivy 17 bold'), bg=co6, fg=co1)
l_total.place(x=450,y=17)
l_total_titulo = Label(FrameMeio, text='   Valor total de todos os itens  ', height=1, anchor=NW,font=('Ivy 10 bold'), bg=co6, fg=co1)
l_total_titulo.place(x=450,y=12)

#Quantidade
l_qtd = Label(FrameMeio, text='',width=14, height=3, anchor=CENTER,font=('Ivy 17 bold'), bg=co6, fg=co1)
l_qtd.place(x=450,y=90)
l_total_titulo = Label(FrameMeio, text='   Quantidade total de itens', height=1, anchor=NW,font=('Ivy 10 bold'), bg=co6, fg=co1)
l_total_titulo.place(x=450,y=92)

#Label baixo
#tabela
def mostrar():   
    tabela_head = ['#Item','Nome',  'Área','Descrição', 'Marca/Modelo', 'Data da compra','Valor da compra', 'Número de série']

    lista_itens = select_form()


    tree = ttk.Treeview(FrameBaixo, selectmode="extended",columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(FrameBaixo, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(FrameBaixo, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    FrameBaixo.grid_rowconfigure(0, weight=12)

    hd=["center","center","center","center","center","center","center", 'center']
    h=[40,150,100,160,130,100,100, 100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1


    # inserindo os itens dentro da tabela
    for item in lista_itens:
        tree.insert('', 'end', values=item)


    quantidade = [0000,00]
    quantidade_itens = []

    for iten in lista_itens:
        quantidade.append(iten[6])
        quantidade_itens.append(item[0])

    Total_valor = sum(quantidade)
    Total_itens = len(quantidade_itens)

    l_total['text'] = 'R$ {:,.2f}'.format(Total_valor)
    l_qtd['text'] = Total_itens


mostrar()

janela.mainloop()