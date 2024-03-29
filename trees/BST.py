import random


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __str__(self):
        return f"Data: {self.data}; (Left: {self.left}; Right: {self.right})"


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def from_array(self, array):
        for item in array:
            self.insert(item)

    def build_tree(self, n_items, generate_rand=lambda: random.randint(0, 100)):
        for _ in range(n_items):
            self.insert(generate_rand())

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.__insert(data, self.root)

    def __insert(self, data, current_node):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self.__insert(data, current_node.left)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self.__insert(data, current_node.right)
        else:
            print("Value is already present in the tree.")

    def get_width(self):
        if self.root is None:
            return 0
        queue = [(self.root, 0)]
        cur_level = 0
        cur_count = 0
        max_count = 0
        while queue:
            node, level = queue.pop(0)
            if level == cur_level:
                cur_count += 1
            else:
                max_count = max(cur_count, max_count)
                cur_level = level
                cur_count = 1
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        return max(cur_count, max_count) + 1

    def get_height(self):
        return self.__get_height(self.root)

    def __get_height(self, current_node):
        if current_node is None:
            return -1
        left_height = self.__get_height(current_node.left)
        right_height = self.__get_height(current_node.right)
        return 1 + max(left_height, right_height)

    def get_num_leaves(self):
        return self.__get_num_leaves(self.root)

    def __get_num_leaves(self, current_node):
        if current_node is None:
            return 0
        if current_node.left is None and current_node.right is None:
            return 1
        return self.__get_num_leaves(current_node.left) + self.__get_num_leaves(current_node.right)

    def print_in_order(self):
        self.__print_in_order(self.root)
        print()

    def __print_in_order(self, current_node):
        if current_node:
            self.__print_in_order(current_node.left)
            print(current_node.data, end=" ")
            self.__print_in_order(current_node.right)

    def print_in_reverse(self):
        self.__print_in_reverse(self.root)
        print()

    def __print_in_reverse(self, current_node):
        if current_node:
            self.__print_in_reverse(current_node.right)
            print(current_node.data, end=" ")
            self.__print_in_reverse(current_node.left)

    def print_pre_order(self):
        self.__print_pre_order(self.root)
        print()

    def __print_pre_order(self, current_node):
        if current_node:
            print(current_node.data, end=" ")
            self.__print_pre_order(current_node.left)
            self.__print_pre_order(current_node.right)

    def print_post_order(self):
        self.__print_post_order(self.root)
        print()

    def __print_post_order(self, current_node):
        if current_node:
            self.__print_post_order(current_node.left)
            self.__print_post_order(current_node.right)
            print(current_node.data, end=" ")

    def get_num_nodes(self):
        return self.__get_num_nodes(self.root)

    def __get_num_nodes(self, node):
        if node is None:
            return 0
        return 1 + self.__get_num_nodes(node.left) + self.__get_num_nodes(node.right)

    def get_num_levels(self):
        return self.__get_num_levels(self.root)

    def __get_num_levels(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self.__get_num_levels(node.left), self.__get_num_levels(node.right))

    def is_full(self):
        return self.__is_full(self.root)

    def __is_full(self, node):
        if node is None:
            return True
        elif node.left is None and node.right is None:
            return True
        elif node.left is not None and node.right is not None:
            return self.__is_full(node.left) and self.__is_full(node.right)
        return False

    def find(self, data):
        current_node = self.root
        while current_node is not None:
            if data == current_node.data:
                return current_node
            elif data < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return None

    def delete_min(self):
        if self.root is None:
            return None
        elif self.root.left is None:
            deleted_node = self.root
            self.root = self.root.right
            return deleted_node
        else:
            parent_node = self.root
            current_node = self.root.left
            while current_node.left is not None:
                parent_node = current_node
                current_node = current_node.left
            deleted_node = current_node
            parent_node.left = current_node.right
            return deleted_node

    def delete_max(self):
        if self.root is None:
            return None
        elif self.root.right is None:
            deleted_node = self.root
            self.root = self.root.left
            return deleted_node
        else:
            parent_node = self.root
            current_node = self.root.right
            while current_node.right is not None:
                parent_node = current_node
                current_node = current_node.right
            deleted_node = current_node
            parent_node.right = current_node.left
            return deleted_node

    def delete_node(self, data):
        self.root = self._delete_node(data, self.root)

    def _get_max(self, node):
        if node.right is None:
            return node
        else:
            return self._get_max(node.right)

    def _delete_node(self, data, node):
        if node is None:
            return None
        elif data < node.data:
            node.left = self._delete_node(data, node.left)
        elif data > node.data:
            node.right = self._delete_node(data, node.right)
        else:
            if node.left is None and node.right is None:
                node = None
            elif node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:
                temp = self._get_max(node.left)
                node.data = temp.data
                node.left = self._delete_node(temp.data, node.left)
        return node

    def __str(self, node):
        ret_str = ""
        if node:
            ret_str += self.__str(node.left) + f"{node.data} " + self.__str(node.right)
        return ret_str

    def __str__(self):
        ret_str = ""
        for value in self.__str(self.root):
            ret_str += value
        return ret_str
