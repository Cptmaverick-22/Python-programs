import pyautogui as pag 

pag.sleep(5)
msg = 'hello'
for i in range(5):
    pag.write(msg)
    pag.press('enter')