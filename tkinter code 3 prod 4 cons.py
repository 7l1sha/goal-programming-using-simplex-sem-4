import tkinter as tk

def calculate_optimal_solution():
    # Get coefficients of the objective function from the user
    c1 = float(c1_entry.get())
    c2 = float(c2_entry.get())
    c3 = float(c3_entry.get())

    # Get coefficients of the constraints from the user
    a11 = float(a11_entry.get())
    a12 = float(a12_entry.get())
    a13 = float(a13_entry.get())
    b1 = float(b1_entry.get())

    a21 = float(a21_entry.get())
    a22 = float(a22_entry.get())
    a23 = float(a23_entry.get())
    b2 = float(b2_entry.get())

    a31 = float(a31_entry.get())
    a32 = float(a32_entry.get())
    a33 = float(a33_entry.get())
    b3 = float(b3_entry.get())
    
    a41 = float(a41_entry.get())
    a42 = float(a42_entry.get())
    a43 = float(a43_entry.get())
    b4 = float(b4_entry.get())

    # Get the goal
    goal = float(goal_entry.get())

    # Initialize variables for the optimal solution
    maxProfit = 0
    x1Optimal = 0
    x2Optimal = 0
    x3Optimal = 0
    x4Optimal = 0
    deviationFromGoal=goal
    
    # Loop to explore the solution space
    for i in range(int(b1) + 1):
        for j in range(int(b2) + 1):
            for k in range(int(b3) + 1):
                for l in range(int(b4) + 1):
                    profit = c1 * i + c2 * j + c3 * k
                    deviation = abs(profit - goal)  # Calculate the deviation from Goal 1

                    # Check if constraints are satisfied
                    if (a11 * i + a12 * j + a13 * k <= b1 and
                        a21 * i + a22 * j + a23 * k <= b2 and
                        a31 * i + a32 * j + a33 * k <= b3 and
                        a41 * i + a42 * j + a43 * k <= b4):
                    # If the deviation qn
                        if deviation < deviationFromGoal:
                            maxProfit = profit
                            x1Optimal = i
                            x2Optimal = j
                            x3Optimal = k
                            x4Optimal = l
                            deviationFromGoal = deviation

    # Display the optimal solution and profit in a new window
    result_window = tk.Toplevel(root)
    result_window.title("Optimal Solution")
    result_window.configure(bg="black")
    result_text = tk.StringVar()
    result_text.set(f"Optimal Solution:\n"
                    f"x1 = {x1Optimal}\n"
                    f"x2 = {x2Optimal}\n"
                    f"x3 = {x3Optimal}\n"
                    f"x4 = {x4Optimal}\n"
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
heading_label = tk.Label(root, text="3 Products\n4 Constraints", font=("Times New Roman", 30, "bold"), justify="center", fg="white", bg="black")
heading_label.grid(row=0, column=0, columnspan=10, padx=10, pady=10)

# Add labels and entry widgets for inputs
tk.Label(root, text="Objective Function Coefficients", bg="black", fg="white").grid(row=1, column=0, columnspan=8)

c1_label = tk.Label(root, text="c1:", bg="black", fg="white")
c1_label.grid(row=2, column=0)
c1_entry = tk.Entry(root, fg="black")  # Set foreground color to black
c1_entry.grid(row=2, column=1)

c2_label = tk.Label(root, text="c2:", bg="black", fg="white")
c2_label.grid(row=2, column=2)
c2_entry = tk.Entry(root, fg="black")  # Set foreground color to black
c2_entry.grid(row=2, column=3)

c3_label = tk.Label(root, text="c3:", bg="black", fg="white")
c3_label.grid(row=2, column=4)
c3_entry = tk.Entry(root, fg="black")  # Set foreground color to black
c3_entry.grid(row=2, column=5)

# Add labels and entry widgets for constraint coefficients and RHS
tk.Label(root, text="Constraints", bg="black", fg="white").grid(row=3, column=0, columnspan=8)

a11_label = tk.Label(root, text="a11:", bg="black", fg="white")
a11_label.grid(row=4, column=0)
a11_entry = tk.Entry(root, fg="black")  # Set foreground color to black
a11_entry.grid(row=4, column=1)

a12_label = tk.Label(root, text="a12:", bg="black", fg="white")
a12_label.grid(row=4, column=2)
a12_entry = tk.Entry(root, fg="black")  # Set foreground color to black
a12_entry.grid(row=4, column=3)

a13_label = tk.Label(root, text="a13:", bg="black", fg="white")
a13_label.grid(row=4, column=4)
a13_entry = tk.Entry(root, fg="black")  # Set foreground color to black
a13_entry.grid(row=4, column=5)

b1_label = tk.Label(root, text="b1:", bg="black", fg="white")
b1_label.grid(row=4, column=8)
b1_entry = tk.Entry(root, fg="black")  # Set foreground color to black
b1_entry.grid(row=4, column=9)

a21_label = tk.Label(root, text="a21:", bg="black", fg="white")
a21_label.grid(row=5, column=0)
a21_entry = tk.Entry(root, fg="black")  # Set foreground color to black
a21_entry.grid(row=5, column=1)

a22_label = tk.Label(root, text="a22:", bg="black", fg="white")
a22_label.grid(row=5, column=2)
a22_entry = tk.Entry(root, fg="black")  # Set foreground color to black
a22_entry.grid(row=5, column=3)

a23_label = tk.Label(root, text="a23:", bg="black", fg="white")
a23_label.grid(row=5, column=4)
a23_entry = tk.Entry(root, fg="black")  # Set foreground color to black
a23_entry.grid(row=5, column=5)

b2_label = tk.Label(root, text="b2:", bg="black", fg="white")
b2_label.grid(row=5, column=8)
b2_entry = tk.Entry(root, fg="black")  # Set foreground color to black
b2_entry.grid(row=5, column=9)

a31_label = tk.Label(root, text="a31:", bg="black", fg="white")
a31_label.grid(row=6, column=0)
a31_entry = tk.Entry(root, fg="black")  # Set foreground color to black
a31_entry.grid(row=6, column=1)

a32_label = tk.Label(root, text="a32:", bg="black", fg="white")
a32_label.grid(row=6, column=2)
a32_entry = tk.Entry(root, fg="black")  # Set foreground color to black
a32_entry.grid(row=6, column=3)

a33_label = tk.Label(root, text="a33:", bg="black", fg="white")
a33_label.grid(row=6, column=4)
a33_entry = tk.Entry(root, fg="black")  # Set foreground color to black
a33_entry.grid(row=6, column=5)

b3_label = tk.Label(root, text="b3:", bg="black", fg="white")
b3_label.grid(row=6, column=8)
b3_entry = tk.Entry(root, fg="black")  # Set foreground color to black
b3_entry.grid(row=6, column=9)

a41_label = tk.Label(root, text="a41:", bg="black", fg="white")
a41_label.grid(row=7, column=0)
a41_entry = tk.Entry(root, fg="black")  # Set foreground color to black
a41_entry.grid(row=7, column=1)

a42_label = tk.Label(root, text="a42:", bg="black", fg="white")
a42_label.grid(row=7, column=2)
a42_entry = tk.Entry(root, fg="black")  # Set foreground color to black
a42_entry.grid(row=7, column=3)

a43_label = tk.Label(root, text="a43:", bg="black", fg="white")
a43_label.grid(row=7, column=4)
a43_entry = tk.Entry(root, fg="black")  # Set foreground color to black
a43_entry.grid(row=7, column=5)

b4_label = tk.Label(root, text="b4:", bg="black", fg="white")
b4_label.grid(row=7, column=8)
b4_entry = tk.Entry(root, fg="black")  # Set foreground color to black
b4_entry.grid(row=7, column=9)

# Add label and entry widget for the goal
goal_label = tk.Label(root, text="Goal:", bg="black", fg="white")
goal_label.grid(row=8, column=4)
goal_entry = tk.Entry(root, fg="black")  # Set foreground color to black
goal_entry.grid(row=8, column=5)

# Button to trigger the calculation
calculate_button = tk.Button(root, text="Calculate", command=calculate_optimal_solution, bg="#563980")
calculate_button.grid(row=9, column=5, pady=10)

# Center the window
root.eval('tk::PlaceWindow . center')

root.mainloop()
