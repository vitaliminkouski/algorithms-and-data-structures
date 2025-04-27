class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None


class BST:
    def __init__(self):
        self.root = None

    def add_all(self, list_of_keys):
        for key in list_of_keys:
            self.root = BST.add_rec(self.root, key)

    def delete_key(self, key):
        self.root = BST.delete_key_rec(self.root, key)

    @staticmethod
    def add_rec(node, key):
        if not node:
            return Node(key)
        if key < node.key:
            node.left = BST.add_rec(node.left, key)
        elif key > node.key:
            node.right = BST.add_rec(node.right, key)
        return node

    def pre_order_traversal(self):
        traversal_list = []
        BST.pre_order_traversal_rec(self.root, traversal_list)
        return traversal_list

    @staticmethod
    def pre_order_traversal_rec(node, traversal_list):
        if node is not None:
            traversal_list.append(node.key)
            BST.pre_order_traversal_rec(node.left, traversal_list)
            BST.pre_order_traversal_rec(node.right, traversal_list)

    @staticmethod
    def delete_key_rec(node, key):
        if (node is None):
            return None
        elif (key > node.key):
            node.right = BST.delete_key_rec(node.right, key)
            return node
        elif (key < node.key):
            node.left = BST.delete_key_rec(node.left, key)
            return node

        if (node.left is None):
            return node.right
        elif (node.right is None):
            return node.left
        else:
            min_key_in_right_subtree = BST.find_min_in_subtree(node.right).key
            node.key = min_key_in_right_subtree
            node.right = BST.delete_key_rec(node.right, min_key_in_right_subtree)
            return node

    @staticmethod
    def find_min_in_subtree(node):
        if (node.left is not None):
            return BST.find_max_in_subtree(node.left)
        else:
            return node


with open('input.txt', 'r') as f:
    key_to_delete=int(f.readline())
    f.readline()
    list_of_keys = [int(line.strip()) for line in f]

tree = BST()
tree.add_all(list_of_keys)
tree.delete_key(key_to_delete)
traversal_list = tree.pre_order_traversal()

with open("output.txt", "w") as f:
    f.writelines(f"{key}\n" for key in traversal_list)
