from math import lcm


class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right


def get_nodes_tree(file):
    nodes = {}
    for line in file:
        key, node_data = line.strip().split(" = ")
        left, right = node_data.strip("()").split(", ")
        node = Node(left, right)
        nodes[key] = node
    return nodes


def get_steps_for_each_node(instructions, nodes, starting_nodes):
    steps = []
    for node in starting_nodes:
        step = 0
        while not node.endswith("Z"):
            node = nodes[node].left if instructions[step % len(instructions)] == "L" else nodes[node].right
            step += 1
        steps.append(step)
    return steps


def calculate_result(filename):
    with open(filename, "r") as file:
        instructions = file.readline().strip()
        next(file)
        nodes = get_nodes_tree(file)
        starting_nodes = [coordinate for coordinate in nodes.keys() if coordinate[-1] == "A"]
        steps = get_steps_for_each_node(instructions, nodes, starting_nodes)
        return lcm(*steps)


if __name__ == "__main__":
    result = calculate_result("input.txt")
    print(result)
