class Node:

    def __init__(self, inbound_nodes=[]):
        
        # Node(s) from which this Node receives values
        self.inbound_nodes = inbound_nodes
        # Node(s) to which this Node passes values
        self.outbound_nodes = []
        # For each inbound Node here,
        # add this Node as an outbound Node to _that_ Node.
        for n in self.inbound_nodes:
            n.outbound_nodes.append(self)
        # value will be calculated during forward pass
        self.value = None
        self.gradients = {}
        
    def forward(self):
        """
        Forward propagation.

        Compute the output value based on `inbound_nodes` and
        store the result in self.value.
        """
        raise NotImplemented

    def backward(self):
        """
        Every node that uses this class as a base class will
        need to define its own `backward` method.
        """
        raise NotImplementedError
    
    def __str__(self):
        out = f'inound nodes: {len(self.inbound_nodes)} '
        for in_node in self.inbound_nodes:
            out  += str(in_node)
        return out + '*'
