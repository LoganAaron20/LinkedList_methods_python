# Implementation of the Node class

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def get_next_node(self):
        return self.next # Returns the Node the the current Node is pointing to

    def get_nodes_value(self):
        return self.value # Returns the current Node's value

    def set_next_node(self, node_to_set):
        self.next = node_to_set # Sets the current Node to point to the node passed as an argument

    def change_node_value(self, new_value):
        self.value = new_value # Sets the current Node's value to the value passed in as an argument

