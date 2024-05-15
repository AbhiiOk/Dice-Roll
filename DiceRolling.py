import random
again=True
player1=input("Enter the Player1 name : ")
player2=input("Enter the Player2 name : ")
while again:
    ans=random.randint(1,6)

    roll=input("Its turn of " + player1 + " So you want to roll the dice(y/n): ")
    if roll.lower()=="y":
        print(ans);
    else:
        break
    sroll=input("Its turn of " + player2 + " So you want to roll the dice(y/n): ")
    if sroll.lower()=="y":
        print(ans);
    else:
        break


