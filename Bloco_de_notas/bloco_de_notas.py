# Bloco de Notas - Programa em Python com Tkinter e desenvolvido por KaelxDev

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

class BlocoDeNotas:
    def __init__(self, root):
        self.root = root
        self.root.title("Bloco de Notas - Sem Título")
        self.root.geometry("800x600")

# Variável para guardar o caminho do arquivo atual
        self.caminho_arquivo = None

# Cria a área de texto com barra de rolagem
        self.area_texto = scrolledtext.ScrolledText(
            self.root, 
            wrap=tk.WORD, 
            font=("Arial", 12),
            bg="#ffffff",
            fg="#000000"
        )
        self.area_texto.pack(fill=tk.BOTH, expand=True)

# Cria o menu
        self.criar_menu()

# Atalhos do teclado
        self.root.bind("<Control-n>", lambda e: self.novo_arquivo())
        self.root.bind("<Control-o>", lambda e: self.abrir_arquivo())
        self.root.bind("<Control-s>", lambda e: self.salvar_arquivo())
        self.root.bind("<Control-a>", lambda e: self.selecionar_tudo())

# Criação do menu

    def criar_menu(self):
        barra_menu = tk.Menu(self.root)
        
# Menu Arquivo
        menu_arquivo = tk.Menu(barra_menu, tearoff=0)
        menu_arquivo.add_command(label="Novo (Ctrl+N)", command=self.novo_arquivo)
        menu_arquivo.add_command(label="Abrir... (Ctrl+O)", command=self.abrir_arquivo)
        menu_arquivo.add_separator()
        menu_arquivo.add_command(label="Salvar (Ctrl+S)", command=self.salvar_arquivo)
        menu_arquivo.add_command(label="Salvar Como...", command=self.salvar_como)
        menu_arquivo.add_separator()
        menu_arquivo.add_command(label="Sair", command=self.sair)
        barra_menu.add_cascade(label="Arquivo", menu=menu_arquivo)

# Menu Editar
        menu_editar = tk.Menu(barra_menu, tearoff=0)
        menu_editar.add_command(label="Recortar (Ctrl+X)", command=lambda: self.area_texto.event_generate("<<Cut>>"))
        menu_editar.add_command(label="Copiar (Ctrl+C)", command=lambda: self.area_texto.event_generate("<<Copy>>"))
        menu_editar.add_command(label="Colar (Ctrl+V)", command=lambda: self.area_texto.event_generate("<<Paste>>"))
        menu_editar.add_separator()
        menu_editar.add_command(label="Selecionar Tudo (Ctrl+A)", command=self.selecionar_tudo)
        barra_menu.add_cascade(label="Editar", menu=menu_editar)

# Menu Ajuda

        menu_ajuda = tk.Menu(barra_menu, tearoff=0)
        menu_ajuda.add_command(label="Sobre", command=self.sobre)
        barra_menu.add_cascade(label="Ajuda", menu=menu_ajuda)

        self.root.config(menu=barra_menu)

# Funções do Bloco de Notas

    def novo_arquivo(self):
        # Limpa a área de texto
        self.area_texto.delete(1.0, tk.END)
        self.caminho_arquivo = None
        self.root.title("Bloco de Notas - Sem Título")

    def abrir_arquivo(self):
        caminho = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Arquivos de Texto", "*.txt"), ("Todos os Arquivos", "*.*")]
        )
        if caminho:
            try:
                with open(caminho, "r", encoding="utf-8") as arquivo:
                    conteudo = arquivo.read()
                self.area_texto.delete(1.0, tk.END)
                self.area_texto.insert(1.0, conteudo)
                self.caminho_arquivo = caminho
                self.root.title(f"Bloco de Notas - {caminho}")
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível abrir o arquivo.\nErro: {e}")

# Salvar o arquivo atual

    def salvar_arquivo(self):
        if self.caminho_arquivo:
            try:
                conteudo = self.area_texto.get(1.0, tk.END)
                with open(self.caminho_arquivo, "w", encoding="utf-8") as arquivo:
                    arquivo.write(conteudo)
                messagebox.showinfo("Sucesso", "Arquivo salvo com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível salvar o arquivo.\nErro: {e}")
        else:
            self.salvar_como()

    def salvar_como(self):
        caminho = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Arquivos de Texto", "*.txt"), ("Todos os Arquivos", "*.*")],
            title="Salvar Como"
        )
        if caminho:
            try:
                conteudo = self.area_texto.get(1.0, tk.END)
                with open(caminho, "w", encoding="utf-8") as arquivo:
                    arquivo.write(conteudo)
                self.caminho_arquivo = caminho
                self.root.title(f"Bloco de Notas - {caminho}")
                messagebox.showinfo("Sucesso", "Arquivo salvo com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível salvar o arquivo.\nErro: {e}")

    def selecionar_tudo(self):
        self.area_texto.tag_add(tk.SEL, "1.0", tk.END)
        self.area_texto.mark_set(tk.INSERT, "1.0")
        self.area_texto.see(tk.INSERT)

    def sobre(self):
        messagebox.showinfo("Sobre", "Bloco de Notas\nDesenvolvido por KaelxDev e criado em Python com Tkinter.\nVersão 1.0")

    def sair(self):
        if messagebox.askokcancel("Sair", "Deseja realmente sair?"):
            self.root.destroy()

# Executa o aplicativo
if __name__ == "__main__":
    root = tk.Tk()
    app = BlocoDeNotas(root)
    root.mainloop()