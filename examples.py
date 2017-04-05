from miniflow.node import Node

n1 = Node()
n2 = Node([n1])

print("node 1")
print(n1)

print(" node 2")
print(n2)
