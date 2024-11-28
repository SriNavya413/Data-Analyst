import numpy as np
import pandas as pd

def create_sample_data(size=1000):
    # Create sample data for weather (Sunny/Rainy) and activity (Walk/Stay_Home)
    weather = np.random.choice(['Sunny', 'Rainy'], size=size, p=[0.7, 0.3])
    
    # People are more likely to walk when sunny (80%) than when rainy (20%)
    activity = []
    for condition in weather:
        if condition == 'Sunny':
            activity.append(np.random.choice(['Walk', 'Stay_Home'], p=[0.8, 0.2]))
        else:
            activity.append(np.random.choice(['Walk', 'Stay_Home'], p=[0.2, 0.8]))
    
    return pd.DataFrame({'Weather': weather, 'Activity': activity})

def calculate_conditional_probability(data, event, given_condition):
    """
    Calculate P(event|condition) = P(event and condition) / P(condition)
    """
    # Total number of observations
    total = len(data)
    
    # Count occurrences of the condition
    condition_count = len(data[data['Weather'] == given_condition])
    
    # Count occurrences of both event and condition
    event_and_condition = len(data[(data['Weather'] == given_condition) & 
                                 (data['Activity'] == event)])
    
    # Calculate conditional probability
    conditional_prob = event_and_condition / condition_count
    
    return conditional_prob

# Create sample data
data = create_sample_data()

# Calculate some conditional probabilities
p_walk_given_sunny = calculate_conditional_probability(data, 'Walk', 'Sunny')
p_walk_given_rainy = calculate_conditional_probability(data, 'Walk', 'Rainy')

# Print results
print(f"Probability of walking given it's sunny: {p_walk_given_sunny:.2f}")
print(f"Probability of walking given it's rainy: {p_walk_given_rainy:.2f}")

# Display overall data distribution
print("\nOverall Data Distribution:")
print(pd.crosstab(data['Weather'], data['Activity'], normalize='index'))