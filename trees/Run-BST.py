from trees.BST import BinarySearchTree

tree = BinarySearchTree()
tree.insert(90)
tree.insert(80)
tree.insert(70)
tree.insert(85)
tree.insert(100)
tree.insert(98)
tree.insert(120)

print("In order:")
tree.print_in_order()

print("Pre order:")
tree.print_pre_order()

print("Post order:")
tree.print_post_order()

print("Reverse order:")
tree.print_in_reverse()

print(f"Height: {tree.get_height()}")
print(f"Width: {tree.get_width()}")
print(f"# of leaves: {tree.get_num_leaves()}")
print(f"# of nodes: {tree.get_num_nodes()}")
print(f"# of levels: {tree.get_num_levels()}")
print(f"Tree as string: {tree}")
print(f"Tree is full: {tree.is_full()}")