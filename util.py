import math
import random
from Snake import*
import os.path


def sigmoid(x):
    return 1/(1+math.exp(-x))

def rand_neg():
    return 1 if random.random() < 0.5 else -1

def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

def write_population(snakes,generation,pop_id,population_size):
    save_path = 'C:/Users/jerry/Desktop/Coding Projects/Snake/BestSnakes/'
    filename = "pop" + str(pop_id) + "gen" + str(generation) + ".txt"
    complete_name = os.path.join(save_path,filename)
    f = open(complete_name,"w")
    f.write(str(population_size))
    f.write("\n")
    f.write(str(snakes[0].score))
    f.write("\n")
    for i in snakes:
        f.write(i.to_string())
        f.write(' ')
    f.close()


def CalcVisionList(x1,y1,snake_block,dis_width,dis_height,foodx,foody,snake_List):
    #Calculate vision list

    vision_list = [0.0]*24
    distance_searched = 0.0

    startx = x1
    starty = y1

    ##check up
    found_food = False
    found_self = False
    #distance_searched+= snake_block
    #y1 -= snake_block
    while(y1>0):
        if(not found_food and foody == y1):
            found_food=True
            vision_list[0] = 1.0
        point_to_search = []
        point_to_search.append(x1)
        point_to_search.append(y1)
        if not found_self:
            for i in snake_List[:-1]:
                if i == point_to_search:
                    found_self=True
                    vision_list[8] = 1/(distance_searched+0.5)
        distance_searched += snake_block
        y1-= snake_block
    if not found_self:
        vision_list[8] = 1/(distance_searched+0.5)
    vision_list[16] = 1/(distance_searched+0.5)

    ##check right
    distance_searched = 0.0
    x1=startx
    y1=starty
    found_food = False
    found_self = False
    #distance_searched+= snake_block
    #x1 += snake_block
    while(x1<dis_width):
        if(not found_food and foodx == x1):
            found_food=True
            vision_list[1] = 1.0
        point_to_search = []
        point_to_search.append(x1)
        point_to_search.append(y1)
        if not found_self:
            for i in snake_List[:-1]:
                if i == point_to_search:
                    found_self=True
                    vision_list[9] = 1/(distance_searched+0.5)
        distance_searched+= snake_block
        x1+= snake_block
    vision_list[17] = 1/(distance_searched+0.5)
    if not found_self:
        vision_list[9] = 1/(distance_searched+0.5)

    ##check down
    distance_searched = 0.0
    x1=startx
    y1=starty
    found_food = False
    found_self = False
    #distance_searched+= snake_block
    #y1 += snake_block
    while(y1 < dis_height):
        if(not found_food and foody == y1):
            found_food=True
            vision_list[2] = 1.0
        point_to_search = []
        point_to_search.append(x1)
        point_to_search.append(y1)
        if not found_self:
            for i in snake_List[:-1]:
                if i == point_to_search:
                    found_self=True
                    vision_list[10] = 1/(distance_searched+0.5)
        distance_searched += snake_block
        y1 += snake_block
    vision_list[18] = 1/(distance_searched+0.5)
    if not found_self:
        vision_list[10] = 1/(distance_searched+0.5)

    ##check left
    distance_searched = 0.0
    x1=startx
    y1=starty
    found_food = False
    found_self = False
    #distance_searched+= snake_block
    #x1 -= snake_block
    while(x1>0):
        if(not found_food and foodx == x1):
            found_food=True
            vision_list[3] = 1.0
        point_to_search = []
        point_to_search.append(x1)
        point_to_search.append(y1)
        if not found_self:
            for i in snake_List[:-1]:
                if i == point_to_search:
                    found_self=True
                    vision_list[11] = 1/(distance_searched+0.5)
        distance_searched+=snake_block
        x1 -= snake_block
    vision_list[19] = 1/(distance_searched+0.5)
    if not found_self:
        vision_list[11] = 1/(distance_searched+0.5)

    ##check up right
    distance_searched = 0.0
    x1=startx
    y1=starty
    found_food = False
    found_self = False
    #distance_searched+= 1.4142
    #y1 -= 1.0
    #x1 += 1.0
    while(y1>0 and x1 < dis_width):
        if(not found_food and foodx == x1 and foody == y1):
            found_food=True
            vision_list[4] = 1.0
        point_to_search = []
        point_to_search.append(x1)
        point_to_search.append(y1)
        if not found_self:
            for i in snake_List[:-1]:
                if i == point_to_search:
                    found_self=True
                    vision_list[12] = 1/(distance_searched+0.5)
        distance_searched+= 1.4142
        x1 += 1
        y1 -= 1
    vision_list[20] = 1/(distance_searched+0.5)
    if not found_self:
        vision_list[12] = 1/(distance_searched+0.5)

    ##check down right
    distance_searched = 0.0
    x1=startx
    y1=starty
    found_food = False
    found_self = False
    #distance_searched+= 1.4142
    #y1 += 1.0
    #x1 += 1.0
    while(y1<dis_height and x1 < dis_width):
        if(not found_food and foodx == x1 and foody == y1):
            found_food=True
            vision_list[5] = 1.0
        point_to_search = []
        point_to_search.append(x1)
        point_to_search.append(y1)
        if not found_self:
            for i in snake_List[:-1]:
                if i == point_to_search:
                    found_self=True
                    vision_list[13] = 1/(distance_searched+0.5)
        distance_searched+= 1.4142
        x1 += 1
        y1 += 1
    vision_list[21] = 1/(distance_searched+0.5)
    if not found_self:
        vision_list[13] = 1/(distance_searched+0.5)


    ##check down left
    distance_searched = 0.0
    x1=startx
    y1=starty
    found_food = False
    found_self = False
    #distance_searched+= 1.4142
    #y1 += 1.0
    #x1 -= 1.0
    while(y1<dis_width and x1 > 0):
        if(not found_food and foodx == x1 and foody == y1):
            found_food=True
            vision_list[6] = 1.0
        point_to_search = []
        point_to_search.append(x1)
        point_to_search.append(y1)
        if not found_self:
            for i in snake_List[:-1]:
                if i == point_to_search:
                    found_self=True
                    vision_list[14] = 1/(distance_searched+0.5)
        distance_searched+= 1.4142
        x1 -= 1
        y1 += 1
    vision_list[22] = 1/(distance_searched+0.5)
    if not found_self:
        vision_list[14] = 1/(distance_searched+0.5)

    ##check up left
    distance_searched = 0.0
    x1=startx
    y1=starty
    found_food = False
    found_self = False
    #distance_searched+= 1.4142
    #y1 -= 1.0
    #x1 -= 1.0
    while(y1>0 and x1 > 0):
        if(not found_food and foodx == x1 and foody == y1):
            found_food=True
            vision_list[7] = 1.0
        point_to_search = []
        point_to_search.append(x1)
        point_to_search.append(y1)
        if not found_self:
            for i in snake_List[:-1]:
                if i == point_to_search:
                    found_self=True
                    vision_list[15] = 1/(distance_searched+0.5)
        distance_searched+= 1.4142
        x1 -= 1
        y1 -= 1
    vision_list[23] = 1/(distance_searched+0.5)
    if not found_self:
        vision_list[15] = 1/(distance_searched+0.5)
    return vision_list
