'''
1 for snake
-1 for water
0 for gun
'''
import random

computer=random.choice([1,-1,0])
user=input("Enter the choice:")
userdict={"s":1,"w":-1,"g":0}
int_choice={1:"snake",-1:"water",0:"gun"}

you=userdict[user]
you_1=int_choice[you]

print(f"You chose {you_1}\nComputer chose {int_choice[computer]}")

if(computer==you):
    print("It's a draw!")
else:
    #LOGIC : COMPUTER-YOU WHICH ARE VARIABLES GIVE A SPECIFIC INT

    # if(computer==-1 and you==1):  computer-you=-2
    #     print("You win!")
    # elif(computer==-1 and you==0): computer-you=-1
    #     print("You lose!")        
    # elif(computer==1 and you==-1): computer-you=2
    #     print("You lose!")
    # elif(computer==1 and you==0): computer-you=1 
    #     print("You win!")        
    # elif(computer==0 and you==-1): computer-you=1
    #     print("You win!")
    # elif(computer==0 and you==1): computer-you=-1
    #     print("You lose!")  
    
    if((computer-you)==-2 or (computer-you)==1):
        print("You win!")
    else:
        print("You lose!")    