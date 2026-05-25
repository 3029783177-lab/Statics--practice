import numpy as np


def brightness_uniformity(luminance_values):
    values = np.array(luminance_values)
    return values.min() / values.max() * 100


def contrast_ratio(white_luminance, black_luminance):
    if black_luminance == 0:
        return float('inf')
    return white_luminance / black_luminance


def rgb_color_error(reference_rgb, measured_rgb):
    ref = np.array(reference_rgb)
    meas = np.array(measured_rgb)
    return np.linalg.norm(ref - meas)


if __name__ == '__main__':
    luminance = [102, 100, 98, 105, 97, 96, 101, 99, 95]

    uniformity = brightness_uniformity(luminance)
    print(f'Brightness Uniformity: {uniformity:.2f}%')

    contrast = contrast_ratio(1200, 0.8)
    print(f'Contrast Ratio: {contrast:.2f}')

    error = rgb_color_error((255, 255, 255), (245, 250, 240))
    print(f'RGB Color Error: {error:.2f}')
