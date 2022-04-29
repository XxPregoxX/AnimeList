import os
import PySimpleGUI as Sg
from Operations import ReadFile


class MakeReview:

    @staticmethod
    def make_rewiew():
        Sg.theme("Black")
        imput_right_click = ['unused', ['Fechar', 'Voltar', 'Ajuda', 'Renomear']]
        layout = [
                  [Sg.Push(background_color='gray'), Sg.Text("Nota", background_color='black', text_color='white'),
                   Sg.Push(background_color='gray')],
                  [Sg.Push(background_color='gray'), Sg.Input(key='nota', background_color='black',
                                                              size=(4, 1)), Sg.Push(background_color='gray')],
                  [Sg.Text(size=(5, 3), background_color='gray')],
                  [Sg.Push(background_color='gray'), Sg.Text('Status', text_color='white', background_color='black'),
                   Sg.Push(background_color='gray')],
                  [Sg.Push(background_color='gray'), Sg.Input(key="Status", background_color='black', size=10),
                   Sg.Push(background_color='gray')],
                  [Sg.Text(size=(5, 3), background_color='gray')],
                  [Sg.Push(background_color='gray'), Sg.Text('Revisão', background_color='black', text_color='white'),
                   Sg.Push(background_color='gray')],
                  [Sg.MLine(key='avaliação', background_color='black', size=(40, 10), no_scrollbar=True)],
                  [Sg.Button(key='Feito', button_text='Feito', size=(28, 3))]]

        return Sg.Window('', layout, no_titlebar=True, grab_anywhere=False,
                         right_click_menu=imput_right_click, right_click_menu_background_color='white',
                         right_click_menu_text_color='black', size=(270, 540),
                         background_color='gray', transparent_color='gray', finalize=True)

    @staticmethod
    def transition():

        imput_right_click = ['unused', ['Fechar', 'Voltar', 'Ajuda']]

        layin = [[Sg.Push(), Sg.Text("Nome Do Anime"), Sg.Push()],
                 [Sg.Push(), Sg.Input(key='animename', size=(10, 1)), Sg.Push()],
                 [Sg.Push(), Sg.Button('Feito', key='feito'),
                  Sg.Push()]]

        return Sg.Window('', layin, transparent_color='gray', right_click_menu=imput_right_click,
                         finalize=True, no_titlebar=True)


class MainScreen:

    @staticmethod
    def main_screen():
        for _, _, file in os.walk('Animes'):
            pass
        file2 = ' '.join(file).replace('.txt', '').split()
        Sg.theme("Black")
        imput_right_click = ['unused', ['Fechar', 'Ajuda', 'Excluir']]
        layout = [[Sg.LBox(key='arquivo', values=file2, size=(30, 20), no_scrollbar=True, background_color='black')],
                  [Sg.Button('Visualizar'), Sg.Push(background_color='gray'), Sg.Button('Novo Anime')]]

        return Sg.Window('', layout, right_click_menu=imput_right_click, no_titlebar=True, transparent_color='gray',
                         background_color='gray', finalize=True)


class SeeReview:

    def __init__(self, nomedoanime):
        self.nomedoanime = nomedoanime

    def see_review(self):
        o = ReadFile(self.nomedoanime)
        Sg.theme("Black")
        imput_right_click = ['unused', ['Fechar', 'Voltar', 'Ajuda']]
        layout = [[Sg.Text(background_color='gray')],
                  [Sg.Push(background_color='gray'), Sg.Text(text=o.note(), font='Default 100'),
                   Sg.Push(background_color='gray')],
                  [Sg.Text(background_color='gray')],
                  [Sg.Push(background_color='gray'), Sg.Text(text=o.watched(), font='Default 20'),
                   Sg.Push(background_color='gray')],
                  [Sg.Text(background_color='gray')],
                  [Sg.Push(background_color='gray'),
                   Sg.Text(text=o.review(), size=(40, 10)), Sg.Push(background_color='gray')],
                  [Sg.Push(background_color='gray'),
                   Sg.Button('Voltar', size=(17, 3)), Sg.Push(background_color='gray')]]

        return Sg.Window('olosco', layout, right_click_menu=imput_right_click,
                         no_titlebar=True, background_color='gray', transparent_color='gray', finalize=True)
