goal_weight = input("Enter your goal body weight (kg):")
goal_weight_lb = float(goal_weight) * 2.20462
low_protein = int(goal_weight_lb)
high_protein = int(goal_weight_lb * 1.2)

print("Protein needs to be between " + str(low_protein) + " and " + str(high_protein) + " grams.")