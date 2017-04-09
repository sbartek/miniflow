def forward_pass(graph):
    """
    Performs a forward pass through a list of sorted Nodes.

    Arguments:

        `graph`: The result of calling `topological_sort`.
    """
    # Forward pass
    for n in graph:
        n.forward()


# def forward_pass(output_node, sorted_nodes):
#     """
#     Performs a forward pass through a list of sorted nodes.

#     Arguments:

#         `output_node`: A node in the graph, should be the output node (have no outgoing edges).
#         `sorted_nodes`: A topologically sorted list of nodes.

#     Returns the output Node's value
#     """

#     for n in sorted_nodes:
#         n.forward()

#     return output_node.value
