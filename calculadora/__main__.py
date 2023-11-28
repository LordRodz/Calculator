# Visual da Calculadora ---------------------------------------------

from tkinter import *
from tkinter import messagebox

# Janela Principal ---------------------------------------------------
janela_principal = Tk()
janela_principal.geometry('300x310')
janela_principal.resizable(width=FALSE, height=FALSE)
janela_principal.title('Calculadora')

# Variáveis ----------------------------------------------------------
expressao = fator = ''
input_text = StringVar(value='0')
a = b = 0


# Funções ------------------------------------------------------------
def clique(botao): # botões que escrevem no painel
    global expressao
    expressao = expressao + str(botao)
    input_text.set(expressao)


def clean(): # botão C > limpa tudo
    global expressao, a, fator
    expressao = fator = ''
    a = 0
    input_text.set(value='0')


def limpa_expressao(): # função que limpa o painel da calculadora durante operações
    global expressao
    expressao = ''
    input_text.set(expressao)


def soma():
    global expressao, a, b, fator
    try:
        if a == 0:
            a = int(expressao)
        else:
            b = a
            match fator:
                case 'soma':
                    a = b + int(expressao)
                case 'sub':
                    a = b - int(expressao)
                case 'div':
                    a = b / int(expressao)
                case 'vezes':
                    a = b * int(expressao)
    except ValueError:
        pass
    finally:
        limpa_expressao()
        fator = 'soma'


def sub():
    global expressao, a, b, fator
    try:
        if a == 0:
            a = int(expressao)
        else:
            b = a
            match fator:
                case 'soma':
                    a = b + int(expressao)
                case 'sub':
                    a = b - int(expressao)
                case 'div':
                    a = b / int(expressao)
                case 'vezes':
                    a = b * int(expressao)
    except ValueError:
        pass
    finally:
        fator = 'sub'
        limpa_expressao()


def vezes():
    global expressao, a, b, fator
    try:
        if a == 0:
            a = int(expressao)
        else:
            b = a
            match fator:
                case 'soma':
                    a = b + int(expressao)
                case 'sub':
                    a = b - int(expressao)
                case 'div':
                    a = b / int(expressao)
                case 'vezes':
                    a = b * int(expressao)
    except ValueError:
        pass
    finally:
        limpa_expressao()
        fator = 'vezes'


def div():
    global expressao, a, b, fator
    try:
        if a == 0:
            a = int(expressao)
        else:
            b = a
            match fator:
                case 'soma':
                    a = b + int(expressao)
                case 'sub':
                    a = b - int(expressao)
                case 'vezes':
                    a = b * int(expressao)
                case 'div':
                    a = b / int(expressao)
    except ValueError:
        pass
    finally:
        limpa_expressao()
        fator = 'div'


def igual():
    global expressao, a, fator
    match fator:
        case 'soma':
            try:
                a = a + int(expressao)
            except ValueError:
                a = 0
            finally:
                fator = ''
                limpa_expressao()
                input_text.set(str(a))
        case 'sub':
            try:
                a = a - int(expressao)
            except ValueError:
                a = 0
            finally:
                fator = ''
                limpa_expressao()
                input_text.set(str(a))
        case 'vezes':
            try:
                a = a * int(expressao)
            except ValueError:
                pass
            finally:
                fator = ''
                limpa_expressao()
                input_text.set(str(a))
        case 'div':
            try:
                if a == 0 or expressao == '0':
                    messagebox.showwarning(title='', message='Não é possível dividir por ZERO')
                    clean()
                a = a / int(expressao)
            except ValueError:
                pass
            finally:
                fator = ''
                limpa_expressao()
                input_text.set(str(a))


# Entrada de texto ---------------------------------------------------
painel = Entry(janela_principal, bd=5, relief=GROOVE, border=3, width=21, font='Arial 30', textvariable=input_text)
painel.grid(row=0, column=0, columnspan=100, pady=21)
ent_cima = Label(janela_principal, bg='#86a8e3', anchor=NW, width=100)
ent_cima.place(x=0, y=0)
ent_baixo = Label(janela_principal, bg='#86a8e3', anchor=NW, width=100)
ent_baixo.place(x=0, y=72)

# Gerando botões -----------------------------------------------------
botao1 = Button(janela_principal, text='1', width=5, height=2, command=lambda: clique('1'))
botao1.grid(row=1, column=0)
botao2 = Button(janela_principal, text='2', width=5, height=2, command=lambda: clique('2'))
botao2.grid(row=1, column=1)
botao3 = Button(janela_principal, text='3', width=5, height=2, command=lambda: clique('3'))
botao3.grid(row=1, column=2)
botao4 = Button(janela_principal, text='4', width=5, height=2, command=lambda: clique('4'))
botao4.grid(row=2, column=0)
botao5 = Button(janela_principal, text='5', width=5, height=2, command=lambda: clique('5'))
botao5.grid(row=2, column=1)
botao6 = Button(janela_principal, text='6', width=5, height=2, command=lambda: clique('6'))
botao6.grid(row=2, column=2)
botao7 = Button(janela_principal, text='7', width=5, height=2, command=lambda: clique('7'))
botao7.grid(row=3, column=0)
botao8 = Button(janela_principal, text='8', width=5, height=2, command=lambda: clique('8'))
botao8.grid(row=3, column=1)
botao9 = Button(janela_principal, text='9', width=5, height=2, command=lambda: clique('9'))
botao9.grid(row=3, column=2)
botao0 = Button(janela_principal, text='0', width=5, height=2, command=lambda: clique('0'))
botao0.grid(row=4, column=0)
botaoIGUAL = Button(janela_principal, text='=', width=12, height=2, command=igual)
botaoIGUAL.grid(row=4, column=1, columnspan=2)
botaoSOMA = Button(janela_principal, text='+', width=5, height=2, command=soma)
botaoSOMA.grid(row=4, column=3)
botaoSUB = Button(janela_principal, text='-', width=5, height=2, command=sub)
botaoSUB.grid(row=3, column=3)
botaoVEZES = Button(janela_principal, text='*', width=5, height=2, command=vezes)
botaoVEZES.grid(row=2, column=3)
botaoDIV = Button(janela_principal, text='/', width=5, height=2, command=div)
botaoDIV.grid(row=1, column=3)
botaoLIMPA = Button(janela_principal, text='C', width=5, height=2, command=clean)
botaoLIMPA.grid(row=5, column=0)

janela_principal.mainloop()
