import numpy as np
import math


class Graphe:
    """Classe définissant un noeud caractérisée par :
    - ses coordonnées
    - son nom
    """

    def __init__(self, array_nodes, array_links):
        self.array_nodes = array_nodes
        self.array_links = array_links
