from random import randint as rd
from random import sample as sp
from random import choices as ch
source=list(str(i) for i in range(10))
def menu():
    print("""Welcome too guess the password game
--------------Select mode-------------
0. Introduction
1. Easy
2. Medium
3. Hard
4. Extremely hard
--------------------------------------""")

def introduction():
    print("""-----------------------------------
There is a sequence number with 5 letters
You have to guess it
1. Mode
<Easy> - There are 5 different numbers
<Medium> - There are 5 numbers
<Hard> - There are 5 different numbers
<Extremely hard> - There are 5 numbers)
2. Note
- With easy and medium mode, after finishing your guess, you will know 
which number is wrong-placed, right-placed or not appeared
- With hard and extremely hard mode, after finishing your guess you will know 
the number of right-placed numbers
3. Signs
V: Right-placed number
O: wrong-placed number
X: not-appeared number
x/5: there are x right-placed numbers
------------------------------------------------""")
    skip=input("Enter anything to continue: ")
    print("-----------------------------------------------")

def player():
    def get_player():
        player=[]
        user=list(input("Your selection: "))
        for k in user:
            if k !=" ":
                player.append(k)
        return player
    player=get_player()
    def check_str():
        str_detected=False
        for k in player:
            if k not in source:
                str_detected=True
                break
        return str_detected
    str_detected=check_str()
    while len(player)!=5 or str_detected==True:
        player=get_player()
        str_detected=check_str()
    return player

def easy_medium():
    print("""-------------------------------------
Password: X X X X X""")
    turn=1
    def check():
        result=[]
        pw=[]
        for k in range(0,5):
            if user[k]==password[k]:
                result.append("V")
                pw.append(user[k])
            elif user[k]!=password[k] and password.count(user[k])!=0:
                result.append("O")
                pw.append("X")
            else:
                result.append("X")
                pw.append("X")
        print(f"Turn {turn}:   ",end="")
        for k in result:
            print(k,end=" ")
        print("")
        print("Password: ",end="")
        for k in pw:
            print(k,end=" ")
        print("\n----------------------------------------------")
        return result
    user=player()
    result=check()
    while result.count("V")!=5:
        turn+=1
        user=player()
        result=check()
    print(f"""--------------VICTORY---------------------
You took {turn} turn to finish the game""")
    skip=input("enter anything to continue: ")
    print("------------------------------------------------")

def hard_exhard():
    print("""---------------------------------------------
Password: X X X X X""")
    turn=1
    def check():
        V_detected=0
        for k in range(0,5):
            if user[k]==password[k]:
                V_detected+=1
        return V_detected
    user=player()
    result=check()
    print(f"turn {turn}: {result}/5")
    print("--------------------------------------------")
    while result!=5:
        turn+=1
        user=player()
        result=check()
        print(f"turn {turn}: {result}/5")
        print("--------------------------------------------")
    print(f"""VICTORY
You took {turn} turn to finish the game""")
    skip=input("Enter anything to continue: ")
    print("------------------------------------------------")  

while True:
    menu()  
    player_selection=input("Your selection: ")
    while player_selection not in source[0:5]:
        player_selection=input("Error, try again: ")
    if player_selection=="0":
        introduction()
    elif player_selection=="1":
        password=sp(source, k=5)
        easy_medium()
    elif player_selection=="2":
        password=ch(source, k=5)
        easy_medium()
    elif player_selection=="3":
        password=sp(source, k=5)
        hard_exhard()
    else:
        password=ch(source, k=5)
        hard_exhard()