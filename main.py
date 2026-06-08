import pyautogui
import time

pyautogui.PAUSE = 0.5

# Abrir o spotify
pyautogui.press("win") # clicar com o mouse
pyautogui.write("spotify")
pyautogui.press("enter")

time.sleep(6)

pyautogui.hotkey('ctrl', 'l')
pyautogui.write("marina sena - desmitificar")

time.sleep(3)
pyautogui.press("enter")

time.sleep(3)
pyautogui.click(x=1055, y=319)
