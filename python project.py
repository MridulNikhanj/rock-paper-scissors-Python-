import random

Moves=["rock","paper","scissors"]

sum_computer=0
sum_player=0

print("GAME: ROCK/PAPER/SCISSORS\n")
while True:
    computer=Moves[random.randint(0,2)]
    player=input("Player(rock/paper/scissors)?: ").lower()
    if (player=="rock" or player=="paper" or player=="scissors"):
        print("computer:",computer)

        """combination of moves by player and computer""" 

        if player==computer:
            print("Tie")
        
            ask=input("do u want to play more(yes/no): ").lower()
            if ask=="yes":
                continue
            else:
                break

        elif player=="rock":
            if computer=="paper":
                print("you loose this time!")
                sum_computer=sum_computer+1
            else:
                print("you win this time!")
                sum_player=sum_player+1

            ask=input("do u want to play more(yes/no): ").lower()
            if ask=="yes":
                continue
            else:
                break


        elif player=="paper":
            if computer=="scissors":
                print("you loose this time!")
                sum_computer=sum_computer+1
            else:
                print("you win this time!")
                sum_player=sum_player+1

            ask=input("do u want to play more(yes/no): ").lower()
            if ask=="yes":
                continue
            else:
                break


        elif player=="scissors":
            if computer=="rock":
                print("you loose this time!")
                sum_computer=sum_computer+1
            else:
                print("you win this time!")
                sum_player=sum_player+1

            ask=input("do u want to play more(yes/no): ").lower()
            if ask=="yes":
                continue
            else:
                break
            

    else:
        print("wrong input by player!! re-enter your move")
        

print()
print("Final Scores:")
print("sum_computer: ",sum_computer)
print("sum_player: ",sum_player)
        


