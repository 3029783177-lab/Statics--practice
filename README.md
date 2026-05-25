# Automated Projector Performance Evaluation

A Python practice project for automated projector performance testing and data analysis.

This repository focuses on measurement workflows commonly used in optical engineering, display testing, and projection system evaluation.

## Evaluation Targets

- Brightness measurement
- Brightness uniformity
- Contrast ratio
- Color accuracy
- Grayscale response
- Image sharpness
- Geometric distortion
- Repeatability analysis
- Automatic report generation

## Project Structure

```text
.
├── data/
│   └── sample_measurements.csv
├── outputs/
│   └── .gitkeep
├── src/
│   ├── analysis.py
│   ├── projector_metrics.py
│   └── simulate_projector_data.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Typical Workflow

1. Capture test patterns with a camera or sensor
2. Extract measurement regions
3. Calculate luminance and color metrics
4. Analyze uniformity, contrast, and repeatability
5. Visualize results
6. Export CSV results and charts
7. Generate an evaluation report

## Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Generate simulated projector measurement data:

```bash
python src/simulate_projector_data.py
```

Run analysis:

```bash
python src/analysis.py
```

Generated charts and analysis results will be saved in the `outputs/` folder.

## Metrics

### Brightness Uniformity

```text
uniformity = minimum_luminance / maximum_luminance * 100%
```

### Contrast Ratio

```text
contrast_ratio = white_luminance / black_luminance
```

### Color Error

This project uses simplified RGB distance as a beginner-friendly example. Later it can be extended to CIE XYZ, CIE Lab, and Delta E.

## Tech Stack

- Python
- pandas
- numpy
- matplotlib

## Roadmap

- Add camera image processing examples
- Add nine-point luminance uniformity evaluation
- Add CIE color space conversion
- Add geometric distortion analysis
- Add automatic PDF or HTML report generation
