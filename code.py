import tkinter as tk
from tkinter import messagebox

class GoalProgrammingTkinterGUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Goal Programming Example")
        self.configure(background="#FFCC99")  # Customization

        # Input panel
        input_panel = tk.Frame(self)
        input_panel.grid(row=0, column=0, padx=10, pady=10)

        labels = ["Coefficient c1:", "Coefficient c2:", "a11:", "a12:", "b1:",
                  "a21:", "a22:", "b2:", "Goal 1:"]
        entries = [tk.Entry(input_panel) for _ in range(len(labels))]

        for i, label in enumerate(labels):
            tk.Label(input_panel, text=label, background="#FFCC99").grid(row=i, column=0, sticky=tk.E)
            entries[i].grid(row=i, column=1)

        # Calculate button
        calculate_button = tk.Button(self, text="Calculate", command=self.calculate_optimal_solution,
                                     background="#8E8CD8", font=("Poppins", "bold", 20))
        calculate_button.grid(row=1, column=0, pady=10)

        # Result panel initially hidden
        result_panel = tk.Frame(self)
        result_panel.grid(row=2, column=0, pady=10)

        self.solution_label = tk.Label(result_panel, text="Optimal Solution: ")
        self.solution_label.pack()

        self.profit_label = tk.Label(result_panel, text="Optimal Profit (Z): ")
        self.profit_label.pack()

        self.deviation_label = tk.Label(result_panel, text="Deviation from Goal 1: ")
        self.deviation_label.pack()

    def calculate_optimal_solution(self):
        try:
            coefficients = [float(entry.get()) for entry in self.winfo_children()[0].winfo_children() if isinstance(entry, tk.Entry)]
            b1 = int(coefficients[4])
            b2 = int(coefficients[7])
            goal1 = float(coefficients[-1])

            max_profit = 0
            x1_optimal = 0
            x2_optimal = 0
            deviation_from_goal = float('inf')

            for i in range(b1 + 1):
                for j in range(b2 + 1):
                    profit = coefficients[0] * i + coefficients[1] * j
                    deviation = abs(profit - goal1)

                    if coefficients[2] * i + coefficients[3] * j <= b1 and coefficients[5] * i + coefficients[6] * j <= b2:
                        if deviation < deviation_from_goal:
                            max_profit = profit
                            x1_optimal = i
                            x2_optimal = j
                            deviation_from_goal = deviation

            self.solution_label.config(text=f"Optimal Solution: x1 = {x1_optimal}, x2 = {x2_optimal}")
            self.profit_label.config(text=f"Optimal Profit (Z): {max_profit}")
            self.deviation_label.config(text=f"Deviation from Goal 1: {deviation_from_goal}")

        except ValueError:
            self.solution_label.config(text="Optimal Solution: N/A")
            self.profit_label.config(text="Optimal Profit (Z): N/A")
            self.deviation_label.config(text="Deviation from Goal 1: N/A")
            messagebox.showerror("Input Error", "Invalid input. Please enter valid numeric values.")

if __name__ == "__main__":
    gui = GoalProgrammingTkinterGUI()
    gui.geometry("350x310")
    gui.mainloop()
