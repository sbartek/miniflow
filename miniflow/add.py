from .node import Node

class Add(Node):
    def __init__(self, *args):
        Node.__init__(self, args)

    def forward(self):
        """
        You'll be writing code here in the next quiz!
        """
        self.value = 0
        for n in self.inbound_nodes:
            self.value += n.value
