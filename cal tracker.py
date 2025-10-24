print("Welcome to the Daily Calorie Tracker")

meal_names = []
meal_calories = []

num_meals = int(input("How many meals do you want to enter today? "))

for i in range(num_meals):
    meal = input(f"Enter the name of meal {i+1}: ")
    calories = float(input(f"Enter calories for {meal}: "))
    meal_names.append(meal)
    meal_calories.append(calories)

print("\nMeals Entered:")
for i in range(num_meals):
    print(meal_names[i], ":", meal_calories[i], "calories")

total_calories = sum(meal_calories)
average_calories = total_calories / num_meals

print("\nTotal Calorie Intake:", total_calories)
print("Average Calories per Meal:", average_calories)

daily_limit = float(input("\nEnter your daily calorie limit: "))

if total_calories > daily_limit:
    print("Warning: You have exceeded your daily calorie limit.")
else:
    print("Good job! You are within your daily calorie limit.")