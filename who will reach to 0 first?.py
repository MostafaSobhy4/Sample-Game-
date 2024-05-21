from math import sqrt
from random import randint
print("\n# Welcome To Subtract A Square Game #")   #Welcome Message

#The Game:
while True:   #lets the user choose wether to insert or randomize the number of coins
    choice =input('\nplease select a valid choice from below:\n'
        '(a) choose a random number of coins.\n'
        '(b) decide the number of coins.\n')
    if choice == 'a' or choice =='b':break

if choice == 'a':    #ensures that the randomized coins are not a square number between 10and 100
    while True:
        coins = randint(10,1000)
        if coins != int(sqrt(coins))**2:break
else:
    coins = int(input("Please Enter The Number Of Coins: "))
       
print(f"\nThe Number Of Coins is: {coins}")


while (coins>0):

    player1_coins = int(input("Player 1\'s Turn: "))   #player1_coins=> the number that player1 will removing coins from the pile
    while player1_coins != int(sqrt(player1_coins))**2  or  player1_coins>coins  or  player1_coins==0:
        player1_coins = int(input(f"Please Enter a Non-Zero Square Number less than {coins} : "))

    coins -= player1_coins   #removes the drawn coins from the pile and updates the game status
    print(f"\nthe Curent Number Of Coins is: {coins}")


    if coins==0:   #declares player is the winner if he is last to pick
       print("Player 1 Wins!")
       exit()


    player2_coins = int(input("Player 2\'s Turn: "))    #player2_coins=> the number that player2 will removing coins from the pile
    while player2_coins != int(sqrt(player2_coins))**2  or  player2_coins>coins or player2_coins==0:
        player2_coins = int(input(f"Please Enter a Non-Zero Square Number less than {coins} : "))

    coins -= player2_coins   #removes the drawn coins from the pile and updates the game status
    print(f"\nthe Curent Number Of Coins is: {coins}")

print("Player 2 Wins!")  #declares player is the winner if he is last to pick
