import random
# snake drinks water
# water dousses gun
# gun shoots snake

rules={
"snake":"water",
"water":"gun",
"gun":"snake"

}
count,player_score,computer_score=0,0,0
number=int(input("how many times do u wanna play ?"))

while count<number:

    player=input(" player:(snake/water/gun) ")
    computer=random.choice(["snake","water","gun"])

    if player not in rules:
        print("invalid input")
        continue

    elif player==computer:
        print('draw')

    elif rules[player]==computer :
        print("player  wins")
        player_score+=1  

    else: 
        print("Computer wins")      
        computer_score+=1

    count+=1
    print("            SCORE BOARD          ") 
    print(f"player's score is :{player_score}")   
    print(f"computer's score is  :{computer_score}")     

if player_score>computer_score:
    print("congratulations!player wins this round")

elif player_score<computer_score:
    print("congratulations!computer wins this round")

elif player_score==computer_score :
    print("draw!yey")        