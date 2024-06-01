import tkinter as tk
from tkinter import simpledialog

def get_coefficient(prompt):
    return float(simpledialog.askstring("Input", prompt))

def get_right_hand_side(prompt):
    return float(simpledialog.askstring("Input", prompt))

root = tk.Tk()
root.withdraw()  # Hide the main window

# Get coefficients of the objective function from the user
c1 = get_coefficient("Enter coefficient c1 for the objective function Z = c1*x1 + c2*x2 + c3*x3: ")
c2 = get_coefficient("Enter coefficient c2 for the objective function Z = c1*x1 + c2*x2 + c3*x3: ")
c3 = get_coefficient("Enter coefficient c3 for the objective function Z = c1*x1 + c2*x2 + c3*x3: ")

# Get coefficients of the constraints from the user
a11 = get_coefficient("Enter coefficient a11 for Constraint 1: ")
a12 = get_coefficient("Enter coefficient a12 for Constraint 1: ")
a13 = get_coefficient("Enter coefficient a13 for Constraint 1: ")
b1 = get_right_hand_side("Enter the right-hand side (b1) for Constraint 1: ")

a21 = get_coefficient("Enter coefficient a21 for Constraint 2: ")
a22 = get_coefficient("Enter coefficient a22 for Constraint 2: ")
a23 = get_coefficient("Enter coefficient a23 for Constraint 2: ")
b2 = get_right_hand_side("Enter the right-hand side (b2) for Constraint 2: ")

a31 = get_coefficient("Enter coefficient a31 for Constraint 3: ")
a32 = get_coefficient("Enter coefficient a32 for Constraint 3: ")
a33 = get_coefficient("Enter coefficient a33 for Constraint 3: ")
b3 = get_right_hand_side("Enter the right-hand side (b3) for Constraint 3: ")

a41 = get_coefficient("Enter coefficient a41 for Constraint 4: ")
a42 = get_coefficient("Enter coefficient a42 for Constraint 4: ")
a43 = get_coefficient("Enter coefficient a43 for Constraint 4: ")
b4 = get_right_hand_side("Enter the right-hand side (b4) for Constraint 4: ")

# Initialize variables for the optimal solution
maxProfit = 0
x1Optimal = 0
x2Optimal = 0
x3Optimal = 0
deviationFromGoal = float('inf')

# Set the arbitrary goal for profit maximization
goal1 = get_coefficient("Enter the arbitrary goal for profit maximization (Goal 1): ")

# Loop to explore the solution space
for i in range(int(b1) + 1):
    for j in range(int(b2) + 1):
        for k in range(int(b3) + 1):
            for l in range(int(b4) + 1):
                profit = c1 * i + c2 * j + c3 * k
                deviation = abs(profit - goal1)  # Calculate the deviation from Goal 1

                # Check if constraints are satisfied
                if (a11 * i + a12 * j + a13 * k <= b1 and
                    a21 * i + a22 * j + a23 * k <= b2 and
                    a31 * i + a32 * j + a33 * k <= b3 and
                    a41 * i + a42 * j + a43 * k <= b4):
                    # If the deviation from Goal 1 is smaller, update the solution
                    if deviation < deviationFromGoal:
                        maxProfit = profit
                        x1Optimal = i
                        x2Optimal = j
                        x3Optimal = k
                        deviationFromGoal = deviation

# Create a new window to display results
result_window = tk.Tk()
result_window.title("Optimal Solution")

# Display the optimal solution and profit
tk.Label(result_window, text="Optimal Solution:").pack()
tk.Label(result_window, text=f"x1 = {x1Optimal}").pack()
tk.Label(result_window, text=f"x2 = {x2Optimal}").pack()
tk.Label(result_window, text=f"x3 = {x3Optimal}").pack()
tk.Label(result_window, text=f"Optimal Profit (Z) = {maxProfit}").pack()
tk.Label(result_window, text=f"Deviation from Goal 1 = {deviationFromGoal}").pack()

result_window.mainloop()
