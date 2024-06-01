import tkinter as tk

def calculate_optimal_solution():
    # Get coefficients of the objective function from the user
    c1 = float(c1_entry.get())
    c2 = float(c2_entry.get())

    # Get coefficients of the constraints from the user
    a11 = float(a11_entry.get())
    a12 = float(a12_entry.get())
    b1 = float(b1_entry.get())

    a21 = float(a21_entry.get())
    a22 = float(a22_entry.get())
    b2 = float(b2_entry.get())

    # Get the goal
    goal = float(goal_entry.get())

    # Initialize variables for the optimal solution
    maxProfit = 0
    x1Optimal = 0
    x2Optimal = 0
    deviationFromGoal=goal

    # Loop to explore the solution space
    for i in range(int(b1) + 1):
        for j in range(int(b2) + 1):
            profit = c1 * i + c2 * j
            deviation = abs(profit - goal)  # Calculate the deviation from Goal 1

                # Check if constraints are satisfied and profit meets the goal
            if (a11 * i + a12 * j <= b1 and
                a21 * i + a22 * j <= b2):
                # Update the solution if profit is maximized
                if deviation < deviationFromGoal:
                            maxProfit = profit
                            x1Optimal = i
                            x2Optimal = j
                            deviationFromGoal = deviation
                            
    # Display the optimal solution and profit in a new window
    result_window = tk.Toplevel(root)
    result_window.title("Optimal Solution")
    result_window.configure(bg="black")
    result_text = tk.StringVar()
    result_text.set(f"Optimal Solution:\n"
                    f"x1 = {x1Optimal}\n"
                    f"x2 = {x2Optimal}\n"
                    f"Optimal Profit (Z) = {maxProfit}")
    result_label = tk.Label(result_window, textvariable=result_text, bg="black", fg="white")
    result_label.pack()

# Create main window
root = tk.Tk()
root.title("Linear Programming Solver")
root.configure(bg="black")

# Change font to Palatino and font color to white
root.option_add("*Font", "Palatino")
root.option_add("*foreground", "white")

# Add main heading
heading_label = tk.Label(root, text="2 Products\n2 Constraints", font=("Times New Roman", 30, "bold"), justify="center", fg="white", bg="black")
heading_label.grid(row=0, column=0, columnspan=6, padx=10, pady=10)


# Add labels and entry widgets for inputs
tk.Label(root, text="Objective Function Coefficients", bg="black", fg="white").grid(row=1, column=0, columnspan=4)

c1_label = tk.Label(root, text="c1:", bg="black", fg="white")
c1_label.grid(row=2, column=0)
c1_entry = tk.Entry(root, fg="black")  # Set foreground color to black
c1_entry.grid(row=2, column=1)

c2_label = tk.Label(root, text="c2:", bg="black", fg="white")
c2_label.grid(row=2, column=2)
c2_entry = tk.Entry(root, fg="black")  # Set foreground color to black
c2_entry.grid(row=2, column=3)

# Add labels and entry widgets for constraint coefficients and RHS
tk.Label(root, text="Constraints", justify="center",bg="black", fg="white").grid(row=3, column=0, columnspan=4)

a11_label = tk.Label(root, text="a11:", bg="black", fg="white")
a11_label.grid(row=4, column=0)
a11_entry = tk.Entry(root, fg="black")  # Set foreground color to black
a11_entry.grid(row=4, column=1)

a12_label = tk.Label(root, text="a12:", bg="black", fg="white")
a12_label.grid(row=4, column=2)
a12_entry = tk.Entry(root, fg="black")  # Set foreground color to black
a12_entry.grid(row=4, column=3)

b1_label = tk.Label(root, text="b1:", bg="black", fg="white")
b1_label.grid(row=4, column=4)
b1_entry = tk.Entry(root, fg="black")  # Set foreground color to black
b1_entry.grid(row=4, column=5)

a21_label = tk.Label(root, text="a21:", bg="black", fg="white")
a21_label.grid(row=5, column=0)
a21_entry = tk.Entry(root, fg="black")  # Set foreground color to black
a21_entry.grid(row=5, column=1)

a22_label = tk.Label(root, text="a22:", bg="black", fg="white")
a22_label.grid(row=5, column=2)
a22_entry = tk.Entry(root, fg="black")  # Set foreground color to black
a22_entry.grid(row=5, column=3)

b2_label = tk.Label(root, text="b2:", bg="black", fg="white")
b2_label.grid(row=5, column=4)
b2_entry = tk.Entry(root, fg="black")  # Set foreground color to black
b2_entry.grid(row=5, column=5)

# Add label and entry widget for the goal
goal_label = tk.Label(root, text="Goal:", bg="black", fg="white")
goal_label.grid(row=6, column=2)
goal_entry = tk.Entry(root, fg="black")  # Set foreground color to black
goal_entry.grid(row=6, column=3)

# Button to trigger the calculation
calculate_button = tk.Button(root, text="Calculate",justify="center", command=calculate_optimal_solution, bg="#563980")
calculate_button.grid(row=8,column=3, pady=10)

# Center the window
root.eval('tk::PlaceWindow . center')

root.mainloop()
