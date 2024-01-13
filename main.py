import flet as ft
from flet import colors
import pyautogui

(screen_width, screen_height) = pyautogui.size()

BUTTON_WIDTH = 800
BUTTON_HEIGHT = 150

def main(page = ft.Page):
    page.bgcolor = '#FAFAFF'
    page.title = 'Jogo da Memória'
    page.window_always_on_top = True
    page.window_width = 1414 #A "width" 1400 não estava sendo mostrada corretamente então foi preciso alterar para 1414.
    page.window_height = 838 #A "height" 800 não estava sendo mostrada corretamente então foi preciso alterar para 838.
    page.window_resizable = False
    page.window_left = (screen_width - page.window_width) / 2
    page.window_top = (screen_height - page.window_height) / 2
    page.padding = 0

    def game(e):
        pass

    def change_button(e):
        if e.data == 'true':
            start_button.content.scale = 5.4
            start_button.width += 15
            start_button.height += 15
            start_button.top = (800 - start_button.height) / 2
            start_button.left = (1400 - start_button.width) / 2
            sombra_grande.opacity = 100
        else:
            start_button.content.scale = 5
            start_button.width -= 15
            start_button.height -= 15
            start_button.top = (800 - BUTTON_HEIGHT) / 2
            start_button.left = (1400 - BUTTON_WIDTH) / 2
            sombra_grande.opacity = 0
        page.update()

    start_button = ft.Container(
        content = ft.Text("Iniciar", color = colors.BLACK, weight=ft.FontWeight.W_700, scale = 5),
        width = BUTTON_WIDTH,
        height = BUTTON_HEIGHT,
        bgcolor = colors.RED_400,
        border_radius = 50,
        alignment = ft.alignment.center,
        top = (800 - BUTTON_HEIGHT) / 2,
        left = (1400 - BUTTON_WIDTH) / 2,
        on_click = game,
        on_hover = change_button
        )

    sombra_grande = ft.Image(
                src = 'Sombra_Grande.png',
                opacity = 0,
                width = 1400,
                height = 800,
                )

    page.add(ft.Stack([ft.Image(
                src = 'Background_Jogo_da_Memoria.png',
                width = 1400,
                height = 800,
                ), 
            sombra_grande,
            start_button])
        )

ft.app(main)
