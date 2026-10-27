import random
from colorama import Fore, Style
current_HP=20
source=[]
i=1
for k in range(1,53):
    source.append(i)
    if k %4==0:
        i+=1

def st():
    unchanged_HP=current_HP
    print(f"""-------------------------------------------
current_HP: {unchanged_HP}""")
    error=True
    while error==True:
        error=False
        try:
            new_HP=int(input("HP change to('0' to back): "))
        except Exception:
            error=True
    print("-------------------------------------------------------")
    if new_HP!=0:
        return new_HP
    else:
        return unchanged_HP

def menu():
    print("""Welcome to 3 cards game
0. Introduction
1. Play
2. Setting
Enter: '0', '1', '2' to select
---------------------------------------""")

def introduction():
    print(f"""-------------------------------------
After you start the game
You will receive 3 cards and {current_HP} HP
Then take ones digit of the sum of 3 cards as your result
For example:
Your hand: 2 5 10
Your result: 7
So the opponent does
You alse have opportunities to retake your hand
After you choose your best hand, the game will compare 2 results (your and opponent's)
Who is smaller will lose HP, the amount equals to the gap of 2 results
Who dies first will lose the game
----------------------<Note>-----------------------
A=1
J=11
Q=12
K=13
---------------------------------------------------------------------------------------""")
    skip=input("enter anything to continue: ")
    print("--------------------------------------------------------")

def get_user():
    print("--------------------------------------------------")
    print("Your hand: ",end="")
    user=random.sample(source, k=3)
    for k in user:
        if k==1:
            print("A", end=" ")
        elif k==11:
            print("j", end=" ")
        elif k==12:
            print("Q", end=" ")
        elif k==13:
            print("K", end=" ")
        else:
            print(k, end=" ")
    print("")
    return user

while True:
    menu()
    selection=input("Your selection: ")
    while selection not in ["0", "1", "2"]:
        selection=input("Your selection: ")
    if selection=="0":
        introduction()
    elif selection=="2":
        current_HP=st()
    else:
        user_HP=current_HP
        bot_HP=current_HP 
        retake_turn=0
        print("-------------------------------------------------")
        print(Fore.LIGHTMAGENTA_EX +"""0. Continue
1. Retake your hand"""+ Style.RESET_ALL)
        while user_HP>0 and bot_HP>0:
            bot=random.sample(source, k=3)
            bot_result=sum(k for k in bot)%10
            user=get_user()
            user_result=sum(k for k in user)%10
            print(Fore.LIGHTCYAN_EX + f"""Your result: {user_result}
Retake = {retake_turn} times""" + Style.RESET_ALL)
            print("-----------------------------------------------")
            retake=input("Your selection: ")
            while retake not in ["0", "1"]:
                retake=input("Your selection: ")
            while retake =="1":
                retake_turn+=1
                user=get_user()
                user_result= sum(k for k in user)%10
                print(Fore.LIGHTCYAN_EX + f"""Your result: {user_result}
Retake = {retake_turn} times""" + Style.RESET_ALL)
                print("-----------------------------------------------")
                retake=input("Your selection: ")
                while retake not in ["0", "1"]:
                    retake=input("Your selection: ")
            if user_result < bot_result:
                user_HP -=(bot_result-user_result)
                print(Fore.BLACK + "-----------------YOU LOSE---------------------" + Style.RESET_ALL)
            elif user_result > bot_result:
                bot_HP -=(user_result-bot_result)
                print(Fore.YELLOW + "-----------------YOU WIN---------------------" + Style.RESET_ALL)
            else:
                print(Fore.GREEN + "------------------DRAW------------------------" + Style.RESET_ALL)
            print(Fore.RED + f"""Your_HP: {user_HP}
opponent's HP: {bot_HP}""" + Style.RESET_ALL)
        if user_HP<=0:
            print("-------------------------------------------------------------------")
            print(Fore.RED + "                        YOU LOSE" + Style.RESET_ALL)
            print("-------------------------------------------------------------------")
            skip=input("Enter anything to continue: ")
            print("-------------------------------------------------------------------")
        if bot_HP<=0:
            print("-------------------------------------------------------------------")
            print(Fore.RED + f"                       YOU WIN with {retake_turn} retake turns" + Style.RESET_ALL)
            print("-------------------------------------------------------------------")
            skip=input("Enter anything to continue: ")
            print("-------------------------------------------------------------------")