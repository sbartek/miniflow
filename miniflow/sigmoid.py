import numpy as np

from .node import Node

class Sigmoid(Node):

    def __init__(self, *args):
        super().__init__(args)

    def forward(self):
        self.value = sigmoid(self.inbound_nodes[0].value)

    def backward(self):
        """
        Calculates the gradient using the derivative of
        the sigmoid function.
        """
        # Initialize the gradients to 0.
        self.gradients \
            = {n: np.zeros_like(n.value) for n in self.inbound_nodes}

        # Cycle through the outputs. The gradient will change depending
        # on each output, so the gradients are summed over all outputs.
        for n in self.outbound_nodes:
            # Get the partial of the cost with respect to this node.
            grad_cost = n.gradients[self]
            """
            TODO: Your code goes here!

            Set the gradients property to the gradients with respect to each input.

            NOTE: See the Linear node and MSE node for examples.
            """
            sigmoid = self.value
            self.gradients[self.inbound_nodes[0]]\
                += sigmoid * (1 - sigmoid) * grad_cost
        
def sigmoid(t):
    return 1/(1+np.exp(-t))
