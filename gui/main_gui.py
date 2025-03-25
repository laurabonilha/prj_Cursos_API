import customtkinter as ctk
import json
from gui.pages import Pages


class App:
    def __init__(self):
        '''Inicializa a aplicação e configura a janela principal'''

        # Configuração inicial
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Janela principal
        janela = ctk.CTk()
        janela.geometry("400x500")
        janela.title("Menu de Opções")

        pages = Pages(janela)
        pages.mostrar_menu_principal()

    def run(self):
        '''Inicia o loop da interface gráfica'''
        self.janela.mainloop()
        
if __name__ == '__main__':
    app = App()
    app.run()