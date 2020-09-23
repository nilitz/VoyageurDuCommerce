import numpy as np
import math
from Node import Node
from Link import Link
from Graphe import Graphe
import random
import matplotlib.pyplot as plt
import time
from mpl_toolkits.mplot3d import Axes3D


def generate_array_nodes():
    array_nodes = []
    for i in range(10):
        node = Node(i, random.randrange(-4, 5), random.randrange(-4, 5), random.randrange(-4, 5))
        array_nodes.append(node)
    return array_nodes


def generate_array_links(array_nodes):
    array_links = []
    for i in range(9):
        for j in range(i, 9):
            link = Link(array_nodes[i], array_nodes[j + 1])
            array_links.append(link)
    return array_links


def launch():
    array_nodes = generate_array_nodes()
    array_links = generate_array_links(array_nodes)
    graph = Graphe(array_nodes, array_links)
    links = prim(graph)
    display(links, graph)
    travel2(links)


def display(prim, graph):
    plt.figure()
    ax = plt.axes(projection='3d')

    for node in graph.array_nodes:
        ax.plot(node.position[0], node.position[1], node.position[2], 'bo')
    for link in graph.array_links:
        ax.plot([link.node_a.position[0], link.node_b.position[0]],
                [link.node_a.position[1], link.node_b.position[1]],
                [link.node_a.position[2], link.node_b.position[2]])

    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])
    ax.set_zlim([-5, 5])

    plt.show()

    time.sleep(1)

    plt.figure()
    ax = plt.axes(projection='3d')

    for node in graph.array_nodes:
        ax.plot(node.position[0], node.position[1], node.position[2], 'bo')
    for link in prim:
        ax.plot([link.node_a.position[0], link.node_b.position[0]],
                [link.node_a.position[1], link.node_b.position[1]],
                [link.node_a.position[2], link.node_b.position[2]])

    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])
    ax.set_zlim([-5, 5])

    plt.show()


def higher_weight(array_links):
    max = 15
    choosen_link = Link
    for i in range(len(array_links)):
        if array_links[i].weight < max:
            max = array_links[i].weight
            choosen_link = array_links[i]
        elif array_links[i].weight == max:
            if random.randrange(0, 2) == 1:
                max = array_links[i].weight
                choosen_link = array_links[i]
    return choosen_link


def prim(graph):
    first_node_pos = random.randrange(0, 10)
    return check_weights(first_node_pos, graph)


def all_nodes_checked(array):
    if len(array) == 0:
        return 0
    return 1


def check_weights(first_node_pos, graph):
    candidates = graph.array_nodes
    positions = []
    passed_nodes = []

    while all_nodes_checked(candidates):
        temporary = []
        for i in range(len(graph.array_nodes)):
            if graph.array_nodes[i].name == first_node_pos:
                passed_nodes.append(graph.array_nodes[i])
        for i in range(0, 45):
            if (graph.array_links[i].node_a in passed_nodes) and (graph.array_links[i].node_b in candidates):
                temporary.append(graph.array_links[i])
            elif (graph.array_links[i].node_b in passed_nodes) and (graph.array_links[i].node_a in candidates):
                temporary.append(graph.array_links[i])

        new_link = higher_weight(temporary)

        if new_link.node_a in candidates:
            candidates.remove(new_link.node_a)
            passed_nodes.append(new_link.node_a)
        if new_link.node_b in candidates:
            candidates.remove(new_link.node_b)
            passed_nodes.append(new_link.node_b)

        positions.append(new_link)

    return positions


def all_links_checked(array):
    if len(array) < 18:
        return 1
    return 0


def only_one(node, array):
    count = 0
    for i in range(len(array)):
        if array[i].node_a == node:
            count = count + 1
        elif array[i].node_b == node:
            count = count + 1
    print(count)
    return count


def travel2(array_links):
    array_stock = []
    array_travel = []

    actual_link = array_links[0]
    actual_point = actual_link.node_a
    while all_links_checked(array_stock):
        temporary = []
        for link in range(len(array_links)):

            if array_links[link].node_a == actual_point:
                if array_stock.count(array_links[link]) < 2:
                    temporary.append([array_links[link], array_stock.count(array_links[link]), 'b'])
            elif array_links[link].node_b == actual_point:
                if array_stock.count(array_links[link]) < 2:
                    temporary.append([array_links[link], array_stock.count(array_links[link]), 'a'])

        print('-----TEMP----')
        for i in range(len(array_stock)):
            print(array_stock[i], array_stock.count(array_stock[i]))
        print('---------')

        if len(temporary) != 0:
            for i in range(len(temporary)):
                if i == 0:
                    the_choosen_one = temporary[i]
                elif temporary[i][1] < the_choosen_one[1]:
                    the_choosen_one = temporary[i]

            array_stock.append(the_choosen_one[0])
            actual_link = the_choosen_one[0]
            if the_choosen_one[2] == 'a':
                actual_point = actual_link.node_a
                if actual_point not in array_travel :
                    array_travel.append(actual_point)
            else:
                actual_point = actual_link.node_b
                if actual_point not in array_travel:
                    array_travel.append(actual_point)

            print('----1-----')
            print(temporary, ' | ')
            print('----2-----')
            for i in range(len(array_stock)):
                print(array_stock[i], array_stock.count(array_stock[i]))
            print('---------')
            '''
            plt.figure()
            ax = plt.axes(projection='3d')
            for link in array_stock:
                ax.plot([link.node_a.position[0], link.node_b.position[0]],
                        [link.node_a.position[1], link.node_b.position[1]],
                        [link.node_a.position[2], link.node_b.position[2]])

            ax.set_xlim([-5, 5])
            ax.set_ylim([-5, 5])
            ax.set_zlim([-5, 5])

            plt.show()
            
        time.sleep(0.3)
            '''
    for i in range(len(array_stock)):
        print(' | ', array_stock[i].node_a.name, ' ; ', array_stock[i].node_b.name, ' | ')
    for i in range(len(array_travel)):
        print(' | ', array_travel[i].name, ' ; ')

    plt.figure()
    ax = plt.axes(projection='3d')
    for i in range(len(array_travel)-1):
        ax.plot([array_travel[i].position[0], array_travel[i+1].position[0]],
                [array_travel[i].position[1], array_travel[i+1].position[1]],
                [array_travel[i].position[2], array_travel[i+1].position[2]])
    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])
    ax.set_zlim([-5, 5])

    plt.show()


if __name__ == '__main__':
    launch()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
