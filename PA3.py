#PA3
import numpy as np 

# Define the polynomial function f(x) = 2x^3 + 3x^2 + 1
poly_func = np.poly1d([2, 3, 0, 1])

# Print the polynomial function
print("Polynomial function f(x) = 2x^3 + 3x^2 + 1:")
print(poly_func)
print()

# Evaluate the function at x = 2
x_val = 2
result = poly_func(x_val)
print(f"f({x_val}) =", result)

# Define the polynomial function f(x) = x^2 + 1
poly_func_2 = np.poly1d([1, 0, 1])

# Find and print the derivative
derivative = np.polyder(poly_func_2)
print("\nDerivative of f(x) = x^2 + 1:")
print(derivative)
print()

# Evaluate the derivative at x = 1
x_val_2 = 1
result_2 = np.polyval(derivative, x_val_2)
print(f"f'({x_val_2}) =", result_2)
#%%
import numpy as np

def polynomial_val(coefficients, x):
    return np.polyval(coefficients, x)

def polynomial_deriv(coefficients):
    return np.polyder(coefficients)

def newtons_method(coefficients, x_guess, x_prev=None):
    x_next = x_guess - polynomial_val(coefficients, x_guess) / polynomial_val(polynomial_deriv(coefficients), x_guess)
    print("x_n:", x_next)
    
    #If x_prev is not provided, set it to the current guess for comparison
    if x_prev is None:
        x_prev = x_guess

    # Check if the difference between approximations is small
    if abs(x_next - x_prev) < 1e-6:  # prevent conversion
        return x_next
    else:
        return newtons_method(coefficients, x_next, x_prev=x_next)

def main():
    # Prompt user for a polynomial
    polynomial_str = input("Enter the coefficients of the polynomial separated by spaces (e.g., '2 3 1' for 2x^2 + 3x + 1): ")
    coefficients = [float(coef) for coef in polynomial_str.split()]

    # Prompt user for an initial guess x_1
    x_guess = float(input("Enter an initial guess (x_1): "))

    # Apply Newton's method (recursion)
    print("Iterative values of x_n:")
    root = newtons_method(coefficients, x_guess)

    # Print the root
    print("Final root:", round(root, 3))

    # Compute and print roots using numpy
    roots = np.roots(coefficients)
    print("Roots using numpy:", roots)

main()

