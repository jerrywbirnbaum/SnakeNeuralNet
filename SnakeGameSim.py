import time
import random
from Snake import*
from NeuralNetwork import*
from util import*
import numpy as np
import math

def SnakeGameSim(snake_player,seed):

    random.seed(111)
    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)

    dis_width = 400
    dis_height = 400

    snake_block = 10.0


    def gameLoop():
        game_over = False
        game_close = False

        x1 = dis_width / 2.0
        y1 = dis_height / 2.0
        prev_x1 = dis_width / 2.0
        prev_y1 = dis_height / 2.0

        x1_change = 0.0
        y1_change = 0.0

        snake_Head = []
        snake_List = []
        snake_Head.append(x1 + snake_block)
        snake_Head.append(y1)
        snake_Head.append(x1 + 2* snake_block)
        snake_Head.append(y1)
        snake_Head.append(x1 + 3* snake_block)
        snake_Head.append(y1)
        snake_Head.append(x1 + 4* snake_block)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        Length_of_snake = 5
        time_to_live = 200
        score = 0

        first_weights = snake_player.first_weights
        first_biases = snake_player.first_biases
        second_weights = snake_player.second_weights
        second_biases = snake_player.second_biases

        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

        #foodx = dis_width / 5
        #foody=dis_height/4

        while True:
            time_to_live -= 1
            if time_to_live < 0:
                game_close = True


            if game_close:
                score = score*score*(2**Length_of_snake)
                snake_player.score = score
                return score

            #Calculate vision list
            vision_list = CalcVisionList(x1,y1,snake_block,dis_width,dis_height,foodx,foody,snake_List)
            #print(vision_list)

            final_nodes=NeuralNetwork(vision_list,first_weights,first_biases,second_weights,second_biases)

            minVal = -1
            for i in range(4):
                if (final_nodes[0][i] > minVal):
                    direction = i
                    minVal = final_nodes[0][i]
            if direction == 0:
                x1_change = -snake_block
                y1_change = 0
            elif direction == 1:
                x1_change = snake_block
                y1_change = 0
            elif direction == 2:
                x1_change = 0
                y1_change = snake_block
            else:
                x1_change = 0
                y1_change = -snake_block




            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change


            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)


            if len(snake_List) > Length_of_snake:
                del snake_List[0]

            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True



            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                Length_of_snake += 1
                time_to_live += 150

            prev_x1 = x1
            prev_y1 = y1
            score+=1


    score = gameLoop()
    return score
