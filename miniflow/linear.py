import numpy as np

from .node import Node

class Linear(Node):

    def __init__(self, inputs, weights, bias):
        super().__init__([inputs, weights, bias])

    def forward(self):
        self.value = \
          self.inbound_nodes[0].value\
            .dot(self.inbound_nodes[1].value)\
            + self.inbound_nodes[2].value
