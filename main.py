from tkinter import*
from tkinter import Tk, StringVar, ttk

#CORES
co0 = "" #preto
co1 = "#FFFFFF" #branco 
co2 = "" #verde 
co3 = "" #valor
co4 = "" #letra
co5 = "" #profit
co6 = "" #azul
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

janela.mainloop()
