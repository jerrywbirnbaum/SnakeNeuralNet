from SnakeGame import*
from Snake import*
import copy
from util import*

filename = "BestSnakes\popbestgen161.txt"

snakes = read_population(filename)
pygame.init()

print(SnakeGame(snakes[0],40,111))
