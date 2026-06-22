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

        self.label_1 = Label(self.frame_1, text="Clinica + Saude", font=("verdana", 21, "bold"), bg="#458b74", fg="white")
       
        self.label_1.place(relx=0.3, rely=0.4)

    def leyout(self):
        self.nome_label = Label(janela, text="NomeCompleto", font=("verdana", 12, "bold"), bg="white")
        self.nome_label.place()

        #self.data_entry = DateEntry(janela, width =12, background="darkblue", foreground="#7fffd4", borderwidth=2, date_pattern='dd/mm/yyyy')
        #self.data_entry.grid()

  
Produto()
    
