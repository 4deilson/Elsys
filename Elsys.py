from typing import Text
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from time import get_clock_info, sleep
from bs4 import BeautifulSoup
from datetime import datetime 
import time
from tkinter import *

def AtualizarStatusElsys():    

    dtInicio =  time.time()    
    options = Options(); options.add_argument('--headless')
    navegador = webdriver.Chrome(executable_path = r'C:/Curso asp.Net Core/Elsys/chromedriver.exe', options = options)    
    navegador.get('http://192.168.10.254/index.html?status')
    sleep(1.6)
    
    page_content = navegador.page_source
    site = BeautifulSoup(page_content,'html.parser')
    table_status = site.find('table', attrs={'class' :'spacing-table'})

    ip_protocol         = table_status.find('span', attrs={'class':'ip_protocol'})
    endereco_ip         = table_status.find('span', attrs={'class':'endereco_ip'})
    ipv6                = table_status.find('span', attrs={'class':'hide_ipv6_on_disconnect'})
    ip_subnet_mask      = table_status.find('span', attrs={'class':'ip_subnet_mask'})
    tipo_rede_movel     = table_status.find('span', attrs={'class':'tipo_rede_movel'})
    nivel_3g            = table_status.find('span', attrs={'class':'nivel-3g'})
    signal_quality      = table_status.find('span', attrs={'class':'signal_quality'})
    banda               = table_status.find('span', attrs={'class':'banda'})
    freq_3G             = table_status.find('span', attrs={'class':'freq_3G'})
    imei                = table_status.find('span', attrs={'class':'imei'})
    sim_number          = table_status.find('span', attrs={'class':'sim-number'})
    data_translate      = table_status.find('span', attrs={'class':'data-translate'})
    field_name          = table_status.find('span', attrs={'class':'field_name'})

    print('Endereço IP:',endereco_ip.text)
    print('Nivel do Sinal:',nivel_3g.text)
    print('Qualidade do Sinal:',signal_quality)
    print('Tipo de Rede:',tipo_rede_movel.text)

    dtFinal = time.time()
    Dtdecorrido = dtFinal-dtInicio  
    print('Tempo de Execução:',dtFinal-dtInicio )

    navegador.quit()

#AtualizarStatusElsys()


class Application():
   mainWindows = Tk()
   mainWindows.title('Elsys - Aplimax') 
   mainWindows.iconwindow('') 
   mainWindows.geometry('400x500+800+200')
   mainWindows.resizable(False,False)
   atualizar = Button(mainWindows,fg='green' ,text='Atualizar',)
   atualizar.pack(COMMAND=AtualizarStatusElsys())
   mainWindows['bg'] = 'blue'



   mainWindows.mainloop()    
Application()