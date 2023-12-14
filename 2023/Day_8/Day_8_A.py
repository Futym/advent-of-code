class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right


def calculate_result(filename):
    with open(filename, "r") as file:
        instructions = file.readline().strip()
        next(file)
        nodes = {}
        for line in file:
            key, node_data = line.strip().split(" = ")
            left, right = node_data.strip("()").split(", ")
            node = Node(left, right)
            nodes[key] = node
        current_node = "AAA"
        step = 0
        while current_node != "ZZZ":
            current_node = nodes[current_node].left if instructions[step % len(instructions)] == "L" \
                else nodes[current_node].right
            step += 1
        return step


if __name__ == "__main__":
    result = calculate_result("input.txt")
    print(result)
