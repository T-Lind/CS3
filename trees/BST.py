class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, current_node):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert(data, current_node.left)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert(data, current_node.right)
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
        return self._get_height(self.root)

    def _get_height(self, current_node):
        if current_node is None:
            return -1
        left_height = self._get_height(current_node.left)
        right_height = self._get_height(current_node.right)
        return 1 + max(left_height, right_height)

    def get_num_leaves(self):
        return self._get_num_leaves(self.root)

    def _get_num_leaves(self, current_node):
        if current_node is None:
            return 0
        if current_node.left is None and current_node.right is None:
            return 1
        return self._get_num_leaves(current_node.left) + self._get_num_leaves(current_node.right)

    def print_in_order(self):
        self._print_in_order(self.root)
        print()

    def _print_in_order(self, current_node):
        if current_node:
            self._print_in_order(current_node.left)
            print(current_node.data, end=" ")
            self._print_in_order(current_node.right)

    def print_in_reverse(self):
        self._print_in_reverse(self.root)
        print()

    def _print_in_reverse(self, current_node):
        if current_node:
            self._print_in_reverse(current_node.right)
            print(current_node.data, end=" ")
            self._print_in_reverse(current_node.left)

    def print_pre_order(self):
        self._print_pre_order(self.root)
        print()

    def _print_pre_order(self, current_node):
        if current_node:
            print(current_node.data, end=" ")
            self._print_pre_order(current_node.left)
            self._print_pre_order(current_node.right)

    def print_post_order(self):
        self._print_post_order(self.root)
        print()

    def _print_post_order(self, current_node):
        if current_node:
            self._print_post_order(current_node.left)
            self._print_post_order(current_node.right)
            print(current_node.data, end=" ")

    def _get_num_nodes(self, node):
        if node is None:
            return 0
        return 1 + self._get_num_nodes(node.left) + self._get_num_nodes(node.right)

    def get_num_nodes(self):
        return self._get_num_nodes(self.root)

    def _get_num_levels(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self._get_num_levels(node.left), self._get_num_levels(node.right))

    def get_num_levels(self):
        return self._get_num_levels(self.root)

    def _is_full(self, node):
        if node is None:
            return True
        elif node.left is None and node.right is None:
            return True
        elif node.left is not None and node.right is not None:
            return self._is_full(node.left) and self._is_full(node.right)
        return False

    def is_full(self):
        return self._is_full(self.root)

    def _str(self, node):
        ret_str = ""
        if node:
            ret_str += self._str(node.left) + f"{node.data} " + self._str(node.right)
        return ret_str

    def str(self):
        return self._str(self.root)

    def __str__(self):
        ret_str = ""
        for value in self._str(self.root):
            ret_str += value
        return ret_str
