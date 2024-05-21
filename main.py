import tkinter as tk
from tkinter import messagebox

def salvar_dados():
    cpf = cpf_entry.get()
    data_nascimento = data_nascimento_entry.get()
    nome_completo = nome_completo_entry.get()
    estado = estado_entry.get()
    cidade = cidade_entry.get()
    bairro = bairro_entry.get()
    rua = rua_entry.get()
    numero = numero_entry.get()
    complemento = complemento_entry.get()
    nome_mae = nome_mae_entry.get()
    nome_pai = nome_pai_entry.get()

    # Aqui você pode adicionar código para salvar os dados, como escrever em um arquivo ou enviar para um banco de dados

    messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")

# Criar a janela principal
root = tk.Tk()
root.title("Cadastro de Pessoa")

# Labels
tk.Label(root, text="CPF:").grid(row=0, column=0, sticky="w")
tk.Label(root, text="Data de Nascimento:").grid(row=1, column=0, sticky="w")
tk.Label(root, text="Nome Completo:").grid(row=2, column=0, sticky="w")
tk.Label(root, text="Estado:").grid(row=3, column=0, sticky="w")
tk.Label(root, text="Cidade:").grid(row=4, column=0, sticky="w")
tk.Label(root, text="Bairro:").grid(row=5, column=0, sticky="w")
tk.Label(root, text="Rua:").grid(row=6, column=0, sticky="w")
tk.Label(root, text="Número:").grid(row=7, column=0, sticky="w")
tk.Label(root, text="Complemento:").grid(row=8, column=0, sticky="w")
tk.Label(root, text="Nome da Mãe:").grid(row=9, column=0, sticky="w")
tk.Label(root, text="Nome do Pai:").grid(row=10, column=0, sticky="w")

# Entradas de texto
cpf_entry = tk.Entry(root)
cpf_entry.grid(row=0, column=1)
data_nascimento_entry = tk.Entry(root)
data_nascimento_entry.grid(row=1, column=1)
nome_completo_entry = tk.Entry(root)
nome_completo_entry.grid(row=2, column=1)
estado_entry = tk.Entry(root)
estado_entry.grid(row=3, column=1)
cidade_entry = tk.Entry(root)
cidade_entry.grid(row=4, column=1)
bairro_entry = tk.Entry(root)
bairro_entry.grid(row=5, column=1)
rua_entry = tk.Entry(root)
rua_entry.grid(row=6, column=1)
numero_entry = tk.Entry(root)
numero_entry.grid(row=7, column=1)
complemento_entry = tk.Entry(root)
complemento_entry.grid(row=8, column=1)
nome_mae_entry = tk.Entry(root)
nome_mae_entry.grid(row=9, column=1)
nome_pai_entry = tk.Entry(root)
nome_pai_entry.grid(row=10, column=1)

# Botão para salvar
salvar_button = tk.Button(root, text="Salvar", command=salvar_dados)
salvar_button.grid(row=11, column=0, columnspan=2, pady=10)

root.mainloop()
