import numpy as np
import random
from util import*

def NeuralNetwork(vision_list,first_weights,first_biases,second_weights,second_biases):
    first_nodes = np.matrix(vision_list)
    first_biases = np.matrix(first_biases)
    #print(first_nodes)

    second_nodes = first_nodes.dot(first_weights)
    second_nodes = np.add(second_nodes, first_biases)
    second_nodes = np.array(second_nodes)
    #print(second_nodes)
    for i in range(18):
        second_nodes[0][i] = sigmoid(second_nodes[0][i])

    final_nodes = second_nodes.dot(second_weights)
    final_nodes = np.add(final_nodes,second_biases)
    final_nodes = np.array(final_nodes)
    for i in range(4):
        final_nodes[0][i] = sigmoid(final_nodes[0][i])

    return final_nodes
