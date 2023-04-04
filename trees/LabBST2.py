from trees.BST import BinarySearchTree

tree = BinarySearchTree()
tree.build_tree(15)  # Add 15 nodes
tree.insert(50)
tree.insert(51)
tree.build_tree(5)  # Add another 5 nodes

print("In order:")
tree.print_in_order()

print(f"Found node: {tree.find(50)}")
tree.delete_max()
tree.delete_min()

print("Deleted min and max:")
tree.print_in_order()
tree.delete_node(51)
tree.delete_node(50)

print(f"Deleted 50 and 51:")
tree.print_in_order()
