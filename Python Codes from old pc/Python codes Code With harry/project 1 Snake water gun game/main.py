import random
a = random.randint(1,3)
if a == 1:
    comp = 's'
elif a== 2:
    comp = 'w'
elif a == 3:
    comp = 'g'

print("Computer has choosen!!Enter your choice!! s for Snake, w for Water, g for Gun ")
you = input()

if you == 's':
    if comp == 'w':
        print("You win because you choose snake and computer choose water")
    elif comp == 'g':
        print("You lose becuase you choose snake and computer choose gun")
    elif comp == 's':
        print("Tied because you choose snake and computer also choose snake")

elif you == 'w':
    if comp == 'g':
        print("You win becuase you choose water and computer choose gun")
    elif comp == 's':
        print("You lose because you choose water and computer choose snake")
    elif comp == 'w':
        print("Tied because you choose water and computer also choose water")

elif you == 'g':
    if comp == 's':
        print("You win because you choose gun and computer choose snake")
    elif comp == 'w':
        print("You lose becuase you choose gun and computer choose water")
    elif comp == 'g':
        print("Tied because you choose g and computer also choose gun")

else:
    print("Wrong input")
# Snake water gun game