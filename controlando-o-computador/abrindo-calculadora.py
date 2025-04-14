#!pip install pyautogui
import pyautogui as pg

pg.sleep(2)

#print(posicaoMouse.position())

pg.moveTo(x=455, y=754)
pg.click(x=455, y=754)

# Aguarda 2 segundos para abrir o menu iniciar
pg.sleep(2)

# Digita 'calculadora'
pg.typewrite('calculadora')

# Espera 3 segundos para o sistema listar os apps
pg.sleep(3)

# Descubro a posição o botão abrir
    #print(posicaoMouse.position())

# Move o mouse até a posição da calculadora e clica
pg.moveTo(x=724, y=387)
pg.click(x=724, y=387)