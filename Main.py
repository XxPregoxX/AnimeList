from Interface import MakeReview, SeeReview, MainScreen
from Operations import Watched, Note, Review
import os
import PySimpleGUI as Sg
c = MakeReview()
d = MainScreen()

screen1 = d.main_screen()
screen2 = None
screen3 = None
screen4 = None

while True:
    window, event, values = Sg.read_all_windows()
    if event == 'Fechar':
        break
    if window == screen1 and event == 'Excluir' and len(values['arquivo']) > 0:
        strip = (str(values['arquivo']).strip("['']"))
        os.remove(f"Animes/{strip}.txt")
        screen1.hide()
        screen1 = d.main_screen()
    if window == screen1 and event == 'Visualizar' and len(values['arquivo']) > 0:
        arquivo = (str(values['arquivo']).strip("['']"))
        e = SeeReview(arquivo)
        screen1.hide()
        screen2 = e.see_review()
    if window == screen1 and event == 'Novo Anime':
        screen1.hide()
        screen4 = c.transition()
    if window == screen4 and event == 'feito' and len(values['animename']) > 0:
        Animename = values['animename']
        screen4.hide()
        screen3 = c.make_rewiew()
    if window == screen3 and event == 'Feito':
        if len(values['nota']) > 0 and len(values['Status']) > 0 and len(values['avaliação']):
            y = Note(values['nota'], Animename.replace(' ', '-'))
            y.note()
            r = Watched(values['Status'], Animename.replace(' ', '-'))
            r.watched()
            h = Review(values['avaliação'], Animename.replace(' ', '-'))
            h.review()
            screen3.hide()
            screen1 = d.main_screen()

    if window == screen3 and event == 'Voltar':
        screen3.hide()
        tela4 = c.transition()
    if window == screen2 and event == 'Voltar':
        screen2.hide()
        screen1 = d.main_screen()
    if window == screen4 and event == 'Voltar':
        screen4.hide()
        screen1 = d.main_screen()
