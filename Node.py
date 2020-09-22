import numpy as np
import math


class Node:
    """Classe définissant un noeud caractérisée par :
    - ses coordonnées
    - son nom
    """

    def __init__(self, name, x, y, z):
        self.name = name
        self.position = np.array([x, y, z])
