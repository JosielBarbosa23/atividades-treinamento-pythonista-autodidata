

#Desafio 1 - Crie um programa que irá navegar até um site e baixe fotos deste mesmo site paralelamente. Faça o uso de thread para a tarefa de baixar fotos.

import webbrowser
import threading
import time

def acessando_site(site):
    print(f'Abrindo o site: {site}')
    webbrowser.open_new(site)

def baixando_fotos():
    for i in range(1, 6):
        print(f'Baixando fotos - {i}/5')
        time.sleep(3)
    print('Fotos baixadas')

site = 'https:www.instagram.com'
nova_thread = threading.Thread(target= acessando_site, args=('https:www.instagram.com',), daemon=True)

nova_thread.start()
baixando_fotos()
nova_thread.join()