# Importing libraries
import pyautogui
import time
import pandas as pd

# Configure the pyautogui method pause
pyautogui.PAUSE = 0.5

# Start the robot
# First step - open the navigator (Chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Second step - write link website
time.sleep(5)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(5)

# Third step - make login in sistem
pyautogui.click(x=769, y=468)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("sua senha")
pyautogui.click(x=974, y=682)
time.sleep(5)

# Fourth step - read the file and starting registration
# Use the pandas to the read csv and put information in new variable
tabela = pd.read_csv("produtos.csv")
for linha in tabela.index:
    pyautogui.click(x=691, y=324)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)
