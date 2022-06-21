'''considering a game where depending on
defficulty level a player gets a health portion quantity'''

'''difficulty level being 1(easy), 2(medium), 3(hard)'''

import random
difficulty=int(input())
health=50
portion_health=int(random.randint(25,50)/difficulty)
health+=portion_health
print(health)
