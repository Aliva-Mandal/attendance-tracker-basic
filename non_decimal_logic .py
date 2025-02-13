from datetime import datetime, timedelta

def calculate_attendance_hours(current_date, last_date, goal_attendance, current_attendance, total_class_hours_per_week):
    current_date = datetime.strptime(current_date, '%d-%m-%Y')
    last_date = datetime.strptime(last_date, '%d-%m-%Y')
    total_days = (last_date - current_date).days + 1
    total_weeks = total_days / 7
    goal_attendance /= 100
    current_attendance /= 100

 
    goal_total_hours = goal_attendance * total_weeks * total_class_hours_per_week
    current_total_hours = current_attendance * total_weeks * total_class_hours_per_week
    remaining_hours_needed = goal_total_hours - current_total_hours
    remaining_weeks = total_weeks

    if remaining_weeks > 0:
        required_hours_per_week = remaining_hours_needed / remaining_weeks
        if required_hours_per_week > total_class_hours_per_week:
            return "Unable to reach", None, None
        bunk_hours_per_week = total_class_hours_per_week - required_hours_per_week
        maintenance_hours_per_week = goal_attendance * total_class_hours_per_week

        return required_hours_per_week, bunk_hours_per_week, maintenance_hours_per_week
    else:
        return "Unable to reach", None, None

current_date = input("Enter the current date (DD-MM-YYYY): ")
last_date = input("Enter the last date (DD-MM-YYYY): ")
goal_attendance = float(input("Enter the goal attendance percentage: "))
current_attendance = float(input("Enter the current attendance percentage: "))
total_class_hours_per_week = float(input("Enter the total number of class hours per week: "))

required_hours_per_week, bunk_hours_per_week, maintenance_hours_per_week = calculate_attendance_hours(current_date, last_date, goal_attendance, current_attendance, total_class_hours_per_week)

if required_hours_per_week == "Unable to reach":
    print("Unable to reach the goal attendance.")
else:
    print(f"Required hours per week to reach the goal attendance: {required_hours_per_week:.2f}")
    print(f"Hours you can bunk per week and still reach the goal attendance: {bunk_hours_per_week:.2f}")
    print(f"Hours to attend per week to maintain the goal attendance after reaching it: {maintenance_hours_per_week:.2f}")
