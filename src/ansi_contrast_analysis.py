import numpy as np
import matplotlib.pyplot as plt


# Simulated ANSI checkerboard luminance measurements.
# White and black blocks are measured separately.
white_blocks = np.array([
    1180, 1195, 1210, 1178,
    1202, 1188, 1196, 1205
])

black_blocks = np.array([
    0.82, 0.86, 0.80, 0.88,
    0.84, 0.83, 0.87, 0.81
])

average_white = white_blocks.mean()
average_black = black_blocks.mean()
ansi_contrast = average_white / average_black

print(f'Average White Luminance: {average_white:.2f} nits')
print(f'Average Black Luminance: {average_black:.2f} nits')
print(f'ANSI Contrast Ratio: {ansi_contrast:.2f}:1')

labels = ['Average White', 'Average Black']
values = [average_white, average_black]

plt.bar(labels, values)
plt.ylabel('Luminance (nits)')
plt.title('ANSI Contrast Measurement')
plt.tight_layout()
plt.savefig('outputs/ansi_contrast.png')

print('\nSaved ANSI contrast chart.')
