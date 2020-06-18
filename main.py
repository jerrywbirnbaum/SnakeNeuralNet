from SnakeGame import*
from Snake import*
import copy
from util import*
from SnakeGameSim import*
import os.path


pygame.init()

save_path = 'C:/Users/jerry/Desktop/Coding Projects/Snake/BestSnakes'

generation = 1
generation_one=[]
generation_spare = []
generation_size = 2000
mutation_rate = 0.01

for i in range(generation_size):
    generation_one.append(Snake([],[],[],[]))


for j in range(250):
    for i in range(generation_size):
            SnakeGameSim(generation_one[i],generation)
    generation_one.sort()
    best_snake = copy.deepcopy(generation_one[generation_size-1])
    #SnakeGame(best_snake,40,generation)
    worst_snake = generation_one[0]
    mid_snake = generation_one[int(generation_size/2)]
    print("Generation ", generation)
    print(best_snake.score)
    write_population([best_snake],generation,"best",1)
    random.shuffle(generation_one)
    total_score=0
    for i in generation_one:
        total_score += i.score
    for i in range(generation_size-1):
        cutoff_score = random.randrange(int(total_score))
        current_sum = 0
        for j in generation_one:
            current_sum+= j.score
            if(current_sum >= cutoff_score):
                father = j
                break
        cutoff_score = random.randrange(int(total_score))
        current_sum = 0
        for j in generation_one:
            current_sum+= j.score
            if(current_sum >= cutoff_score):
                mother = j
                break
        child = have_child(father,mother)
        generation_spare.append(child)
    generation_one.clear()
    generation_one.append(best_snake)
    for i in generation_spare:
        generation_one.append(i)
    generation_spare.clear()
    for i in range(1,generation_size):
        generation_one[i].mutate(mutation_rate)
    generation += 1



pygame.quit()
quit()
