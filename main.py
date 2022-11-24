# Implementing LinkedList and Node methods
from Node import Node
from LinkedList import LinkedList

# my_list = LinkedList()

# my_list.set_head_node("Logan") # Sets the node we created to be the head node of the list

# my_list.add_node("Bob") # Adds a new node to the end of the list

# my_list.add_node("Joe")

# my_list.add_node("Jeff")

# head_node = my_list.get_head_node()
# print(head_node.get_nodes_value())

# print(my_list.get_node_index("Bob"))

# print(my_list.get_head_node())

# my_list.remove_node("Joe")

# stringed_list = my_list.stringify_list()
# print(stringed_list)

list_to_swap = LinkedList()  # Create a new LinkedList to write a swap algorithm
list_to_swap.set_head_node(1)
list_to_swap.add_node(2)
list_to_swap.add_node(3)
list_to_swap.add_node(4)
list_to_swap.add_node(5)
list_to_swap.add_node(6)

# print(list_to_swap.stringify_list())


def swap_nodes(list, val1, val2):

    if val1 == val2:
        print('No swap is needed - the two values are the same')
        return

    node1 = list.head  # Starts at the head node of the list
    node1_prev = None
    node2 = list.head
    node2_prev = None

    while node1 is not None:
        if node1.get_nodes_value() == val1:
            break
        node1_prev = node1
        node1 = node1.get_next_node()

    while node2 is not None:
        if node2.get_nodes_value() == val2:
            break
        node2_prev = node2
        node2 = node2.get_next_node()

    if node1 is None or node2 is None:
        print('Swap is not possible - One or more elements are not in the list.')
        return

    if node1_prev is None:
        list.head = node2
    else:
        node1_prev.set_next_node(node2)

    if node2_prev is None:
        list.head = node1
    else:
        node2_prev.set_next_node(node1)

    temp = node1.get_next_node()
    node1.set_next_node(node2.get_next_node())
    node2.set_next_node(temp)


def find_2nd_to_last(list):
    current_node = list.head
    last_node = None

    while current_node is not None:
        if current_node.get_next_node() == None:
            last_node = current_node
            break
        current_node = current_node.get_next_node()

    while current_node is not None:
        if current_node.get_next_node() == last_node:
            return current_node
        current_node = current_node.get_next_node()


swap_nodes(list_to_swap, 1, 3)
print(list_to_swap.stringify_list())
print(find_2nd_to_last(list_to_swap))
