from .node import Node

class Mul(Node):

    def __init__(self, *args):
        super().__init__(args)
        self.value = None
        
    def forward(self):
        self.value = 1
        for n in self.inbound_nodes:
            self.value *= n.value
        
