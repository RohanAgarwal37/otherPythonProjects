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

#Write your code below this line 👇
images=[rock,paper,scissors]
rps = ["Rock", "Paper", "Scissors"]

myChoice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
cpuChoice = random.randint(0,2)

if myChoice<0 or myChoice>=3:
    print("You chose an invalid input")
elif myChoice==0 and cpuChoice==2:
    print(f"You chose: {rps[myChoice]}\n{images[myChoice]}")
    print(f"CPU chose: {rps[cpuChoice]}\n{images[cpuChoice]}")
    print("You won!!")
elif cpuChoice==0 and myChoice==2:
    print(f"You chose: {rps[myChoice]}\n{images[myChoice]}")
    print(f"CPU chose: {rps[cpuChoice]}\n{images[cpuChoice]}")
    print("Cpu won!!")
elif cpuChoice>myChoice:
    print(f"You chose: {rps[myChoice]}\n{images[myChoice]}")
    print(f"CPU chose: {rps[cpuChoice]}\n{images[cpuChoice]}")
    print("Cpu won!!")
elif myChoice > cpuChoice:
    print(f"You chose: {rps[myChoice]}\n{images[myChoice]}")
    print(f"CPU chose: {rps[cpuChoice]}\n{images[cpuChoice]}")
    print("You won!!")
else:
    print(f"You chose: {rps[myChoice]}\n{images[myChoice]}")
    print(f"CPU chose: {rps[cpuChoice]}\n{images[cpuChoice]}")
    print("It is a Draw!!")
