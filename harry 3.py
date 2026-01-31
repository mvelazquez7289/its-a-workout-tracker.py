import matplotlib.pyplot as plt

print("Hello Mark")

# Basic info
age = int(input("What is your age? "))
weight = float(input("What is your weight? "))

if weight > 230:
    print("Ok, let's plan.")
else:
    print("Ok, implement new plan.")

print("\nBench Press Tracker")
bench_weight = float(input("Weight used in bench press (lbs)? "))
bench_reps = int(input("Reps per set? "))
bench_sets = int(input("Number of sets? "))
bench_duration = float(input("Total bench duration (minutes)? "))

# Estimate calories burned for bench press (6 cal/min for heavy lifting)
bench_calories = bench_duration * 6
bench_weight_change = bench_calories / 3500  # weight change in lbs

print(f"Estimated calories burned from bench press: {bench_calories:.1f} calories")

print("\nSit-up Tracker")
situps = int(input("How many sit-ups did you do today? "))
calories_situps = (situps / 110) * 100
situp_weight_change = calories_situps / 3500
print(f"You did {situps} sit-ups today.")
print(f"Estimated calories burned from sit-ups: {calories_situps:.1f} calories")

if calories_situps >= 100:
    print("Great job! You hit your 100 calorie goal 💪")
else:
    print("Keep going — you're getting closer to 100 calories!")

print("\nRunning Tracker")
run_distance = float(input("How far did you run today? (miles) "))
run_time = float(input("How long did you run? (minutes) "))
run_calories = run_distance * weight * 0.63  # running calories estimate
run_weight_change = run_calories / 3500

# Input calories eaten
calories_eaten = float(input("How many calories did you eat today? "))

# Total burned and net calories
total_burned = bench_calories + calories_situps + run_calories
calorie_balance = total_burned - calories_eaten
total_weight_change = calorie_balance / 3500

# Output
print(f"\nCalories burned from bench press: {bench_calories:.1f}")
print(f"Calories burned from sit-ups: {calories_situps:.1f}")
print(f"Calories burned from running: {run_calories:.1f}")
print(f"Total calories burned: {total_burned:.1f}")
print(f"Calories eaten: {calories_eaten:.1f}")
print(f"Net calories (burned - eaten): {calorie_balance:.1f}")

if total_weight_change > 0:
    print(f"Estimated weight loss: {total_weight_change:.3f} lbs")
elif total_weight_change < 0:
    print(f"Estimated weight gain: {abs(total_weight_change):.3f} lbs")
else:
    print("Calories balanced — no weight change.")

# Graph: Calories burned
activities = ['Bench Press', 'Sit-ups', 'Running']
calories = [bench_calories, calories_situps, run_calories]
weight_changes = [bench_weight_change, situp_weight_change, run_weight_change]

plt.figure(figsize=(10,5))

# Bar chart for calories burned
plt.bar(activities, calories, color=['red', 'blue', 'green'], alpha=0.7, label='Calories Burned')

# Overlay line chart for weight change (lbs)
plt.plot(activities, weight_changes, color='black', marker='o', linestyle='-', linewidth=2, label='Weight Change (lbs)')

plt.title('Calories Burned and Weight Change by Activity')
plt.ylabel('Calories / Weight (lbs)')
plt.legend()
plt.show()
