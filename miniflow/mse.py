from .node import Node

class MSE(Node):

    def __init__(self, y, a):
        super().__init__([y, a])

    def forward(self):
        y = self.inbound_nodes[0].value
        a = self.inbound_nodes[1].value
        self.value = sum((y-a)**2)/len(y)

        # NOTE: We reshape these to avoid possible matrix/vector broadcast
        # errors.
        #
        # For example, if we subtract an array of shape (3,) from an array of shape
        # (3,1) we get an array of shape(3,3) as the result when we want
        # an array of shape (3,1) instead.
        #
        # Making both arrays (3,1) insures the result is (3,1) and does
        # an elementwise subtraction as expected.
        #y = self.inbound_nodes[0].value.reshape(-1, 1)
        #a = self.inbound_nodes[1].value.reshape(-1, 1)
        
