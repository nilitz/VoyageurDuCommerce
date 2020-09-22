import numpy as np
import math


class Link:
    """Classe définissant un noeud caractérisée par :
    - son poids
    - le premier noeud
    - le deuxième noeud
    """

    def __init__(self, node_a, node_b):
        self.vector = np.array([node_b.position[0] - node_a.position[0], node_b.position[1] - node_a.position[1], node_b.position[2] - node_a.position[2]])
        self.weight = np.sqrt((node_b.position[0] - node_a.position[0])**2 + (node_b.position[1] - node_a.position[1])**2 + (node_b.position[2] - node_a.position[2])**2)
        self.node_a = node_a
        self.node_b = node_b

