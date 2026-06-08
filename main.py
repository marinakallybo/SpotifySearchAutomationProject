import pyautogui
import time


pyautogui.PAUSE = 0.5


def tocar_musica(musica):
    # Abrir o Spotify
    pyautogui.press("win")
    pyautogui.write("spotify")
    pyautogui.press("enter")

    time.sleep(6)

    # Ir para pesquisa
    pyautogui.hotkey('ctrl', 'l')

    # Digitar a música escolhida
    pyautogui.write(musica)

    time.sleep(3)
    pyautogui.press("enter")

    time.sleep(3)

    # Clicar no play
    pyautogui.click(x=1055, y=319)