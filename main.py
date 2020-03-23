from time import sleep
import random
import os

# constants
grid_size = 25
cell_size = 10
step_length = .5 # in seconds
running = True

class Node:
    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state
        self.next_state = 0
    def draw(self):
        if self.state == 1:
            text = " ■ "
        else:
            text = "   "
        print("%s" % text, end='')      

def find_neighboring_nodes(node_list, node_obj):
    num_neighbors_alive = 0
    neighbors = []

    origin_x = node_obj.x
    origin_y = node_obj.y

    dirs = [
    [-1, 1], [0, 1], [1, 1],
    [-1, 0], [1, 0],
    [-1, -1], [0, -1], [1, -1]
    ]

    for dir in dirs:
        dir_x = origin_x + dir[0]
        dir_y = origin_y + dir[1]
        for node in node_list:
            if node.x == dir_x and node.y == dir_y:
                num_neighbors_alive += node.state
                break

    return num_neighbors_alive

def main(nodes):
    # spawn a grid
    for x in range(grid_size):
        for y in range(grid_size):
            node = Node(x, y, random.choice([0, 0, 0, 1]))
            nodes.append(node)

    while running:
        # for each node, find neighbor and set next state
        for node in nodes:
            num = find_neighboring_nodes(nodes, node)
            if node.state == 0 and num == 3:
                node.next_state = 1
            else:
                node.next_state = node.state
            if node.state == 1: 
                if num < 2:
                    node.next_state = 0
                elif num == 2 or num == 3:
                    node.next_state = node.state
                elif num > 3:
                    node.next_state = 0

        sleep(step_length)
        print("\nLoading...\n")
        os.system('clear')

        # set nodes to their next state
        for node in nodes:
            node.state = node.next_state

        # draw grid
        for y in range(grid_size):
            for x in range(grid_size):
                for node in nodes:
                    if node.x == x and node.y == y:
                        node.draw()
            print("\n")

if __name__ == "__main__":
    nodes = []
    main(nodes)
