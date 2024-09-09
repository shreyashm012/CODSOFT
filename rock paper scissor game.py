# ROCK PAPER SCISSOR GAME


print("### RULES ###")
print("The first line of input asks number of Rounds you want in game.\n(Tip:Play odd number of rounds for a fair result.)")
print("Enter: \n'r' for Rock\n'p' for Paper\n's' for Scissor")
print("For each win points will be counted")
print("At the end of all rounds player with most point will win.\n")
import random


def play():
    Human=input("\n\n\nPlease Enter your Name : ")
    n=int(input("Enter number of rounds: "))
    a=0
    h=0
    s=0
    for i in range(0,n):
        sm=["Rock","Paper","Scissor"]
        ai=random.choice(sm)

        n=input("Enter your choice : ")
        d1={"r":1,"p":0,"s":-1}
        d2={1:"Rock",0:"Paper",-1:"Scissor"}
        human=d1[n]
            
        print("You choose: ",d2[human])
        print("Computer choose: ",ai)

        if ai==d2[human]:
            print("It's a Draw \U0001F914")
            a+=1
            print("{} : {}  AI : {}\n".format(Human,h,s))
        else:
            if ai=="Rock" and human==-1:
                print("You Loose \U0001F62C\nTry again ")
                a+=1
                s+=1
                print("{} : {}  AI : {}\n".format(Human,h,s))
            elif ai=="Paper" and human==1:
                print("You Loose \U0001F62C\nTry again ")
                a+=1
                s+=1
                print("{} : {}  AI : {}\n".format(Human,h,s))
            elif ai=="Scissor" and human==0:
                print("You Loose \U0001F62C\nTry again ")
                a+=1
                s+=1
                print("{} : {}  AI : {}\n".format(Human,h,s))
            elif ai=="Rock" and human==0:
                print("You Won \U0001F604")
                a+=1
                h+=1
                print("{}: {}  AI : {}\n".format(Human,h,s))
            elif ai=="Paper" and human==-1:
                print("You Won \U0001F604")
                a+=1
                h+=1
                print("{} : {}  AI : {}\n".format(Human,h,s))
            elif ai=="Scissor" and human==1:
                print("You Won \U0001F604")
                a+=1
                h+=1
                print("{} : {}  AI : {}\n".format(Human,h,s))
            else:
                print("Invalid input!!\n")
    if h>s:
        print("\U0001F973  \U0001F973  \U0001F973  \U0001F973  \U0001F973  \U0001F973  \U0001F973 ")
        print("\U0001F60E You Won \U0001F60E\nFinal Score :\n{} : {}\nAI : {}".format(Human,h,s))
        play_again()
    elif h==s:
        print("\U0001F610 It's a Tie \U0001F610	\nFinal Score :\n{} : {}\nAI : {}".format(Human,h,s))
        play_again()
    else:
        print("\U0001F630 You Lost \U0001F630\nFinal Score :\n{} : {}\nAI : {}".format(Human,h,s))
        play_again()


                
def play_again():
    print("\ndo you want to play again (Yes/No)")
    t=input("Press y for Yes\nn for no : ")
    if t=="y":
        play()
    else:
        print("Thanks for Playing.")

        
play() 
   




