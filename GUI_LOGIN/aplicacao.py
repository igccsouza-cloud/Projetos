from login_pageFE import *
import login_pageBE as core

app = None

def view_command():
    
    rows = core.view()
    
    app.listClientes.delete(0, END)

    for r in rows:

        app.listClientes.insert(END, r)

def search_command():

    rows = core.search(app.txt_Nome.get(), app.txt_Sobrenome.get(), app.txt_Email.get(), app.txt_CPF.get())

    for r in rows:

        app.listClientes.insert(END, r)

def insert_command():

    core.insert(app.txt_Nome.get(), app.txt_Email.get(), app.txt_CPF.get(), app.txt_Sobrenome.get())
    
    view_command()


def update_command():

    core.update(app.selected_tuple[0], app.txt_Nome.get(), app.txt_Sobrenome.get(), app.txt_Email.get(), app.txt_CPF.get())

    view_command()

def delete_command():

    core.delete(app.selected_tuple[0])

    view_command()

def getSelectedRow(event):
    try:
        index = app.listClientes.curselection()[0]
        app.selected_tuple = app.listClientes.get(index)

        app.ent_Nome.delete(0, END)
        app.ent_Nome.insert(END, app.selected_tuple[1])

        app.ent_Sobrenome.delete(0, END)
        app.ent_Sobrenome.insert(END, app.selected_tuple[2])

        app.ent_Email.delete(0, END)
        app.ent_Email.insert(END, app.selected_tuple[3])

        app.ent_CPF.delete(0, END)
        app.ent_CPF.insert(END, app.selected_tuple[4])

    except IndexError:
        pass

if __name__ == "__main__":

    app = Gui()

    app.listClientes.bind('<<ListboxSelect>>', getSelectedRow)

    app.btn_ViewAll.configure(command=view_command)
    app.btn_Buscar.configure(command=search_command)
    app.btn_Inserir.configure(command=insert_command)
    app.btn_Update.configure(command=update_command)
    app.btn_Del.configure(command=delete_command)
    app.btn_Close.configure(command=app.window.destroy)



    app.run()