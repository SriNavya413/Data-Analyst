import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn2_circles
 
def set_operations(set_a, set_b, universal_set):
    # Union of set_a and set_b
    union = set_a.union(set_b)
   
    # Intersection of set_a and set_b
    intersection = set_a.intersection(set_b)
   
    # Complement of set_a with respect to the universal set
    complement_a = universal_set.difference(set_a)
   
    # Complement of set_b with respect to the universal set
    complement_b = universal_set.difference(set_b)
   
    return union, intersection, complement_a, complement_b
 
# Example sets
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
universal_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
 
union, intersection, complement_a, complement_b = set_operations(set_a, set_b, universal_set)
 
print(f"Union of A and B: {union}")
print(f"Intersection of A and B: {intersection}")
print(f"Complement of A: {complement_a}")
print(f"Complement of B: {complement_b}")
 
# Plotting Venn diagram
venn = venn2([set_a, set_b], ('Set A', 'Set B'))
venn2_circles([set_a, set_b])
 
plt.title("Venn Diagram of Set A and Set B")
plt.show()
