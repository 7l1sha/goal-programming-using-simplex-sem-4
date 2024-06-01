from itertools import product

# Function to get coefficients for objective function and constraints
def get_coefficients(num_variables, num_constraints, obj_desc="objective"):
    coefficients = []
    print(f"Enter coefficients for the {obj_desc} function:")
    for i in range(num_variables):
        coeff = float(input(f"Enter coefficient c{i+1} for x{i+1}: "))
        coefficients.append(coeff)
    constraints = []
    bounds = []
    print("Enter coefficients for the constraints:")
    for i in range(num_constraints):
        constraint_coeffs = []
        print(f"For Constraint {i+1}:")
        for j in range(num_variables):
            coeff = float(input(f"Enter coefficient a{i+1}{j+1} for x{j+1}: "))
            constraint_coeffs.append(coeff)
        constraints.append(constraint_coeffs)
        bound = float(input(f"Enter the right-hand side (b{i+1}): "))
        bounds.append(bound)
    return coefficients, constraints, bounds

# Function to find optimal solution
def find_optimal_solution(num_variables, num_constraints, objective_coefficients, constraint_coefficients, constraint_bounds, goal):
    max_profit = 0
    optimal_solution = [0] * num_variables
    deviation_from_goal = float('inf')
    
    for values in product(*[range(int(bound) + 1) for bound in constraint_bounds]):
        profit = sum(c * v for c, v in zip(objective_coefficients, values))
        deviation = abs(profit - goal)

        # Check if constraints are satisfied
        constraints_satisfied = all(sum(a * v for a, v in zip(constraint, values)) <= bound 
                                    for constraint, bound in zip(constraint_coefficients, constraint_bounds))

        # Update the solution if all constraints are satisfied and deviation is smaller
        if constraints_satisfied and deviation < deviation_from_goal:
            max_profit = profit
            optimal_solution = list(values)
            deviation_from_goal = deviation
    
    return optimal_solution, max_profit, deviation_from_goal

# Get user input for the number of products and constraints
num_products = int(input("Enter the number of products: "))
num_constraints = int(input("Enter the number of constraints: "))

# Get coefficients for objective function and constraints
objective_coefficients, constraint_coefficients, constraint_bounds = get_coefficients(num_products, num_constraints)

# Set the arbitrary goal for profit maximization
goal = float(input("Enter the arbitrary goal for profit maximization: "))

# Find the optimal solution
optimal_solution, max_profit, deviation_from_goal = find_optimal_solution(num_products, num_constraints, objective_coefficients, constraint_coefficients, constraint_bounds, goal)

# Print the optimal solution and profit
print("Optimal Solution:")
for i in range(num_products):
    if i < len(optimal_solution):
        print(f"x{i+1} =", optimal_solution[i])
    else:
        print(f"x{i+1} = 0 (Not Used)")
print("Optimal Profit (Z) =", max_profit)
print("Deviation from Goal =", deviation_from_goal)
