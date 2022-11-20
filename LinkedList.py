# Implementation of a LinkedList class
from Node import Node

class LinkedList:

    def __init__(self):
        self.head = None # Starts as an empty list

    def get_head_node(self):
        return self.head

    def set_head_node(self, node_data):
        if self.get_head_node() == None: 
            new_node = Node(node_data)
            self.head = new_node # Sets the head of the LinkedList to the node passed as an argument
        else:
            raise ValueError("There is already a head node, please use the set_new_head() method")

    def get_previous_node(self, node):
        starting_node = self.get_head_node()
        prev_node = None
        
        if starting_node == node:
            raise ValueError("The Node you are trying to find is the head of the list (There is no previous Node)")

            while starting_node is not None:
                if starting_node == node:
                    return prev_node
                    break # If we found the node we are looking for, break out of the loop
                prev_node = starting_node
                starting_node = starting_node.get_next_node()

    def add_node(self, node_to_add):
        starting_node = self.get_head_node()

        if starting_node is None:
            raise ValueError("The list you are trying to add to is empty, please add a new head Node to start a list")

        while starting_node is not None:
            if starting_node.get_next_node() == None: # We reached the end of the list
                new_node = Node(node_to_add)
                starting_node.set_next_node(new_node)
                return f'Added {new_node.get_nodes_value()} to the list'
            starting_node = starting_node.get_next_node()

    def set_new_head(self, node_to_set):
        head_node = self.get_head_node()

        if head_node is not None:
            new_node = Node(node_to_set)
            new_node.set_next_node(head_node) # Set the new Node to point at the previous head Node
        elif head_node is None:
            self.set_head_node(Node(node_to_set)) # Sets the head Node to the node to set as head if there is not head Node

    def remove_node(self, node_to_remove): # Removes the Node from the list that contains the value of the argument passed in
        if self.get_head_node() is not None:
            starting_node = self.get_head_node() # Retrieves the Head Node
            prev_node = None

            while starting_node is not None: # Starts at the head Node
                if starting_node.get_nodes_value() == node_to_remove:
                    starting_node_next = starting_node.get_next_node() # Getting the next Node to set Previous Node to point to next
                    prev_node.set_next_node(starting_node_next)
                    return f'Successfully removed {starting_node.get_nodes_value()}'
                prev_node = starting_node
                starting_node = starting_node.get_next_node()
        else:
            return -1 

    def get_node_index(self, node_to_find):
        count = 0
        
        starting_node = self.get_head_node() # Start at the beginning of the list

        while starting_node is not None:
            if starting_node.get_nodes_value() == node_to_find:
                count += 1
                return count
            count += 1
            starting_node = starting_node.get_next_node()

    def stringify_list(self):
        string_list = ""

        starting_node = self.get_head_node()

        while starting_node is not None:
            if starting_node.get_next_node() == None:
                string_list += starting_node.get_nodes_value()
                starting_node = starting_node.get_next_node()
            else:
                string_list += starting_node.get_nodes_value() + ", "
                starting_node = starting_node.get_next_node()

        return string_list
