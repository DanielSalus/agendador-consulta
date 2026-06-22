from tkinter import*
from tkcalendar import DateEntry
janela = Tk()
class Produto:
    def __init__(self):
        self.janela = janela
        self.tela()
        self.leyout()
        janela.mainloop()

    def tela(self):
        janela.geometry("800x600")
        janela.config(bg="white")
        janela.title("cadastro paciente")
        #janela.resizable(False, False)

        self.frame_1 = Frame(janela, width=800, height=100, bg="#458b74",)
        self.frame_1.place(relx=0.0, rely=0.0)

        self.label_1 = Label(self.frame_1, text="Clínica + Saúde", font=("verdana", 21, "bold"), bg="#458b74", fg="white")
       
        self.label_1.place(relx=0.3, rely=0.4)

    def leyout(self):
        self.nome_label = Label(janela, text="NomeCompleto*", font=("verdana", 12, "bold"), bg="white")
        self.nome_label.place(relx=0.0, rely=0.2)

        self.nome_entry= Entry(janela, bg="#7fffd4")
        self.nome_entry.place(relx=0.2, rely=0.2, relwidth=0.5)

        self.email_label = Label(janela, text="Email*", font=("verdana", 12, "bold"))
        self.email_label.place(relx=0.0, rely=0.3)

        self.email_entry= Entry(janela, bg="#7fffd4")
        self.email_entry.place(relx=0.1, rely=0.3, relwidth=0.4)

        self.telefone_label = Label(janela, text="Telefone*",  font=("verdana", 12, "bold"), bg="white" )
        self.telefone_label.place(relx= 0.52, rely=0.3)

        self.telefone_entry = Entry(janela, bg="#7fffd4" )
        self.telefone_entry.place(relx=0.64, rely=0.3, relwidth=0.2)

        self.cpf_label = Label(janela, text="CPF*", font=("verdana", 12, "bold"), bg="white")
        self.cpf_label.place(relx=0.0, rely=0.4)

        self.cpf_entry = Entry(janela, bg="#7fffd4" )
        self.cpf_entry.place(relx=0.1, rely=0.4, relwidth=0.2)

        self.cpf_label = Label(janela, text="CPF*", font=("verdana", 12, "bold"), bg="white")
        self.cpf_label.place(relx=0.0, rely=0.4)
        
        self.cpf_entry = Entry(janela, bg="#7fffd4" )
        self.cpf_entry.place(relx=0.1, rely=0.4, relwidth=0.2)

        self.rg_label = Label(janela, text="RG*",  font=("verdana", 12, "bold"), bg="white" )
        self.rg_label.place(relx=0.32, rely=0.4, )

        self.rg_entry = Entry(janela, bg="#7fffd4")
        self.rg_entry.place(relx=0.38, rely=0.4, relwidth=0.18)

        self.dataNasc_label = Label(janela, text="DataNascimento*",  font=("verdana", 12, "bold"), bg="white"  )
        self.dataNasc_label.place(relx=0.57, rely=0.4)

        self.dataNasc_entry = DateEntry(janela, width =12, background="#7fffd4", foreground="black",borderwidth=2, date_pattern='dd/mm/yyyy')
        self.dataNasc_entry.place(relx=0.78, rely=0.4)

  
Produto()
    
