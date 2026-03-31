import matplotlib.pyplot as plt
import numpy as np

print("Enter X values separated by spaces (or Enter for [1,2,3,4,5]):")
x_input = input().strip()

if x_input:
    x_data = [float(val) for val in x_input.split()]
else:
    x_data = [1, 2, 3, 4, 5]

print("Enter Y values separated by spaces (or Enter for sample data):")
y_input = input().strip()

if y_input:
    y_data = [float(val) for val in y_input.split()]
else:
    y_data = [2, 4, 6, 8, 10]

print(f"Plotting {len(x_data)} points: X={x_data}, Y={y_data}")

plt.figure(figsize=(10, 6))
plt.plot(x_data, y_data,
         marker='o',
         linestyle='--',
         linewidth=2,
         markersize=8,
         color='blue')

plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title(f"Line Graph: {len(x_data)} Data Points")
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("Line graph displayed!")