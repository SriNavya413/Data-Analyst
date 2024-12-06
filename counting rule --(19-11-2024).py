from collections import Counter

# List of roles (or elements)
roles = ['admin', 'user', 'admin', 'guest', 'user', 'user', 'admin']

# Count occurrences of each role using Counter
role_counts = Counter(roles)

# Print the result
print("Role counts:", role_counts)
