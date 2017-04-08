import numpy as np

from .node import Node

class Sigmoid(Node):

    def __init__(self, *args):
        super().__init__(args)

    def forward(self):
        self.value = sigmoid(self.inbound_nodes[0].value)

def sigmoid(t):
    return 1/(1+np.exp(-t))
