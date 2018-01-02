# simple Text based blackjack game

import random
import math 
print("BLACKJACK\n")
answer = input('Do u want to begin session (enter Y or N)- ')
pre_answer ='y'
again = 'y'
suits = ['Hearts','Diamond','Spades','Clubs']
ranks= [1,2,3,4,5,6,7,8,9,'J','K','Q','A']

def draw(face):
    return face[random.randint(0,len(face)-1)]

def valuate(current_rank):
    value = 0
    if current_rank == 'J' or current_rank == 'Q' or current_rank == 'K':
        value = value + 10
    elif current_rank == 'A':
        value = value + 11
    else:
        value = value + int(current_rank)    
    return value

def state(person,suit,rank,value):
    print("{} drew---".format(person), suit, rank)
    print ("Current {} Total---".format(person), value,'\n\n')
    input("hit any key")

def win(score,person, against):
    k = 1
    if score > 21:
        print ("BUST, {} loose so {} WIN".format(person,against))
        return k
    elif value == 21:
        print ("{} win so {} loose".format(person,against))
        return k
    return 0
        
while again == 'y':
    value = 0
    comp_value = 0
    accumulator = 0    
    while answer == 'y':
        if pre_answer== 'y':
            current_suit = draw(suits)
            current_rank = draw(ranks)
            value = value + valuate(current_rank)
            state("Your", current_suit, current_rank, value)
            if win(value,"You","Computer") == 1:
                break
        comp_suit = draw(suits)
        comp_rank=  draw(ranks)
        comp_value = comp_value + valuate(comp_rank)
        state("Computer", comp_suit, comp_rank, comp_value)
        if win(comp_value,"Computer","You") == 1:
            break    
        if pre_answer == 'y':
            pre_answer = input("u want to draw (y or n)-   ")
        if pre_answer == 'n' and comp_value > 17 :
            answer = 'n'
            if comp_value > value:
                print("Computer Wins")
            else:
                print("Player Wins")
    again = input("do u want to play again (y or n)-   ")               