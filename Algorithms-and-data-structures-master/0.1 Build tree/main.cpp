#include <fstream>
#include <vector>

class Node {
public:
	int key_;
	Node* right_;
	Node* left_;

	Node(int key): key_(key), left_(nullptr), right_(nullptr) {}

};

class BST {
private:
	Node* root_;

	Node* add_rec(Node* node, int key) {
		if (node == nullptr) {
			return new Node(key);
		}
		if (key < node->key_) {
			node->left_ = add_rec(node->left_, key);
		} else if(key>node->key_){
			node->right_ = add_rec(node->right_, key);
		}
		return node;
	}

	void pre_order_traversal_rec(Node* node, std::vector<int>& traversal_list) {
		if (node != nullptr) {
			traversal_list.push_back(node->key_);
			pre_order_traversal_rec(node->left_, traversal_list);
			pre_order_traversal_rec(node->right_, traversal_list);
		}
	}

	Node* delete_key_rec(Node* node, int key) {
		if (node == nullptr) {
			return nullptr;
		}
		else if (key < node->key_) {
			node->left_ = delete_key_rec(node->left_, key);
			return node;
		}
		else if (key > node->key_) {
			node->right_= delete_key_rec(node->right_, key);
			return node;
		}

		if (node->left_ == nullptr) {
			return node->right_;
		}
		else if (node->right_ == nullptr) {
			return node->left_;
		}
		int min_key_in_right_subtree = find_min_in_subtree(node->right_)->key_;
		node->key_ = min_key_in_right_subtree;
		node->right_ = delete_key_rec(node->right_, min_key_in_right_subtree);
		return node;

	}

	Node* find_min_in_subtree(Node* node) {
		if (node->left_ != nullptr) {
			return find_min_in_subtree(node->left_);
		}
		else {
			return node;
		}
	}

public:
	void add_all(std::vector<int>& list_of_keys) {
		for (int key : list_of_keys) {
			this->root_ = add_rec(this->root_, key);
		}
	}

	std::vector<int> pre_order_traversal() {
		std::vector<int> traversal_list;
		pre_order_traversal_rec(this->root_, traversal_list);
		return traversal_list;
	}

	void delete_key(int key) {
		this->root_ = delete_key_rec(this->root_, key);
	}

	BST():root_(nullptr){}
};

int main() {
	std::ifstream fin("input.txt");
	std::vector<int> list_of_keys;
	int key;
	int key_to_delete;
	fin >> key_to_delete;
	while (fin >> key) {
		list_of_keys.push_back(key);
	}
	fin.close();
	BST tree;
	tree.add_all(list_of_keys);
	tree.delete_key(key_to_delete);
	std::vector<int> traversal_list = tree.pre_order_traversal();
	std::ofstream fout("output.txt");
	for (int key : traversal_list) {
		fout << key << "\n";
	}
	fout.close();
	return 0;
}