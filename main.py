import flet as ft
from flet import colors
import time
import random
import pyautogui

BUTTON_WIDTH = 800
BUTTON_HEIGHT = 150

def main(page = ft.Page):
    page.bgcolor = '#FAFAFF'
    page.title = 'Jogo da Memória'
    page.window_width = 1414
    page.window_height = 838
    page.window_resizable = False
    page.window_minimizable = True
    page.window_maximizable = False
    page.window_center()
    page.padding = 0

    def game(e):
        page.remove(pagina_inicial)

        def voltar(e):
            page.add(pagina_inicial)
            start_button.content.content.scale = 5
            start_button.content.width = BUTTON_WIDTH
            start_button.content.height = BUTTON_HEIGHT
            sombra_grande.visible = False
            page.remove(pagina_jogo)

        def mudar_voltar_botao(e):
            if e.data == 'true':
                voltar_botao.content.content.scale = 1.4
                voltar_botao.content.width += 7
                voltar_botao.content.height += 7
                voltar_botao.padding = 16.5
            else:
                voltar_botao.content.content.scale = 1.3
                voltar_botao.content.width = 100
                voltar_botao.content.height = 30
                voltar_botao.padding = 20
            page.update()

        def mudar_sair_botao(e):
            if e.data == 'true':
                sair_botao.content.content.scale = 5.5
                sair_botao.content.width += 10
                sair_botao.content.height += 10
                sair_botao.height += 10
                sair_botao.bottom -= 5
            else:
                sair_botao.content.content.scale = 5
                sair_botao.content.width = 800
                sair_botao.content.height = 120
                sair_botao.height = 120
                sair_botao.bottom = 165
            page.update()

        def mudar_jogar_novamente_botao(e):
            if e.data == 'true':
                jogar_novamente_botao.content.content.scale = 5.35
                jogar_novamente_botao.content.width += 10
                jogar_novamente_botao.content.height += 10
                jogar_novamente_botao.height += 10
                jogar_novamente_botao.bottom -= 5
            else:
                jogar_novamente_botao.content.content.scale = 5
                jogar_novamente_botao.content.width = 800
                jogar_novamente_botao.content.height = 120
                jogar_novamente_botao.height = 120
                jogar_novamente_botao.bottom = 340
            page.update()

        voltar_botao = ft.Container(content = ft.Container(
            content = ft.Text("Voltar", color = colors.WHITE, weight=ft.FontWeight.W_700, scale = 1.3),
            bgcolor = colors.BLACK,
            width = 100,
            height = 30,
            border_radius = 100,
            on_click = voltar,
            on_hover = mudar_voltar_botao,
            alignment = ft.alignment.center
            ),
            width = 1400,
            height = 800,
            padding = 20,
            alignment = ft.alignment.bottom_right)

        def fechar(e):
            pyautogui.keyDown('alt')
            pyautogui.press('f4')
            pyautogui.keyUp('alt')

        tela_vitoria = ft.Container(ft.Image(src = 'Tela-Vitoria2.png'),
                            width = 1400, height = 800, alignment=ft.alignment.center)
        
        jogar_novamente_botao = ft.Container(content = ft.Container(
            content = ft.Text("Jogar novamente", color = colors.BLACK, weight=ft.FontWeight.W_800, scale = 5),
            bgcolor = colors.WHITE,
            width = 800,
            height = 120,
            border_radius = 100,
            on_click = voltar,
            on_hover = mudar_jogar_novamente_botao,
            alignment = ft.alignment.center
            ),
            width = 1400,
            height = 120,
            bottom = 340,
            alignment = ft.alignment.center)
        
        sair_botao = ft.Container(content = ft.Container(
            content = ft.Text("Sair", color = colors.BLACK, weight=ft.FontWeight.W_800, scale = 5),
            bgcolor = colors.WHITE,
            width = 800,
            height = 120,
            border_radius = 100,
            on_click = fechar,
            on_hover = mudar_sair_botao,
            alignment = ft.alignment.center
            ),
            width = 1400,
            height = 120,
            bottom = 165,
            alignment = ft.alignment.bottom_center)
        
        borda_sair_botao = ft.Container(
            content = ft.Image('Botao-Sair.png'),
            width = 1400,
            height = 800,
            alignment = ft.alignment.center
            )
        borda_jogar_novamente = ft.Container(
            content = ft.Image('Botao-Jogar_Novamente.png'),
            width = 1400,
            height = 800,
            alignment = ft.alignment.center
            )
        
        def vitoria():
            time.sleep(0.75)
            pagina_jogo.controls.append(tela_vitoria)
            pagina_jogo.controls.append(borda_sair_botao)
            pagina_jogo.controls.append(borda_jogar_novamente)
            pagina_jogo.controls.append(jogar_novamente_botao)
            pagina_jogo.controls.append(sair_botao)
            page.update()

        QNTD_CARDS = 32
        virados = []
        qntd_pares_encontrados = []
        def precisa_virar():
            if len(virados) == 2:
                if all_cards.content.controls[virados[0]].controls[0].src == all_cards.content.controls[virados[1]].controls[0].src:
                    desativar.append(virados[0])
                    desativar.append(virados[1])
                    time.sleep(0.35)
                    all_cards.content.controls[virados[0]].controls[0].opacity=0.4
                    all_cards.content.controls[virados[1]].controls[0].opacity=0.4
                    qntd_pares_encontrados.append('')
                    barra_de_progresso.content.src = f'Barra_de_Progresso-{len(qntd_pares_encontrados)}.png'
                    if len(qntd_pares_encontrados) < 10:
                        texto_qntd_pares_encontrados.content.value = f' 0{len(qntd_pares_encontrados)}   16'
                    else:
                        texto_qntd_pares_encontrados.content.value = f' {len(qntd_pares_encontrados)}   16'
                    if len(qntd_pares_encontrados) > 6:
                        texto_qntd_pares_encontrados.content.color = colors.BLACK87
                        barra.content.color = colors.BLACK87
                    page.update()
                    if len(qntd_pares_encontrados) == 1:
                        vitoria()
                else: time.sleep(1.5)
                for i in range(QNTD_CARDS):
                    if i not in desativar:
                        all_cards.content.controls[i].controls[1].opacity=1
                    if int(all_cards.content.controls[i].controls[2].content.value) in virados:
                        virados.remove(int(all_cards.content.controls[i].controls[2].content.value))
            page.update()

        desativar = []

        def trocar(e):
            button = int(e.control.content.value)
            if button not in desativar:
                if len(virados) < 2:
                    all_cards.content.controls[button].controls[1].opacity=0
                    if button not in virados:
                        virados.append(button)
                    page.update()
                    precisa_virar()

        image_links = {
            'carta-virada': 'carta-virada2.png',
            'pizza': 'carta-pizza.png',
            'hamburguer': 'carta-hamburguer.png',
            'cachorroquente': 'carta-cachorroquente.png',
            'pipoca': 'carta-pipoca.png',
            'batatafrita': 'carta-batatafrita.png',
            'frango': 'carta-frango.png',
            'sorvete': 'carta-sorvete.png',
            'queijo': 'carta-queijo.png',
            'repolho': 'carta-repolho.png',
            'pao': 'carta-pao.png',
            'milho': 'carta-milho.png',
            'abobora': 'carta-abobora.png',
            'melancia': 'carta-melancia.png',
            'laranja': 'carta-laranja.png',
            'macaverde': 'carta-macaverde.png',
            'banana': 'carta-banana.png',
            'tomate': 'carta-tomate.png',
            'kiwi': 'carta-kiwi.png',
            'cafe': 'carta-cafe.png',
            'ketchupmostarda': 'carta-ketchupmostarda.png',
            'chocolate': 'carta-chocolate.png',
            'maca': 'carta-maca.png',
            'carne': 'carta-carne.png',
            'cenoura': 'carta-cenoura.png',
            'uva': 'carta-uva.png',
            'bolo': 'carta-bolo.png',
            'cookie': 'carta-cookie.png',
            'abacaxi': 'carta-abacaxi.png',
            'espaguete': 'carta-espaguete.png',
            'chimarrao': 'carta-chimarrao.png',
        }

        lista_comidas = ['pizza', 'hamburguer', 'cachorroquente', 'pipoca', 'batatafrita', 'frango', 'sorvete', 'queijo', 'repolho', 'pao', 'milho',
                         'abobora', 'melancia', 'laranja', 'macaverde', 'banana', 'tomate', 'kiwi', 'cafe', 'ketchupmostarda', 'chocolate', 'maca',
                         'carne', 'cenoura', 'uva', 'bolo', 'cookie', 'abacaxi', 'espaguete', 'chimarrao']
        comidas = []
        for _ in range(int(QNTD_CARDS/2)):
            comida = random.choice(lista_comidas)
            lista_comidas.remove(comida)
            comidas.append(comida)

        image_cards = []
        for number in range(int(QNTD_CARDS/2)):
            image_cards.append(image_links[comidas[number]])
            image_cards.append(image_links[comidas[number]])
        random.shuffle(image_cards)
        all_cards = ft.Container(ft.Row(
                        controls = [ft.Stack([ft.Image(src = image_cards[i], opacity = 1,),
                                    ft.Image(src = image_links['carta-virada'], opacity = 1,),
                                    ft.Container(content = ft.Text(f'{i}', width = 100, height = 100, opacity = 0), on_click = trocar)],
                        width = 100, height = 100,) for i in range(QNTD_CARDS)], 
                    width = 900, wrap = True, ), width = 1200, height = 800, alignment = ft.alignment.center, left=114)
        
        logo = ft.Container(ft.Image(src = 'Jogo_da_Memoria-LOGO.png'),
                            width = 1400, height = 170, alignment=ft.alignment.center)
        barra_de_progresso = ft.Container(ft.Image(src = 'Barra_de_Progresso-0.png'),
                            width = 1400, height = 800, alignment=ft.alignment.center)
        background2 = ft.Container(ft.Image(src = 'Background2_Jogo_da_Memoria.png'),
                            width = 1400, height = 800, alignment=ft.alignment.center)
        texto_qntd_pares_encontrados = ft.Container(content = ft.Text(" 00   16", weight=ft.FontWeight.W_700, color = colors.GREY_800, scale = 3.5),
                            width = 1400, height = 800, alignment = ft.alignment.bottom_center, padding = 105)
        barra = ft.Container(content = ft.Text(f"   /  ", weight=ft.FontWeight.W_700, color = colors.GREY_800, scale = 3.5),
                            width = 1400, height = 800, alignment = ft.alignment.bottom_center, padding = 108)
        
        pagina_jogo = ft.Stack([background2, logo, barra_de_progresso, texto_qntd_pares_encontrados, barra, voltar_botao, all_cards])
        page.add(pagina_jogo)

    def change_start_button(e):
        if e.data == 'true':
            start_button.content.content.scale = 6
            start_button.content.width += 15
            start_button.content.height += 15
            sombra_grande.visible = True
        else:
            start_button.content.content.scale = 5
            start_button.content.width = BUTTON_WIDTH
            start_button.content.height = BUTTON_HEIGHT
            sombra_grande.visible = False
        page.update()

    start_button = ft.Container(content = ft.Container(
        content = ft.Text("Iniciar", color = colors.BLACK, weight=ft.FontWeight.W_700, scale = 5),
        width = BUTTON_WIDTH,
        height = BUTTON_HEIGHT,
        bgcolor = colors.RED_400,
        border_radius = 50,
        on_click = game,
        on_hover = change_start_button,
        alignment = ft.alignment.center
        ),
            width = 1400,
            height = 800,
            padding = 10,
            alignment = ft.alignment.center
        )

    background = ft.Image(src = 'Background1_Jogo_da_Memoria.png',
                width = 1400, height = 800)
    sombra_grande = ft.Image(src = 'Sombra_Grande.png',
                width = 1400, height = 800, visible = False)
    pagina_inicial = ft.Stack([background, sombra_grande, start_button])

    page.add(pagina_inicial)

ft.app(main)
