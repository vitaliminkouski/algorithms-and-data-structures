class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None
        self.height = 0
        self.num_of_leaves = 1
        self.MSL = 0
        self.a = 0
        self.b = 0
        self.c=0


class BST:
    def __init__(self):
        self.root = None
        self.tree_MSL = 0
        self.answer = None

    # fill height, num_of_leaves, MSL
    def first_step(self, node):
        if node is not None:
            self.first_step(node.left)
            self.first_step(node.right)
            if (node.left == None and node.right == None):
                pass
            elif (node.left == None):
                node.num_of_leaves = node.right.num_of_leaves
                node.height = node.right.height + 1
                node.MSL = node.right.height + 1
            elif (node.right == None):
                node.num_of_leaves = node.left.num_of_leaves
                node.height = node.left.height + 1
                node.MSL = node.left.height + 1
            elif (node.left.height == node.right.height):
                node.num_of_leaves = node.left.num_of_leaves + node.right.num_of_leaves
            elif(node.left.height>node.right.height):
                node.num_of_leaves = node.left.num_of_leaves
            else:
                node.num_of_leaves=node.right.num_of_leaves

            if not ((node.left is None) or (node.right is None)):
                node.height = max(node.left.height, node.right.height) + 1
                node.MSL = node.left.height + node.right.height + 2

            if (node.MSL > self.tree_MSL):
                self.tree_MSL = node.MSL

    # fill b
    def second_step(self, node):
        if node is not None:
            self.second_step(node.left)
            self.second_step(node.right)
            if (node.MSL == self.tree_MSL):
                if (node.left is None):
                    node.b = node.right.num_of_leaves
                elif (node.right is None):
                    node.b = node.left.num_of_leaves
                else:
                    node.b = node.left.num_of_leaves * node.right.num_of_leaves

    # fill a, c
    def third_step(self, node):
        if node is not None:
            if ((node.left is None) and (node.right is None)):
                pass
            elif (node.left is None):
                node.right.a = node.a + node.b
            elif (node.right is None):
                node.left.a = node.a + node.b
            elif (node.left.height > node.right.height):
                node.left.a = node.a + node.b
                node.right.a = node.b
            elif (node.left.height < node.right.height):
                node.right.a = node.a + node.b
                node.left.a = node.b
            else:
                node.left.a = node.b + node.left.num_of_leaves * node.a / node.num_of_leaves
                node.right.a = node.b + node.right.num_of_leaves * node.a / node.num_of_leaves

            node.c=node.a+node.b
            if (node.c % 2 == 1):
                if ((self.answer is None) or ((self.answer is not None) and (node.key > self.answer))):
                    self.answer = node.key
            self.third_step(node.right)
            self.third_step(node.left)



    def run_task_31(self):
        self.first_step(self.root)
        self.second_step(self.root)

        self.root.c=self.root.a+self.root.b
        self.third_step(self.root)
        if(self.answer is not None):
            self.delete_key(self.answer)

    def add(self, key):
        self.root=BST.add_rec(self.root, key)

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
            return BST.find_min_in_subtree(node.left)
        else:
            return node

tree=BST()
number=0
with open("tst.in", "r") as f:
    for line in f:
        tree.add(int(line.strip()))

tree.run_task_31()

traversal_list=tree.pre_order_traversal()

with open("tst.out", "w") as f:
    for key in traversal_list:
        f.write(f"{key}\n")

