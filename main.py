goal_weight = input("Enter your goal body weight (kg):")
activity_level_int = int(input("Enter your activity level (Hours):"))

goal_weight_lb = float(goal_weight) * 2.20462
low_protein = int(goal_weight_lb)
high_protein = int(goal_weight_lb * 1.2)
low_carbs = 0
high_carbs = 0

if activity_level_int <= 3:
    low_carbs = goal_weight_lb * 0.7
    high_carbs = goal_weight_lb * 0.9
elif activity_level_int <= 6:
    low_carbs = goal_weight_lb * 0.8
    high_carbs = goal_weight_lb * 1.1
elif activity_level_int <= 12:
    low_carbs = goal_weight_lb
    high_carbs = goal_weight_lb * 1.5
else:
    low_carbs = goal_weight_lb * 1.2
    high_carbs = goal_weight_lb * 1.7

print("Protein needs to be between " + str(low_protein) + " and " + str(high_protein) + " grams.")
print("Carbs needs to be between " + str(int(low_carbs)) + " and " + str(int(high_carbs)) + " grams.")