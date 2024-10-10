import pyautogui

pyautogui.PAUSE = 0.5

def clicar (x, y):
    pyautogui.click(x, y)

def apertar (x):
    pyautogui.press(x)

def digitar (x):
    pyautogui.write(x)

# ---------------------------------------------------------------
# abrir navegador

apertar('win')
digitar('chrome')
apertar('enter')
digitar('https://statusinvest.com.br/acoes/variacao/ibovespa')
apertar('enter')


# digitar https://statusinvest.com.br/acoes/variacao/ibovespa

# 