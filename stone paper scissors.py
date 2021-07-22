import random
choice=['rock','paper','scissors']
while True:
    print('WELCOME !')
    user_count=0
    comp_count=0
    for i in range(1,4):
        print("ROUND-",i)
        print("ENTER A VALUE 1.ROCK 2.PAPER 3.SCISSOR")
        your_choice=int(input())
        
        if(your_choice==1):
            print("you have selected rock")
            your_choice="rock"
        elif(your_choice==2):
            print("you have selected paper")
            your_choice="paper"
        elif(your_choice==3):
            print("you have selected scissor")
            your_choice="scissor"
        else:
            print("WRONG CHOICE,SELECT AGAIN")
            break
        
        computerChoice= random.choice(choice) 
        print("Computer selectes",computerChoice)
        
        if(your_choice==computerChoice):
            print("Draw")
        elif((your_choice=='paper'and computerChoice=='rock')or(your_choice=='rock'and computerChoice=='scissor')or(your_choice=='scissor'and computerChoice=='paper')):
            user_count=user_count+1
        elif((your_choice=='rock'and computerChoice=='paper')or(your_choice=='scissor'and computerChoice=='rock')or(your_choice=='paper'and computerChoice=='scissor')):
            comp_count=comp_count+1 
        
    if(user_count>comp_count):
        print("YOU WIN") 
    elif(user_count<comp_count):
        print("COMPUTER WINS")
    else:
        print("DRAW")
    print("DO YOU WANT TO PLAY AGAIN ? YES OR NO ?")  
    x=input()
    if(x=='yes' or x=='YES' or x=='Yes'):
     continue
    else:  
        break           