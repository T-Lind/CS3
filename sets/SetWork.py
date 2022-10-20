from Set import Set

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print("Built in set example:\n--------------")

print(f"Set a: {set_a}\nSet b: {set_b}")

print(f"Union: {set_a.union(set_b)}")
print(f"Intersection: {set_a.intersection(set_b)}")
print(f"Difference A-B: {set_a.difference(set_b)}")
print(f"Difference B-A: {set_b.difference(set_a)}")
print(f"Symmetric Difference: {set_b.symmetric_difference(set_a)}")

print("\nCustom set example:\n--------------")

set_custom_a = Set(1, 2, 3, 4, 5)
set_custom_b = Set(4, 5, 6, 7, 8)
print(f"Set a: {set_custom_a}\nSet b: {set_custom_b}")

print(f"Union: {set_custom_a.union(set_custom_b)}")
print(f"Intersection: {set_custom_a.intersection(set_custom_b)}")
print(f"Difference A-B: {set_custom_a.difference(set_custom_b)}")
print(f"Difference B-A: {set_custom_b.difference(set_custom_a)}")
print(f"Symmetric Difference: {set_custom_b.symmetric_difference(set_custom_a)}")

