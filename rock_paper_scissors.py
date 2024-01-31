import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
graphic_list = [rock, paper, scissors]
rps = {1: "rock", 2: "paper", 3: "scissors"}
conditions = {"rock-paper": "Lose", "rock-scissors": "Win", "paper-rock": "Win", "paper-scissors": "Lose", "scissors-rock": "Lose", "scissors-paper": "Win"}

users_choice = int(input("Choose:\n1 (rock)\n2 (paper)\n3 (scissors)\n"))
user_chose = rps[users_choice]

computers_choice = random.randint(1,3)
computer_chose = rps[computers_choice]



print(f"You chose {user_chose} and the computer chose {computer_chose}")
print(f"{graphic_list[users_choice-1]} vs {graphic_list[computers_choice-1]}")

game_instance = user_chose + "-" + computer_chose

if game_instance in conditions:
    print(f"You {conditions[game_instance]}")
else:
    print("It is a tie")

