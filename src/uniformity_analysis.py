import numpy as np
import matplotlib.pyplot as plt


# Simulated 3x3 luminance measurements
luminance_map = np.array([
    [101, 99, 97],
    [103, 100, 96],
    [102, 98, 95]
])

max_luminance = luminance_map.max()
min_luminance = luminance_map.min()

uniformity = min_luminance / max_luminance * 100

print(f'Max Luminance: {max_luminance}')
print(f'Min Luminance: {min_luminance}')
print(f'Brightness Uniformity: {uniformity:.2f}%')

plt.imshow(luminance_map)
plt.colorbar(label='Luminance')
plt.title('3x3 Brightness Uniformity Map')

for i in range(3):
    for j in range(3):
        plt.text(j, i, luminance_map[i, j], ha='center', va='center')

plt.tight_layout()
plt.savefig('outputs/uniformity_map.png')

print('\nSaved uniformity map.')
