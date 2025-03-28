'''
Arquivo para organização de todas as telas da aplicação 
'''

import customtkinter as ctk
# Importando as funções de request da API
from services.crud import adicionar_curso, obter_cursos, excluir_curso, atualizar_curso
# Importando os elementos comuns de interface gráfica
from gui.componentes import create_button, create_entry, create_label


class Pages:
    def __init__(self, root):
        '''Inicializa a classe Pages com a referência da janela principal'''
        self.root = root
        self.frame_atual = None #Variável para armazenar o frame ativo
        
    def limpar_tela(self):
        '''Remove o frame atual antes de carregar uma nova tela'''
        if self.frame_atual:
            self.frame_atual.destroy()
            
    def mostrar_menu_principal(self):
        '''Ativa o menu principal'''
        self.limpar_tela()
        tela_menu = ctk.CTkFrame(self.root)
        tela_menu.pack(fill='both', expand=True, padx=20, pady=20)
        self.frame_atual = tela_menu
        botao_adicionar = ctk.CTkButton(tela_menu, text="Adicionar Curso")
        

        botao_ver = ctk.CTkButton(tela_menu, text="Ver Cursos", command=self.abrir_tela_ver_cursos)
        botao_ver.pack(pady=20)

        botao_modificar = ctk.CTkButton(tela_menu, text="Modificar Curso")
        botao_modificar.pack(pady=20)

        botao_excluir = ctk.CTkButton(tela_menu, text="Excluir Curso")
        botao_excluir.pack(pady=20)


    def abrir_tela_ver_cursos(self):
        '''Tela para visualizar todos os cursos cadastrados'''
        # Limpando a tela principal
        self.limpar_tela()
        #Abrindo aidiconar cursos na janela principal
        tela_ver_cursos = ctk.CTkFrame(self.root)
        tela_ver_cursos.pack(fill='both', expand=True, padx=20, pady=20)
        self.frame_atual = tela_ver_cursos
        create_label(parent=tela_ver_cursos, text='Todos os cursos cadastrados')
        
        retorno_cursos = obter_cursos() #Retorno em forma de dicionário
        
        # Imprimindo todos os cursos, com título, horas e aulas
        for curso in retorno_cursos:
            create_label(parent=tela_ver_cursos, text=f"Título: {curso['titulo']} \n Aulas: {curso['aulas']} \n Horas {curso['horas']}")
            
        botao_voltar = create_button(tela_ver_cursos, text='Voltar', command=self.mostrar_menu_principal)
    
    
    
    
    
    
    
    
    