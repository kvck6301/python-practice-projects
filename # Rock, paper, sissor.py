# Rock, paper, sissor
"""
rock <> paper = paper wins
sissor<>rock = sissor wins
paper<> sissor= paper wins


Workflow
Input from user to choose
Random pick from Computer
print the winner

Case ROCK
user - Rock and comp - rock then TIE 
user - Rock and comp - paper then Paper wins
user - Rock and comp - sissor then Rock wins

Case paper
user - paper  and comp - paper then TIE 
user - paper and comp - Rock then Paper wins
user - paper and comp - sissor then Sissor wins

Case Sissor
user - Sissor  and comp - Sissor then TIE 
user - Sissor and comp - Rock then Rock wins
user - Sissor and comp - paper then Sissor wins


"""

import random
items =["Rock", "Paper","Sissor"]
user_pick = input("enter the user input Rock, Paper, Sissor = : ")
comp_pick = random.choice(items)
print(f"user pick is {user_pick} and comp_pick is {comp_pick}")
if user_pick== comp_pick:
    print("tie")
elif user_pick=="Rock" and comp_pick== "Paper":
     print ("computer wins - Paper ")
elif user_pick== "Rock" and comp_pick== "Sissor":
     print ("Computer wins - Sissor ")

elif user_pick=="Paper" and comp_pick== "Rock":
     print ("User wins - Paper ")
elif user_pick== "Paper" and comp_pick== "Sissor":
     print ("Computer wins - Sissor ")

elif user_pick=="Sissor" and comp_pick== "Rock":
     print ("User wins - Sissor ")
elif user_pick== "Sissor" and comp_pick== "Paper":
     print ("User wins - Sissor ")



    


