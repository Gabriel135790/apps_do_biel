import flet as ft
import os
from tkinter import messagebox
def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.width = 400
    page.window.height = 500
    page.title = 'Calculadora de BMI'

    def calcular(e):
        if not peso.value.isnumeric() or not altura.value.isnumeric() or peso.value <= '0' or altura.value <= '0':
            messagebox.showerror('Erro Crítico', 'Erro Crítico! Por favor abra o APP novamente')

            try:
                page.run_task(page.window.destroy)
            except:
                os._exit(0)

        calculado = float(peso.value) / (float(altura.value) / 100) ** 2

        if calculado < 18.5:
            estado = 'Abaixo do Peso'
            cor = 'blue'
        elif calculado >= 18.5 and calculado <= 24.9:
            estado = 'Peso Normal (saudável!)'
            cor = 'green'
        elif calculado >= 25 and calculado <= 29.9:
            estado = 'Sobrepeso (Pré-obesidade)'
            cor = 'yellow'
        elif calculado >= 30 and calculado <= 34.9:
            estado = 'Obesidade Grau I'
            cor = 'orange'
        elif calculado >= 35 and calculado <= 39.9:
            estado = 'Obesidade Grau II (severa)'
            cor = 'red'
        else:
            estado = 'Obesidade Grau III (mórbida)'
            cor = "#870000"
        
        alerta = ft.SnackBar(
            content=ft.Text(f'BMI: {calculado:.2f}, Estado: {estado}'), bgcolor=cor)
        
        page.overlay.append(alerta)
        alerta.open = True
        page.update()

    def trocar_cor(e):
        botao.bgcolor = '#2083DF' if e.data == True else None
        page.update()

    titulo = ft.Text(value='Calculadora de BMI', color=('blue'), size=35)
    descricao = ft.Text(value='um simples app feito pelo o Gabriel =)', color="#2083DF")
    peso = ft.TextField(label='Peso: ', value='0')
    altura = ft.TextField(label='Altura (em cm):', value='0')
    botao = ft.Button('Mostrar BMI', width=100, height=50, on_hover=trocar_cor, on_click=calcular)

    page.add(titulo, descricao, peso, altura, botao)

ft.run(main=main)