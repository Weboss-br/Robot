#importando a biblioteca pyautogui e atribuindo um apelido direto
import rpa as r
import pyautogui as p

r.init()

r.url('https://github.com/login')
r.wait(2.0)
r.type('//*[@id="login_field"]', 'weboss@gmail.com')
r.wait(2.0)
r.type('//*[@id="password"]', 'vtVT8BKw859NtcM[enter]')
r.wait(2.0)
r.url('https://github.com/Weboss-br?tab=repositories')
r.wait(2.0)
r.url('https://github.com/new')
r.wait(2.0)
r.type('//*[@id="repository_name"]', 'Novo Repositorio')
r.wait(2.0)
r.type('//*[@id="repository_description"]', 'Descrição do repositório é aqui.')
r.wait(2.0)
r.click('//*[@id="repository_auto_init"]')
r.wait(2.0)
r.click('//*[@id="new_repository"]/div[5]/button')
r.wait(2.0)
r.click('//*[@id="repo-content-pjax-container"]/div/div/div[3]/div[1]/div[2]/span[1]/get-repo/details/summary')
r.wait(2.0)
r.click('//*[@id="local-panel"]/ul/li[1]/tab-container/div[2]/div/div/clipboard-copy')
r.wait(2.0)



p.hotkey('win', 'r', duration=1)
p.sleep(1)
p.typewrite('cmd')
p.sleep(1)
p.hotkey('enter')
p.sleep(1)

p.typewrite('cd/')
p.hotkey('enter')
p.sleep(0.5)
p.typewrite('cd Users')
p.hotkey('enter')
p.sleep(0.5)
p.typewrite('cd User')
p.hotkey('enter')
p.sleep(0.5)

p.typewrite('cd Documents')
p.hotkey('enter')
p.sleep(0.5)

p.typewrite('cd Python22')
p.hotkey('enter')
p.sleep(0.5)
p.typewrite('MKdir TesteExercicio')
p.sleep(0.5)
p.hotkey('enter')
p.typewrite('cd TesteExercicio')
p.hotkey('enter')
p.sleep(0.5)
p.typewrite('git clone ')
p.sleep(3)
p.hotkey('ctrl', 'v')
p.sleep(0.5)
p.hotkey('enter')
p.sleep(1.5)

p.typewrite('code .')
p.sleep(0.2)
p.hotkey('enter')
p.sleep(5)

p.hotkey('win', 'up', duration=1)

p.sleep(3)

#Abre o menu
p.click(x=61, y=22)
p.sleep(2)
p.click(x=61, y=95)
p.sleep(2)

p.typewrite('novoArquivo.py')
p.sleep(0.5)
p.hotkey('enter')
p.sleep(1.5)
p.hotkey('enter')
p.sleep(3)
p.typewrite('SAPORRA!!!')
#r.close()