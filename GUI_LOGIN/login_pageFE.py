from tkinter import *

class Gui():
    
    # Gui stands for Graphical User Interface

    x_pad = 5
    y_pad = 3
    width_entry = 30

    def __init__(self):
        self.window = Tk()
        self.window.wm_title("PYSQL versão 1.0")
        
        self.txt_Nome = StringVar()
        self.txt_Sobrenome = StringVar()
        self.txt_Email = StringVar()
        self.txt_CPF = StringVar()

        self.lbl_Nome = Label(self.window, text="Nome:")
        self.lbl_Sobrenome = Label(self.window, text="Sobrenome:")
        self.lbl_Email = Label(self.window, text="Email:")
        self.lbl_CPF = Label(self.window, text="CPF:")

        self.ent_Nome = Entry(self.window, textvariable=self.txt_Nome, width=self.width_entry)
        self.ent_Sobrenome = Entry(self.window, textvariable=self.txt_Sobrenome, width=self.width_entry)
        self.ent_Email = Entry(self.window, textvariable=self.txt_Email, width=self.width_entry)
        self.ent_CPF = Entry(self.window, textvariable=self.txt_CPF, width=self.width_entry)

        self.listClientes = Listbox(self.window, width=100)
        self.scroll_clientes = Scrollbar(self.window)

        self.btn_ViewAll = Button(self.window, text="Ver todos")
        self.btn_Buscar = Button(self.window, text="Buscar")
        self.btn_Inserir = Button(self.window, text="Inserir")
        self.btn_Update = Button(self.window, text="Atualizar Selecionados")
        self.btn_Del = Button(self.window, text="Deletar Selecionados")
        self.btn_Close = Button(self.window, text="Fechar")
        self.btn_Clear = Button(self.window, text = 'Limpar', command=self.clear_fields)

        self.lbl_Nome.grid(row=0, column=0)
        self.lbl_Sobrenome.grid(row=1, column=0)
        self.lbl_Email.grid(row=2, column=0)
        self.lbl_CPF.grid(row=3, column=0)
        self.ent_Nome.grid(row=0, column=1, padx=50, pady=50)
        self.ent_Sobrenome.grid(row=1, column=1)
        self.ent_Email.grid(row=2, column=1)
        self.ent_CPF.grid(row=3, column=1)
        self.listClientes.grid(row=0, column=2, rowspan=10)
        self.scroll_clientes.grid(row=0, column=2, rowspan=10)
        self.btn_ViewAll.grid(row=4, column=0, columnspan=2)
        self.btn_Buscar.grid(row=5, column=0, columnspan=2)
        self.btn_Inserir.grid(row=6, column=0, columnspan=2)
        self.btn_Update.grid(row=7, column=0, columnspan=2)
        self.btn_Del.grid(row=8, column=0, columnspan=2)
        self.btn_Clear.grid(row=9, column=0, columnspan=2)
        self.btn_Close.grid(row=10, column=0, columnspan=2)

        

        self.listClientes.configure(yscrollcommand=self.scroll_clientes.set)
        self.scroll_clientes.configure(command=self.listClientes.yview)

        for child in self.window.winfo_children():

            widget_class = child.winfo_class()

            if widget_class == 'Button':
                child.grid_configure(sticky = 'WE', padx=self.x_pad, pady=self.y_pad)
            
            elif widget_class == 'Listbox':
                child.grid_configure(sticky = 'NS', padx=self.x_pad, pady=self.y_pad)
            
            elif widget_class == 'Scrollbar':
                child.grid_configure(sticky = 'NS', padx=self.x_pad, pady=self.y_pad)

            else:
                child.grid_configure(padx=self.x_pad, pady=self.y_pad)
    
    def clear_fields(self):
        self.txt_Nome.set("")
        self.txt_Sobrenome.set("")
        self.txt_Email.set("")
        self.txt_CPF.set("")
        self.listClientes.selection_clear(0, END)
        self.selected_tuple = None

    
    def run(self):
        self.window.mainloop()
    
if __name__ == "__main__":
    gui = Gui()
    gui.run()