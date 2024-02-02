#-----------------Code for a card game that generates tables and graphs of your game-----------------#
# V1
# uses while loops and if/else statements for menues and dataframes such as dictionaries to store the cards
# uses Pandas and Seaborn modules to generate yables and graphs
# room for expansion with text based adventure game if you try to leave while in debt

import random as rd
import time

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
     
#get your pack of cards as a dictionary
pack = {"Two of Clubs": 2,
        "Two of Diamonds": 2,
        "Two of Hearts": 2,
        "Two of Spades": 2,
        "Three of Clubs": 3,
        "Three of Diamonds": 3,
        "Three of Hearts": 3,
        "Three of Spades": 3,
        "Four of Clubs": 4,
        "Four of Diamonds": 4,
        "Four of Hearts": 4,
        "Four of Spades": 4,
        "Five of Clubs": 5,
        "Five of Diamonds": 5,
        "Five of Hearts": 5,
        "Five of Spades": 5,
        "Six of Clubs": 6,
        "Six of Diamonds": 6,
        "Six of Hearts": 6,
        "Six of Spades": 6,
        "Seven of Clubs": 7,
        "Seven of Diamonds": 7,
        "Seven of Hearts": 7,
        "Seven of Spades": 7,
        "Eight of Clubs": 8,
        "Eight of Diamonds": 8,
        "Eight of Hearts": 8,
        "Eight of Spades": 8,
        "Nine of Clubs": 9,
        "Nine of Diamonds": 9,
        "Nine of Hearts": 9,
        "Nine of Spades": 9,
        "Ten of Clubs": 10,
        "Ten of Diamonds": 10,
        "Ten of Hearts": 10,
        "Ten of Spades": 10,
        "Jack of Clubs": 11,
        "Jack of Diamonds": 11,
        "Jack of Hearts": 11,
        "Jack of Spades": 11,
        "Queen of Clubs": 12,
        "Queen of Diamonds": 12,
        "Queen of Hearts": 12,
        "Queen of Spades": 12,
        "King of Clubs": 13,
        "King of Diamonds": 13,
        "King of Hearts": 13,
        "King of Spades": 13,
        "Ace of Clubs": 14,
        "Ace of Diamonds": 14,
        "Ace of Hearts": 14,
        "Ace of Spades": 14,}

discard_pile = []

results_record = []

wins_and_losses = []

pot = []


# gambling function
# calculate a win or loss as a function of whether they were correct, how much by, and how much they staked
def gamble(result, stake, distance):
    change = (result * (stake + distance))
    return change
    
#Pick a random card
card = rd.choice(list(pack)) 

menu = ""
while True :
    print("a. deposit money")
    print("b. play card game")
    print("c. cash out")
    print("d. enter the nerve centre to analyse your performance")
    print("q. quit")

    print(f"current pot £{sum(pot)}")

    menu = input("pick from above list : ")

    
    
    if menu == "q":
        print("you leave the casino")
        break

    if menu == "a":
        deposit = int(input("please enter how much you will deposit : £"))
        pot.append(deposit)


    while menu == "b": 
        
        leave = input("Welcome to the casino, here you will play a simple card game\n\ntype 'exit' to go to main menu\nhit any other key to continue : ")

        if leave == "exit":
            break

        if len(discard_pile) > 52:
            break        
        #get the first random card and place on the table
        if discard_pile == []:
        
            comp = pack.get(card)

            discard_pile.append(comp)

            pack.pop(card)

            time.sleep(1)

            if card not in pack:
                print(f"\nCard removed from deck\n it's a {card}")


        # use the previous card as the new comparetor
        else:
            
            new = pack.get(next_card)

            discard_pile.append(new)

            pack.pop(next_card)
            
            if next_card not in pack:
                print(f"\n{next_card} was removed from the deck\nand placed on the table")

        
        next_card = rd.choice(list(pack))

        time.sleep(1)

        
        #ask for prediction 
        punt_input = " "
        while True:
            punt_input = input("\nWill the next card be higher, lower, or the same value? H / L / S ?\n")

            punt = punt_input.upper()

            if punt == "H":
                if (discard_pile[-1]) < (pack[next_card]):
                    #print(f"you were correct!")
                    results_record.append(1) 
                    wins_and_losses.append("win")
                    
                else:
                    #print("you were incorrect")
                    results_record.append(-1)
                    wins_and_losses.append("lose")
                    

            elif punt == "L":
                if (discard_pile[-1] > pack[next_card]):
                    #print("you were correct! the next card was lower")
                    results_record.append(1) 
                    wins_and_losses.append("win")
                    
                else:
                    #print("you were incorrect")
                    results_record.append(-1)
                    wins_and_losses.append("lose")
                    

            elif punt == "S":
                if (discard_pile[-1] == pack[next_card]):
                    #print("you were correct! the cards have the same value")
                    results_record.append(1) 
                    wins_and_losses.append("win")
                    
                else:
                    #print("you were incorrect")
                    results_record.append(-1) 
                    wins_and_losses.append("lose")
                    

            else:
                print("invalid choice")
                continue
            
            #how much they want to gamble
            stake = int(input("\nHow much do you stake?\n£"))
          
            time.sleep(0.5)

            print(f"\nthe next card drawn is {next_card}")


            distance = ((discard_pile[-1]) - (pack[next_card]))**2 
            
            pot_change = gamble(results_record[-1], stake, int(distance))
            
            print(f"you {wins_and_losses[-1]} £{pot_change}!")
            
            pot.append(pot_change)

            print(f"your pot stands at £{sum(pot)}\n")
            #print(f"your record is {wins_and_losses}")
            break

    while menu == "c":
        if sum(pot) >= 0:
            print(f"you have cashed out with \n £{sum(pot)}\n")
            pot = pot.clear()
            pot = []
            break
        else:
            print("...")
            time.sleep(0.5)
            print("... you owe us money")
            time.sleep(0.5)
            print("bye!")
            break
        # add a text adventure game here

    while menu == "d":
        print("\nwelcome to the nerve centre! Here you can analyse your performance and make strategy")
        answer = input("would you like to return to main menu? 'y' \nor see the nerve center menu 'n' : \n")
        if answer == "y":
            break

        else:

            while True:
                print("r. for a record of your wins and losses")
                print("t. print a table of your plays")
                print("g. for a graph of your game")
                print("q. to navigate to menu")
                choice = input("pick letter for intel : \n")

                if choice == "r":

                    print(f"\nyour record is {wins_and_losses}\n")
                    break

                elif choice == "t":

                    df = pd.DataFrame(zip(pot, wins_and_losses), columns = ["pot", "result"])
                    df.index = df.index + 1
                    df.index.name = "play"

                    print(df)

                    print("\n The above logs the value of your pot over time\n")
                    break

                elif choice == "g":
                    sns.set_theme()
                    sns.set_style("darkgrid")
                    sns.set_style('ticks')
                    sns.set_context("paper")
                    
                    df = pd.DataFrame(pot, columns = ["pot"])
                    df.index = df.index + 1
                    plt.xlabel("plays")
                    plt.ylabel("pot_value")

                    graph = sns.lineplot(data=df, x=df.index, y="pot")
                    plt.show()

                else:
                    break   
# ------------------END------------------------------
