class Node:

    def __init__(self, inbound_nodes=[]):
        
        # Node(s) from which this Node receives values
        self.inbound_nodes = inbound_nodes
        # Node(s) to which this Node passes values
        self.outbound_nodes = []
        # For each inbound Node here, add this Node as an outbound Node to _that_ Node.
        for n in self.inbound_nodes:
            n.outbound_nodes.append(self)

    def __str__(self):
        out = f'inound nodes: {len(self.inbound_nodes)} '
        for in_node in self.inbound_nodes:
            out  += str(in_node)
        return out + '*'
