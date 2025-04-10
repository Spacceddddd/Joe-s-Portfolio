import pandas as pd
import matplotlib.pyplot as plt

# Define the Fibonacci generator function
def fibonacci_sequence(n):
    fib = [0, 1]  # Starting values
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

# Generate Fibonacci numbers
n = 20 # Number of Fibonacci numbers to generate
fib_numbers = fibonacci_sequence(n)

# Create a Pandas DataFrame
df = pd.DataFrame({
    'Index': range(1, n + 1),
    'Fibonacci': fib_numbers
})

# Plot the Fibonacci sequence
plt.figure(figsize=(10, 6))
plt.plot(df['Index'], df['Fibonacci'], marker='o', label='Fibonacci Growth')
plt.title('Growth of Fibonacci Sequence', fontsize=16)
plt.xlabel('Index', fontsize=14)
plt.ylabel('Fibonacci Number', fontsize=14)
plt.grid(visible=True, which='both', linestyle='--', linewidth=0.5)
plt.legend(fontsize=12)
plt.show()
