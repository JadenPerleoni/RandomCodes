playerChoice = ''
randomNumber = 0
coinLand = ''
playerChoice = input('Heads or tails')
playerChoice = (playerChoice.lower())
print (f'You chose {playerChoice}')

import random
 
randomNumber = random.randint(1,10)
if (randomNumber) >= 5:
    coinLand = "heads"
else:
    coinLand = "tails"

if (playerChoice) == (coinLand):
    print('You chose correctly!')

else:
    print('You chose WRONG!')
