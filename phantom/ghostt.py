import os,sys
from colorama import Fore, Style
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
banner = f'''{Fore.RED}\n
                       ---                                     
                    -        --                             
                --( /     \ )XXXXXXXXXXXXX                   
            --XXX(   O   O  )XXXXXXXXXXXXXXX-              
           /XXX(       U     )        XXXXXXX\               
         /XXXXX(              )--   XXXXXXXXXXX\             
        /XXXXX/ (      O     )   XXXXXX   \XXXXX
        XXXXX/   /            XXXXXX   \   \XXXXX----        
        XXXXXX  /          XXXXXX         \  ----  -         
---     XXX  /          XXXXXX      \           ---        
  --  --  /      /\  XXXXXX            /     ---=         
    -        /    XXXXXX              '--- XXXXXX         
      --\/XXX\ XXXXXX                      /XXXXX         
        \XXXXXXXXX                        /XXXXX/
         \XXXXXX                         /XXXXX/         
           \XXXXX--  /                -- XXXX/       
            --XXXXXXX---------------  XXXXX--         
               \XXXXXXXXXXXXXXXXXXXXXXXX-            
                 --XXXXXXXXXXXXXXXXXX-
        ╔═════════════════════════════════╗
        ║  - - -[Admin:VuCongHuyHoang]- - ║    
        ╚═════════════════════════════════╝'''
sys.stdout.write(f"\x1b]2;Online Users: [1] | Owner:Vu Cong Huy Hoang\x07")
print(banner)
url=input(f'{Fore.RED}Url:')
time=input(f'{Fore.RED}Time:')
rate=input(f'{Fore.RED}Rate:')
Thread=input(f'{Fore.RED}Thread:')
os.system(f"python api.py {url} {time} {rate} {Thread}")