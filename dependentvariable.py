# Define the independent variable (hours studied)
hours_studied = [1, 2, 3, 4, 5, 6]

# Define the dependent variable (marks scored) based on hours studied
# Assuming marks = 10 * hours_studied
marks_scored = [10 * hour for hour in hours_studied]

# Display the relationship
for hour, marks in zip(hours_studied, marks_scored):
    print(f"Hours studied: {hour}, Marks scored: {marks}")
