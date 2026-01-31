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

# Estimate calories burned for bench
# Rough approximation: 6 cal/min for heavy lifting
bench_calories = bench_duration * 6

print(f"Estimated calories burned from bench press: {bench_calories:.1f} calories")

print("\nSit-up Tracker")
situps = int(input("How many sit-ups did you do today? "))
calories_situps = (situps / 110) * 100
print(f"You did {situps} sit-ups today.")
print(f"Estimated calories burned from sit-ups: {calories_situps:.1f} calories")

if calories_situps >= 100:
    print("Great job! You hit your 100 calorie goal 💪")
else:
    print("Keep going — you're getting closer to 100 calories!")

print("\nRunning Tracker")
run_distance = float(input("How far did you run today? (miles) "))
run_time = float(input("How long did you run? (minutes) "))

# Input calories eaten
calories_eaten = float(input("How many calories did you eat today? "))

# Constants
CAL_PER_LB = 3500
RUN_CAL_PER_MILE_PER_LB = 0.63

# Calculate running calories
run_calories = run_distance * weight * RUN_CAL_PER_MILE_PER_LB

# Total calories burned (bench + sit-ups + running)
total_burned = bench_calories + calories_situps + run_calories

# Net calories and estimated weight change
calorie_balance = total_burned - calories_eaten
weight_change = calorie_balance / CAL_PER_LB

# Output
print(f"\nCalories burned from bench press: {bench_calories:.1f}")
print(f"Calories burned from sit-ups: {calories_situps:.1f}")
print(f"Calories burned from running: {run_calories:.1f}")
print(f"Total calories burned: {total_burned:.1f}")
print(f"Calories eaten: {calories_eaten:.1f}")
print(f"Net calories (burned - eaten): {calorie_balance:.1f}")

if calorie_balance > 0:
    print(f"Estimated weight loss: {weight_change:.3f} lbs")
elif calorie_balance < 0:
    print(f"Estimated weight gain: {abs(weight_change):.3f} lbs")
else:
    print("Calories balanced — no weight change.")

# Graph
activities = ['Bench Press', 'Sit-ups', 'Running']
calories = [bench_calories, calories_situps, run_calories]

plt.bar(activities, calories, color=['red', 'blue', 'green'])
plt.title('Calories Burned by Activity')
plt.ylabel('Calories')
plt.show()


