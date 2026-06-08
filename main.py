import pyautogui
import time


pyautogui.PAUSE = 0.5


def clique_proporcional(x_base, y_base, largura_base=1920, altura_base=1080):

    # resolução atual do usuário
    largura_tela, altura_tela = pyautogui.size()

    # converter proporcionalmente
    x_real = int((x_base / largura_base) * largura_tela)
    y_real = int((y_base / altura_base) * altura_tela)

    pyautogui.click(x=x_real, y=y_real)
    
def tocar_musica(musica):
    # Abrir o Spotify
    pyautogui.press("win")
    pyautogui.write("spotify")
    pyautogui.press("enter")

    time.sleep(4.5)

    # Ir para pesquisa
    pyautogui.hotkey('ctrl', 'l')

    # Digitar a música escolhida
    pyautogui.write(musica)

    time.sleep(1.5)
    pyautogui.press("enter")

    time.sleep(1.2)

    # Clicar no play
    clique_proporcional(1055, 319)