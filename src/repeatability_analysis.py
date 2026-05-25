import numpy as np
import matplotlib.pyplot as plt


np.random.seed(1)

measurements = np.random.normal(1000, 6, 30)

mean_value = np.mean(measurements)
std_value = np.std(measurements)

repeatability = (1 - std_value / mean_value) * 100

print(f'Mean Brightness: {mean_value:.2f}')
print(f'Standard Deviation: {std_value:.2f}')
print(f'Repeatability: {repeatability:.2f}%')

plt.plot(measurements, marker='o')
plt.xlabel('Measurement Index')
plt.ylabel('Brightness (nits)')
plt.title('Brightness Repeatability Test')
plt.grid(True)
plt.tight_layout()
plt.savefig('outputs/repeatability_plot.png')

print('\nSaved repeatability plot.')
