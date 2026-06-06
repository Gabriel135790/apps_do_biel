import flet as ft

def main(page: ft.Page):
    page.window.width = 400
    page.window.height = 400
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = 'Calculadora'

    def calcular(e):
        texto_original = entrada_calculo.value
        
        try:
            # Substitui os símbolos visuais pelos matemáticos do Python
            corrigido = texto_original.replace('x', '*').replace('×', '*').replace('÷', '/')

            # Executa o cálculo matemático
            resp = eval(corrigido)

            # Mostra o resultado mudando o próprio campo na tela
            entrada_calculo.value = str(resp)
            
            # Mostra o SnackBar azul de sucesso
            alerta = ft.SnackBar(
                content=ft.Text(value=f'A Resposta de {texto_original} é {resp}'), 
                bgcolor='blue'
            )
            page.overlay.append(alerta)
            alerta.open = True
            page.update()

        except:
            # Se o eval falhar (ex: campo vazio ou conta incompleta como "2+"), cai aqui
            alerta = ft.SnackBar(
                content=ft.Text(value='Coloque um Cálculo Válido, Por favor!', weight=ft.FontWeight.BOLD), 
                bgcolor='red'
            )
            page.overlay.append(alerta)
            alerta.open = True
            page.update()

    titulo = ft.Text(value='Calculadora', size=35, color=('blue'))
    descricao = ft.Text(value='uma simples calculadora =)', size=15, color=('blue'))
    entrada_calculo = ft.TextField(label='Cálculo:', value='0')
    botao = ft.Button(content='Calcular', on_click=calcular)

    page.add(titulo, descricao, entrada_calculo, botao)

ft.run(main=main)
