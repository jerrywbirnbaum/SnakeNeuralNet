import numpy as np
import random
from util import rand_neg
import re

class Snake:
    first_weights=[]
    first_biases = []
    second_weights=[]
    second_biases=[]
    score = 0

    def __init__(self,first_weights,first_biases,second_weights,second_biases):
        if not first_weights:
            self.first_biases = np.empty((1,18),dtype=np.float32)
            self.first_biases.fill(0)
            self.first_weights = np.empty((24,18),dtype=np.float32)
            self.first_weights.fill(0)
            self.second_biases = np.empty((1,4),dtype=np.float32)
            self.second_biases.fill(0)
            self.second_weights = np.empty((18,4),dtype=np.float32)
            self.second_weights.fill(0)

            for i in range (24):
                for j in range(18):
                    self.first_weights[i,j] += random.random() * rand_neg() *5
            for i in range(18):
                self.first_biases[0,i] += random.random()* rand_neg()*5
            for i in range (18):
                for j in range(4):
                    self.second_weights[i,j] += random.random()* rand_neg()*5
            for i in range(4):
                self.second_biases[0,i] += random.random()* rand_neg()*5

        else:

            self.first_biases = np.empty((1,18),dtype=np.float32)
            self.first_biases.fill(0)
            self.first_weights = np.empty((24,18),dtype=np.float32)
            self.first_weights.fill(0)
            self.second_biases = np.empty((1,4),dtype=np.float32)
            self.second_biases.fill(0)
            self.second_weights = np.empty((18,4),dtype=np.float32)
            self.second_weights.fill(0)
            print(self.first_biases)

            for i in range (24):
                for j in range(18):
                    self.first_weights[i,j] = first_weights[0]
                    first_weights.pop(0)
            for i in range(18):
                self.first_biases[0,i] = first_biases[0]
                first_biases.pop(0)
            for i in range (18):
                for j in range(4):
                    self.second_weights[i,j] =second_weights[0]
                    second_weights.pop(0)
            for i in range(4):
                self.second_biases[0,i] =second_biases[0]
                second_biases.pop(0)

    def __lt__(self,other):
        return self.score < other.score

    def mutate(self, mutation_rate):
        for i in range (24):
            for j in range(18):
                if(random.random()<mutation_rate):
                    self.first_weights[i,j] += (random.random() * rand_neg())
        for i in range(18):
            if(random.random()<mutation_rate):
                self.first_biases[0,i] += (random.random()* rand_neg())
        for i in range(18):
            for j in range(4):
                if(random.random()<mutation_rate):
                    self.second_weights[i,j] += (random.random()* rand_neg())
        for i in range(4):
            if(random.random()<mutation_rate):
                self.second_biases[0,i] += (random.random()* rand_neg())

    def to_string(self):
        neural_net = ""
        for i in range (24):
            for j in range(18):
                neural_net += str(self.first_weights[i,j])
                neural_net += ' '
            #neural_net += "\n"
        neural_net += "\n"
        for i in range(18):
            neural_net += str(self.first_biases[0,i])
            neural_net += ' '
        neural_net += "\n"
        for i in range(18):
            for j in range(4):
                neural_net += str(self.second_weights[i,j])
                neural_net += ' '
            #neural_net += "\n"
        neural_net += "\n"
        for i in range(4):
            neural_net += str(self.second_biases[0,i])
            neural_net += ' '
        neural_net += "\n"
        return neural_net

def have_child(father,mother):

    child = Snake([],[],[],[])
    for i in range (24):
        for j in range(18):
            if random.random() < 0.5:
                child.first_weights[i,j] = father.first_weights[i,j]
            else:
                child.first_weights[i,j] = mother.first_weights[i,j]
    for i in range(18):
        if random.random() < 0.5:
            child.first_weights[0,i] = father.first_weights[0,i]
        else:
            child.first_weights[0,i] = mother.first_weights[0,i]

    for i in range (18):
        for j in range(4):
            if random.random() < 0.5:
                child.first_weights[i,j] = father.first_weights[i,j]
            else:
                child.first_weights[i,j] = mother.first_weights[i,j]

    for i in range(4):
        if random.random() < 0.5:
            child.first_weights[0,i] = father.first_weights[0,i]
        else:
            child.first_weights[0,i] = mother.first_weights[0,i]
    return child

def read_population(filename):
    f = open(filename,"r")
    file_output = f.readlines()
    population_size = int(file_output[0])
    score = int(file_output[1])
    print(population_size)
    print(score)
    snakes = []
    for i in range(population_size):
        first_weights = file_output[2]
        list_first_weights = first_weights.split()
        first_biases = file_output[3]
        list_first_biases = first_biases.split()
        second_weights = file_output[4]
        list_second_weights = second_weights.split()
        second_biases = file_output[5]
        list_second_biases = second_biases.split()
        snakes.append(Snake(list_first_weights,list_first_biases,list_second_weights,list_second_biases))
    return snakes
