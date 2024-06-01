import tkinter as tk

def on_button_click(problem_type):
    print(f"Selected problem type: {problem_type}")

def customize_equation():
    print("Customizing equation...")

root = tk.Tk()
root.title("Goal Programming Using Simplex")

# Configure background to black
root.configure(bg="black")

# Main Heading
heading_label = tk.Label(root, text="Goal Programming\nUsing Simplex Method", font=("Times New Roman", 20, "bold"), justify="center", fg="white", bg="black")
heading_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Sub Heading
sub_heading_label = tk.Label(root, text="Choose your standard problem type", font=("Palatino", 14), fg="white", bg="black")
sub_heading_label.grid(row=1, column=0, columnspan=2)

# Buttons for standard problem types
button1 = tk.Button(root, text="2 products\n2 constraints", width=15, height=3, font=("Palatino", 12), command=lambda: on_button_click("Type 1"), bg="#563980", fg="white")
button1.grid(row=2, column=0, padx=10, pady=10)

button2 = tk.Button(root, text="2 products\n3 constraints", width=15, height=3, font=("Palatino", 12), command=lambda: on_button_click("Type 2"), bg="#563980", fg="white")
button2.grid(row=2, column=1, padx=10, pady=10)

button3 = tk.Button(root, text="3 products\n3 constraints", width=15, height=3, font=("Palatino", 12), command=lambda: on_button_click("Type 3"), bg="#563980", fg="white")
button3.grid(row=3, column=0, padx=10, pady=10)

button4 = tk.Button(root, text="3 products\n4 constraints", width=15, height=3, font=("Palatino", 12), command=lambda: on_button_click("Type 4"), bg="#563980", fg="white")
button4.grid(row=3, column=1, padx=10, pady=10)

# Center the window
root.eval('tk::PlaceWindow . center')

root.mainloop()
