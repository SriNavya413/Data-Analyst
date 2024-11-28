# List of discrete values (e.g., number of cars)
discrete_values = [1, 2, 2, 3, 3, 3, 4, 5, 5]

# Count occurrences using a dictionary
count_dict = {}

# Counting occurrences of each value
for value in discrete_values:
    if value in count_dict:
        count_dict[value] += 1
    else:
        count_dict[value] = 1

# Print the result
print("Count of discrete values:", count_dict)
