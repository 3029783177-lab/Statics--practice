import pandas as pd
import numpy as np


np.random.seed(42)

samples = 100

brightness = np.random.normal(1000, 35, samples)
contrast = np.random.normal(1400, 80, samples)
uniformity = np.random.normal(92, 2, samples)
color_error = np.random.normal(4.5, 0.6, samples)


df = pd.DataFrame({
    'brightness_nits': brightness,
    'contrast_ratio': contrast,
    'uniformity_percent': uniformity,
    'color_error': color_error,
})

print(df.head())

print('\nSaving simulated projector measurement data...')

df.to_csv('outputs/projector_measurements.csv', index=False)

print('Done.')
