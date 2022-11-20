 # Implementing LinkedList and Node methods
from Node import Node
from LinkedList import LinkedList

my_list = LinkedList()

my_list.set_head_node("Logan") # Sets the node we created to be the head node of the list

my_list.add_node("Bob") # Adds a new node to the end of the list

my_list.add_node("Joe")

my_list.add_node("Jeff")

head_node = my_list.get_head_node()
print(head_node.get_nodes_value())

print(my_list.get_node_index("Bob"))

print(my_list.get_head_node())

my_list.remove_node("Joe")

stringed_list = my_list.stringify_list()
print(stringed_list)
