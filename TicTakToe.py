import random
import os
import time


def uw():
    print("""
██    ██ ███████ ███████ ██████      ██     ██  ██████  ███    ██ 
██    ██ ██      ██      ██   ██     ██     ██ ██    ██ ████   ██ 
██    ██ ███████ █████   ██████      ██  █  ██ ██    ██ ██ ██  ██ 
██    ██      ██ ██      ██   ██     ██ ███ ██ ██    ██ ██  ██ ██ 
 ██████  ███████ ███████ ██   ██      ███ ███   ██████  ██   ████ 
""")
    
def ul():
    print(r"""                                                                                  
@@@  @@@   @@@@@@   @@@@@@@@  @@@@@@@      @@@        @@@@@@    @@@@@@   @@@@@@@  
@@@  @@@  @@@@@@@   @@@@@@@@  @@@@@@@@     @@@       @@@@@@@@  @@@@@@@   @@@@@@@  
@@!  @@@  !@@       @@!       @@!  @@@     @@!       @@!  @@@  !@@         @@!    
!@!  @!@  !@!       !@!       !@!  @!@     !@!       !@!  @!@  !@!         !@!    
@!@  !@!  !!@@!!    @!!!:!    @!@!!@!      @!!       @!@  !@!  !!@@!!      @!!    
!@!  !!!   !!@!!!   !!!!!:    !!@!@!       !!!       !@!  !!!   !!@!!!     !!!    
!!:  !!!       !:!  !!:       !!: :!!      !!:       !!:  !!!       !:!    !!:    
:!:  !:!      !:!   :!:       :!:  !:!      :!:      :!:  !:!      !:!     :!:    
::::: ::  :::: ::    :: ::::  ::   :::      :: ::::  ::::: ::  :::: ::      ::    
 : :  :   :: : :    : :: ::    :   : :     : :: : :   : :  :   :: : :       :     
                                                                                  
""")
    print("Ai hub job lelega")

def draw():
    print("""                                                                                                      
DDDDDDDDDDDDD      RRRRRRRRRRRRRRRRR                  AAA   WWWWWWWW                           WWWWWWWW
D::::::::::::DDD   R::::::::::::::::R                A:::A  W::::::W                           W::::::W
D:::::::::::::::DD R::::::RRRRRR:::::R              A:::::A W::::::W                           W::::::W
DDD:::::DDDDD:::::DRR:::::R     R:::::R            A:::::::AW::::::W                           W::::::W
  D:::::D    D:::::D R::::R     R:::::R           A:::::::::AW:::::W           WWWWW           W:::::W 
  D:::::D     D:::::DR::::R     R:::::R          A:::::A:::::AW:::::W         W:::::W         W:::::W  
  D:::::D     D:::::DR::::RRRRRR:::::R          A:::::A A:::::AW:::::W       W:::::::W       W:::::W   
  D:::::D     D:::::DR:::::::::::::RR          A:::::A   A:::::AW:::::W     W:::::::::W     W:::::W    
  D:::::D     D:::::DR::::RRRRRR:::::R        A:::::A     A:::::AW:::::W   W:::::W:::::W   W:::::W     
  D:::::D     D:::::DR::::R     R:::::R      A:::::AAAAAAAAA:::::AW:::::W W:::::W W:::::W W:::::W      
  D:::::D     D:::::DR::::R     R:::::R     A:::::::::::::::::::::AW:::::W:::::W   W:::::W:::::W       
  D:::::D    D:::::D R::::R     R:::::R    A:::::AAAAAAAAAAAAA:::::AW:::::::::W     W:::::::::W        
DDD:::::DDDDD:::::DRR:::::R     R:::::R   A:::::A             A:::::AW:::::::W       W:::::::W         
D:::::::::::::::DD R::::::R     R:::::R  A:::::A               A:::::AW:::::W         W:::::W          
D::::::::::::DDD   R::::::R     R:::::R A:::::A                 A:::::AW:::W           W:::W           
DDDDDDDDDDDDD      RRRRRRRR     RRRRRRRAAAAAAA                   AAAAAAAWWW             WWW            
                                                                                           
""")
def quit():
    os.system('cls')
    print('  _______   ______     ______    _______  .______   ____    ____  _______ ')
    print(' /  _____| /  __  \   /  __  \  |       \ |   _  \  \   \  /   / |   ____|')
    print('|  |  __  |  |  |  | |  |  |  | |  .--.  ||  |_)  |  \   \/   /  |  |__   ')
    print('|  |  __  |  |  |  | |  |  |  | |  .--.  ||  |_)  |  \   \/   /  |  |__   ')
    print('|  | |_ | |  |  |  | |  |  |  | |  |  |  ||   _  <    \_    _/   |   __|  ')
    print("|  |__| | |  `--'  | |  `--'  | |  '--'  ||  |_)  |     |  |     |  |____ ")
    print(' \______|  \______/   \______/  |_______/ |______/      |__|     |_______|')
    print("https://github.com/AjitChauhan081")
    time.sleep(10)
    

                                                                          

def retry(a: str,u: list,m: list,l: list)->str:
    os.system('cls')
    logo()
    if 'User' in a:
        uw()
    elif "Bot" in a:
        ul()
    elif "Draw" in a:
        draw()
            
    print(u[0]," | ",u[1]," | ",u[2])
    print("____________")
    print(m[0]," | ",m[1]," | ",m[2])
    print("____________")
    print(l[0]," | ",l[1]," | ",l[2])
    print(a)
    print("if you want to play again input(play / p) to quit(quit / q) :")
    match=str(input()).lower()
    if (match=='quit' or match=='q'):
        return 'q'
    elif (match=='play' or  match=='p'):
        return 'p'
    else:
        return retry(("Invalid Choice " + a),u,m,l)
    
  
def logo():
    print("████████ ██  ██████ ████████  █████  ██   ██ ████████  ██████  ███████ ")
    print("   ██    ██ ██         ██    ██   ██ ██  ██     ██    ██    ██ ██      ")
    print("   ██    ██ ██         ██    ███████ █████      ██    ██    ██ █████   ")
    print("   ██    ██ ██         ██    ██   ██ ██  ██     ██    ██    ██ ██      ")
    print("   ██    ██  ██████    ██    ██   ██ ██   ██    ██     ██████  ███████ ")        
    print("-".center(100,"-"))
                                             
                                                                           
    
def choise()->str:
    os.system('cls')
    logo()    
    print("""
║ ║    ║    ╔═║    ║          
 ╝     ║    ║ ║    ║          
╝ ╝    ╝    ══╝    ╝          
                              
═╝═╝═╝═╝═╝═╝═╝═╝═╝═╝═╝═╝═╝═╝═╝
                              
╔═║    ║    ║ ║    ║          
║ ║    ║     ╝     ║          
══╝    ╝    ╝ ╝    ╝          
                              
═╝═╝═╝═╝═╝═╝═╝═╝═╝═╝═╝═╝═╝═╝═╝
                              
      ║          ║    ║ ║     
      ║          ║     ╝      
      ╝          ╝    ╝ ╝   
""")
    print("-".center(100,"-"))

    print("Enter your Choice O,X")
    ox=str(input()).upper()
    if ox in {'O','X'}:
        return ox 
    else:
        return choise()


u=['','','']
m=['','','']
l=['','','']
ox=choise()
if ox=="O" :
    bot="X"
elif ox=="X":
    bot="O"

past=["0"]
match='play'


while match!='quit':
    os.system('cls')
    logo()
    print(u[0]," | ",u[1]," | ",u[2])
    print("____________")
    print(m[0]," | ",m[1]," | ",m[2])
    print("____________")
    print(l[0]," | ",l[1]," | ",l[2])
    print("\n\n")
    print("----Example---")
    print("1"," | ","2"," | ","3")
    print("------------")
    print("4"," | ","5"," | ","6")
    print("------------")
    print("7"," | ","8"," | ","9")
    print("Enter your choice:-",end='')
    choice=input()
    while len(past)!=9:
        if choice  in past:
            print("Enter Different No:-",end='')
            choice=input()
        else:
            if choice=="1":
                past.append(choice)
                u[0]=ox
                break
            elif choice=="2":
                past.append(choice)
                u[1]=ox
                break
            elif choice=="3":
                past.append(choice)
                u[2]=ox
                break
            elif choice=="4":
                past.append(choice)
                m[0]=ox
                break
            elif choice=="5":
                past.append(choice)
                m[1]=ox
                break
            elif choice=="6":
                past.append(choice)
                m[2]=ox
                break
            elif choice=="7":
                past.append(choice)
                l[0]=ox
                break
            elif choice=="8":
                past.append(choice)
                l[1]=ox
                break
            elif choice=="9":
                past.append(choice)
                l[2]=ox
                break
            else:
                print("Enter Different No:-",end='')
                choice=input()
                
            
    while True:
        
        bot_choice=str(random.randint(1,9))
        #print(str(bot_choice) not in past)
        
        if bot_choice not in past  :
            
            if bot_choice=='1':
                u[0]=bot
                past.append(bot_choice)
                break
            elif bot_choice=='2':
                past.append(bot_choice)
                u[1]=bot
                break
            elif bot_choice=='3':
                past.append(bot_choice)
                u[2]=bot
                break
            elif bot_choice=='4':
                past.append(bot_choice)
                m[0]=bot
                break
            elif bot_choice=='5':
                past.append(bot_choice)
                m[1]=bot
                break
            elif bot_choice=='6':
                past.append(bot_choice)
                m[2]=bot
                break
            elif bot_choice=='7':
                past.append(bot_choice)
                l[0]=bot
                break
            elif bot_choice=='8':
                past.append(bot_choice)
                l[1]=bot
                break
            elif bot_choice=='9':
                past.append(bot_choice)
                l[2]=bot
                break
        #break
        if len(past)==9:
            if choice=="1":
                past.append(choice)
                u[0]=ox
                break
            elif choice=="2":
                past.append(choice)
                u[1]=ox
                break
            elif choice=="3":
                past.append(choice)
                u[2]=ox
                break
            elif choice=="4":
                past.append(choice)
                m[0]=ox
                break
            elif choice=="5":
                past.append(choice)
                m[1]=ox
                break
            elif choice=="6":
                past.append(choice)
                m[2]=ox
                break
            elif choice=="7":
                past.append(choice)
                l[0]=ox
                break
            elif choice=="8":
                past.append(choice)
                l[1]=ox
                break
            elif choice=="9":
                past.append(choice)
                l[2]=ox
                break
        
            
    
    if u[0]==u[1]==u[2]==ox or m[0]==m[1]==m[2]==ox or l[0]==l[1]==l[2]==ox or u[0]==m[0]==l[0]==ox or u[0]==m[0]==l[0]==ox or u[1]==m[1]==l[1]==ox or u[2]==m[2]==l[2]==ox or u[0]==m[1]==l[2]==ox or u[2]==m[1]==l[0]==ox:
        logo()
        print(u[0]," | ",u[1]," | ",u[2])
        print("____________")
        print(m[0]," | ",m[1]," | ",m[2])
        print("____________")
        print(l[0]," | ",l[1]," | ",l[2])
        print("\n\n")
        a = "User Wins"
        match=retry(a,u,m,l)
        if (match=='q'):
            quit()
            break
        elif (match=='p'):
            u=['','','']
            m=['','','']
            l=['','','']
            ox=choise()
            if ox=="O":
                bot="X"
            elif ox=="X":
                bot="O"
            past=["0"]
            
    elif u[0]==u[1]==u[2]==bot or m[0]==m[1]==m[2]==bot or l[0]==l[1]==l[2]==bot or u[0]==m[0]==l[0]==bot or u[0]==m[0]==l[0]==bot or u[1]==m[1]==l[1]==bot or u[2]==m[2]==l[2]==bot or u[0]==m[1]==l[2]==bot or u[2]==m[1]==l[0]==bot:
        logo()
        print(u[0]," | ",u[1]," | ",u[2])
        print("____________")
        print(m[0]," | ",m[1]," | ",m[2])
        print("____________")
        print(l[0]," | ",l[1]," | ",l[2])
        print("\n\n")
        a="Bot Wins"
        match=retry(a,u,m,l)
        if (match=='q'):
            quit()
            break
        elif (match=='p'):
            u=['','','']
            m=['','','']
            l=['','','']
            ox=choise()
            if ox=="O":
                bot="X"
            elif ox=="X":
                bot="O"
            past=["0"]
    
    
    elif len(past)==10:
        if u[0]==u[1]==u[2]==ox or m[0]==m[1]==m[2]==ox or l[0]==l[1]==l[2]==ox or u[0]==m[0]==l[0]==ox or u[0]==m[0]==l[0]==ox or u[1]==m[1]==l[1]==ox or u[2]==m[2]==l[2]==ox or u[0]==m[1]==l[2]==ox or u[2]==m[1]==l[0]==ox:
            logo()
            print(u[0]," | ",u[1]," | ",u[2])
            print("____________")
            print(m[0]," | ",m[1]," | ",m[2])
            print("____________")
            print(l[0]," | ",l[1]," | ",l[2])
            print("\n\n")
            a="User Wins"
            match=retry(a,u,m,l)
            if (match=='q'):
                quit()
                break
            elif (match=='p'):
                u=['','','']
                m=['','','']
                l=['','','']
                ox=choise()
                if ox=="O":
                    bot="X"
                elif ox=="X":
                    bot="O"
                past=["0"]
            
        elif u[0]==u[1]==u[2]==bot or m[0]==m[1]==m[2]==bot or l[0]==l[1]==l[2]==bot or u[0]==m[0]==l[0]==bot or u[0]==m[0]==l[0]==bot or u[1]==m[1]==l[1]==bot or u[2]==m[2]==l[2]==bot or u[0]==m[1]==l[2]==bot or u[2]==m[1]==l[0]==bot:
            logo()
            print(u[0]," | ",u[1]," | ",u[2])
            print("____________")
            print(m[0]," | ",m[1]," | ",m[2])
            print("____________")
            print(l[0]," | ",l[1]," | ",l[2])
            print("\n\n")
            a="Bot Wins"
            match=retry(a,u,m,l)
            if (match=='q'):
                quit()
                break
            elif (match=='p'):
                u=['','','']
                m=['','','']
                l=['','','']
                ox=choise()
                if ox=="O":
                    bot="X"
                elif ox=="X":
                    bot="O"
                past=["0"]
        else:
            logo()
            print(past)
            print(len(past))
            print(u[0]," | ",u[1]," | ",u[2])
            print("____________")
            print(m[0]," | ",m[1]," | ",m[2])
            print("____________")
            print(l[0]," | ",l[1]," | ",l[2])
            print("\n\n")
            a="Draw"
            match=retry(a,u,m,l)
            if (match=='q'):
                quit()
                break
            elif (match=='p'):
                u=['','','']
                m=['','','']
                l=['','','']
                ox=choise()
                if ox=="O":
                    bot="X"
                elif ox=="X":
                    bot="O"
                past=["0"]
        
