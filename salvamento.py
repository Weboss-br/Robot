#importando a biblioteca pyautogui e atribuindo um apelido direto
import rpa as r
import pyautogui as p




p.hotkey('win', 'r', duration=1)
p.sleep(1)
p.typewrite('cmd')
p.sleep(1)
p.hotkey('enter')

p.typewrite('code .')
p.sleep(0.2)
p.hotkey('enter')
p.sleep(5)

p.hotkey('win', 'up', duration=1)

p.sleep(3)

#Abre o menu
p.click(x=62, y=19)
#Clica em newfile
p.sleep(1.5)
p.click(x=156, y=77)
p.sleep(3)
p.click(x=399, y=98)
p.sleep(3)
p.typewrite('novoArquivo.py')
p.sleep(0.5)
p.hotkey('enter')

p.sleep(1.5)
p.typewrite('SAPORRA!!!')
#r.close()