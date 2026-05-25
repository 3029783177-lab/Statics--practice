import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


np.random.seed(0)

# Simulated brightness stability test
minutes = np.arange(0, 120)
brightness = 1000 + np.random.normal(0, 8, len(minutes))

# Simulate thermal drift
brightness -= minutes * 0.15


df = pd.DataFrame({
    'minute': minutes,
    'brightness_nits': brightness,
})

mean_brightness = df['brightness_nits'].mean()
std_brightness = df['brightness_nits'].std()

stability_percent = (1 - std_brightness / mean_brightness) * 100

print(f'Mean Brightness: {mean_brightness:.2f} nits')
print(f'Standard Deviation: {std_brightness:.2f}')
print(f'Stability Score: {stability_percent:.2f}%')

plt.plot(df['minute'], df['brightness_nits'])
plt.xlabel('Time (minutes)')
plt.ylabel('Brightness (nits)')
plt.title('Projector Brightness Stability')
plt.grid(True)
plt.tight_layout()
plt.savefig('outputs/brightness_stability.png')

print('\nSaved brightness stability chart.')
