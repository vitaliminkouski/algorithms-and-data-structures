

def is_binary_tree_search(input_data, nodes_amount):
    list_of_intervals = []
    list_of_intervals.append((-float('Inf'), float('Inf')))
    for i in range(1, nodes_amount):
        value, parent_index, side = int(input_data[i][0]), int(input_data[i][1]), input_data[i][2]
        if side == "L":
            min_value = list_of_intervals[parent_index-1][0]
            max_value = int(input_data[parent_index-1][0])
        elif side == "R":
            min_value = int(input_data[parent_index-1][0])
            max_value = list_of_intervals[parent_index-1][1]
        list_of_intervals.append((min_value, max_value))
        if (value < min_value or value >= max_value):
            return "NO"

    return "YES"


input_data = []
with open("bst.in", "r") as f:
    nodes_amount = int(f.readline())
    input_data.append([f.readline().strip(), 0, ""])
    for i in range(nodes_amount - 1):
        input_data.append(f.readline().split())

with open("bst.out", "w") as f:
    f.write(is_binary_tree_search(input_data, nodes_amount))
