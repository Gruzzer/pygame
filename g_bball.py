import random

def D_main():
    print("""
    ▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣
    ▣▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▣
    ▣▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▣
    ▣▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▣
    ▣▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▣
    ▣▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▣
    ▣▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▣
    ▣▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▣
    ▣▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▣
    ▣▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▣
    ▣▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▣
    ▣▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▣
    ▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣""")
def D_out():
    print("""
    ▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣
    ▣▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▣
    ▣▒▒▒□□□□□□□▒▒▒▒□▒▒▒▒▒▒▒□▒▒▒□□□□□□□□□▒▒▣
    ▣▒▒□▒▒▒▒▒▒▒□▒▒▒□▒▒▒▒▒▒▒□▒▒▒▒▒▒▒□▒▒▒▒▒▒▣
    ▣▒▒□▒▒▒▒▒▒▒□▒▒▒□▒▒▒▒▒▒▒□▒▒▒▒▒▒▒□▒▒▒▒▒▒▣
    ▣▒▒□▒▒▒▒▒▒▒□▒▒▒□▒▒▒▒▒▒▒□▒▒▒▒▒▒▒□▒▒▒▒▒▒▣
    ▣▒▒□▒▒▒▒▒▒▒□▒▒▒□▒▒▒▒▒▒▒□▒▒▒▒▒▒▒□▒▒▒▒▒▒▣
    ▣▒▒□▒▒▒▒▒▒▒□▒▒▒□▒▒▒▒▒▒▒□▒▒▒▒▒▒▒□▒▒▒▒▒▒▣
    ▣▒▒□▒▒▒▒▒▒▒□▒▒▒□▒▒▒▒▒▒▒□▒▒▒▒▒▒▒□▒▒▒▒▒▒▣
    ▣▒▒□▒▒▒▒▒▒▒□▒▒▒□▒▒▒▒▒▒▒□▒▒▒▒▒▒▒□▒▒▒▒▒▒▣
    ▣▒▒▒□□□□□□□▒▒▒▒▒□□□□□□□▒▒▒▒▒▒▒▒□▒▒▒▒▒▒▣
    ▣▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▣
    ▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣""")
def D_hit():
    print("""
    ▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣
    ▣▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▣
    ▣▒▒□▒▒▒▒▒▒▒□▒▒▒▒▒□□□□□▒▒▒▒▒□□□□□□□□□▒▒▣
    ▣▒▒□▒▒▒▒▒▒▒□▒▒▒▒▒▒▒□▒▒▒▒▒▒▒▒▒▒▒□▒▒▒▒▒▒▣
    ▣▒▒□▒▒▒▒▒▒▒□▒▒▒▒▒▒▒□▒▒▒▒▒▒▒▒▒▒▒□▒▒▒▒▒▒▣
    ▣▒▒□▒▒▒▒▒▒▒□▒▒▒▒▒▒▒□▒▒▒▒▒▒▒▒▒▒▒□▒▒▒▒▒▒▣
    ▣▒▒□□□□□□□□□▒▒▒▒▒▒▒□▒▒▒▒▒▒▒▒▒▒▒□▒▒▒▒▒▒▣
    ▣▒▒□▒▒▒▒▒▒▒□▒▒▒▒▒▒▒□▒▒▒▒▒▒▒▒▒▒▒□▒▒▒▒▒▒▣
    ▣▒▒□▒▒▒▒▒▒▒□▒▒▒▒▒▒▒□▒▒▒▒▒▒▒▒▒▒▒□▒▒▒▒▒▒▣
    ▣▒▒□▒▒▒▒▒▒▒□▒▒▒▒▒▒▒□▒▒▒▒▒▒▒▒▒▒▒□▒▒▒▒▒▒▣
    ▣▒▒□▒▒▒▒▒▒▒□▒▒▒▒▒□□□□□▒▒▒▒▒▒▒▒▒□▒▒▒▒▒▒▣
    ▣▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▣
    ▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣""")
def D_wow():
    print("""
    ▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣
    ▣▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▣
    ▣▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▣
    ▣▒□▒▒▒□▒▒□□□▒▒□▒▒▒□▒□□□□▒▒□▒▒▒□▒▒□□□▒▒▣
    ▣▒□▒▒▒□▒□▒▒▒□▒□□▒□□▒□▒▒▒□▒□▒▒▒□▒□▒▒▒□▒▣
    ▣▒□▒▒▒□▒□▒▒▒□▒□▒□▒□▒□▒▒▒□▒□▒▒▒□▒□▒▒▒□▒▣
    ▣▒□□□□□▒□▒▒▒□▒□▒▒▒□▒□□□□▒▒□▒▒▒□▒□▒▒▒□▒▣
    ▣▒□▒▒▒□▒□▒▒▒□▒□▒▒▒□▒□▒▒□▒▒□▒▒▒□▒□▒▒▒□▒▣
    ▣▒□▒▒▒□▒□▒▒▒□▒□▒▒▒□▒□▒▒▒□▒□▒▒▒□▒□▒▒▒□▒▣
    ▣▒□▒▒▒□▒▒□□□▒▒□▒▒▒□▒□▒▒▒□▒▒□□□▒▒□▒▒▒□▒▣
    ▣▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▣
    ▣▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▣
    ▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣""")
def D_ball():
    print("""
    ▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣
    ▣▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▣
    ▣▒□□□□□□□▒▒▒▒□□□□□□▒▒▒□▒▒▒▒▒▒▒□▒▒▒▒▒▒▒▣
    ▣▒□▒▒▒▒▒▒□▒▒□▒▒▒▒▒▒□▒▒□▒▒▒▒▒▒▒□▒▒▒▒▒▒▒▣
    ▣▒□▒▒▒▒▒▒□▒▒□▒▒▒▒▒▒□▒▒□▒▒▒▒▒▒▒□▒▒▒▒▒▒▒▣
    ▣▒□▒▒▒▒▒▒□▒▒□▒▒▒▒▒▒□▒▒□▒▒▒▒▒▒▒□▒▒▒▒▒▒▒▣
    ▣▒□□□□□□□▒▒▒□□□□□□□□▒▒□▒▒▒▒▒▒▒□▒▒▒▒▒▒▒▣
    ▣▒□▒▒▒▒▒▒□▒▒□▒▒▒▒▒▒□▒▒□▒▒▒▒▒▒▒□▒▒▒▒▒▒▒▣
    ▣▒□▒▒▒▒▒▒□▒▒□▒▒▒▒▒▒□▒▒□▒▒▒▒▒▒▒□▒▒▒▒▒▒▒▣
    ▣▒□▒▒▒▒▒▒□▒▒□▒▒▒▒▒▒□▒▒□▒▒▒▒▒▒▒□▒▒▒▒▒▒▒▣
    ▣▒□□□□□□□▒▒▒□▒▒▒▒▒▒□▒▒□□□□□□▒▒□□□□□□▒▒▣
    ▣▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▣
    ▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣""")
a=1
Setting=1
while a!=0:
    if(Setting==1):
        overwrite = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        PLAYER_BOARD = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        COM_BOARD = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        inning = 1
        top='▣'
        bottom='□'
        base1 = '□'
        base2 = '□'
        base3 = '□'
        score = 0
        out = '○○'
        S_ball = '○○○'
        homerun = 0
        display=0
        Setting-=1
    if(out=='●●●'):
        if(top=='▣'):
            if(inning==10):
                for i in range(9):
                    PLAYER_BOARD[9]+=PLAYER_BOARD[i]
            PLAYER_BOARD[inning-1]=score
            top='□'
            bottom='▣'
        else:
            if (inning == 10):
                for i in range(9):
                    COM_BOARD[9] += COM_BOARD[i]
            COM_BOARD[inning-1]=score
            top = '▣'
            bottom = '□'
            inning+=1
        base1 = '□'
        base2 = '□'
        base3 = '□'
        score = 0
        out = '○○'
        homerun = 0
    if(display==1):
        D_hit()
    elif(display==2):
        D_out()
    elif(display==3):
        D_wow()
    elif (display == 4):
        D_ball()
    else:
        D_main()


    print("""
    ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    ■▒▒▒▒▒▒▒▒▒▒▒■                                                  ■
    ■▒▒▒▒▒%s▒▒▒▒▒■PLAYER   | %d | %d | %d | %d | %d | %d | %d | %d | %d | %d  ■
    ■▒▒▒▒▒▒▒▒▒▒▒■---------|----------------------------------------■
    ■▒▒▒▒▒▒▒▒▒▒▒■COMPUTER | %d | %d | %d | %d | %d | %d | %d | %d | %d | %d  ■
    ■▒▒%s▒▒▒▒▒%s▒▒■                                                  ■
    ■▒▒▒▒▒▒▒▒▒▒▒■■■■■■■■■■■■■■■■■■■■■■■■■■■
    ■▒▒▒▒▒▒▒▒▒▒▒■■ %d   INNING   ■■■■■■■B %s■■■■■■■
    ■▒▒▒▒▒▦▒▒▒▒▒■■%s    TOP     ■■■■■■■S ○○  ■■■■■■■
    ■▒▒▒▒▒▒▒▒▒▒▒■■%s   BOTTOM   ■■■■■■■O %s  ■■■■■■■
    ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """ % (base2,PLAYER_BOARD[0],PLAYER_BOARD[1],PLAYER_BOARD[2],PLAYER_BOARD[3],PLAYER_BOARD[4],PLAYER_BOARD[5],PLAYER_BOARD[6],PLAYER_BOARD[7],PLAYER_BOARD[8],PLAYER_BOARD[9],
           COM_BOARD[0],COM_BOARD[1],COM_BOARD[2],COM_BOARD[3],COM_BOARD[4],COM_BOARD[5],COM_BOARD[6],COM_BOARD[7],COM_BOARD[8],COM_BOARD[9],
           base3,base1,
           inning,S_ball,top,bottom,out))
    if(top=='▣'):
        ball=random.randint(0,9)
        #print(ball)
        hit=int(input("HIT? "))
    else:
        hit = random.randint(1, 9)
        #print(hit)
        ball = int(input("Throw a baseball ! "))
    for i in range(3):
        if(ball in overwrite[i]):
            if (hit in overwrite[i]):
                if (hit == ball):
                    display=3
                    homerun+=1
                    break
                else:
                    display = 4
                    if (S_ball == '●●●'):
                        S_ball = '○○○'

                    elif (S_ball == '●●○'):
                        S_ball = '●●●'
                    elif (S_ball == '●○○'):
                        S_ball = '●●○'
                    else:
                        S_ball = '●○○'
                    break
                display=1
                if(base1=='▣'):
                    if(base2=='▣'):
                        if(base3=='▣'):
                            score+=1
                        else:
                            base3='▣'
                    else:
                        base2='▣'
                else:
                    base1='▣'
                break
            else:
                display = 2
                if(out=='●●'):
                    out='●●●'
                elif(out=='●○'):
                    out = '●●'
                else:
                    out = '●○'
                break

    if(homerun==1):
        if (base1 == '▣'):
            if (base2 == '▣'):
                if (base3 == '▣'):
                    score += 4
                else:
                    score += 3
            else:
                score += 2
        else:
            score += 1
        base1 = '□'
        base2 = '□'
        base3 = '□'
        homerun-=1
    if(bottom=='▣'):
        if(inning==9):
            if(PLAYER_BOARD[9]>COM_BOARD[9]):
                print("PLAYER WIN!")
            else:
                print("COMPUTER WIN!")
            break