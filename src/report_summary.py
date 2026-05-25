import pandas as pd


summary = {
    'Metric': [
        'Brightness Uniformity',
        'Contrast Ratio',
        'Color Error',
        'Brightness Stability'
    ],
    'Value': [
        '92.2%',
        '1500:1',
        '4.3',
        '98.8%'
    ],
    'Status': [
        'PASS',
        'PASS',
        'PASS',
        'PASS'
    ]
}

report = pd.DataFrame(summary)

print(report)

report.to_excel('outputs/projector_evaluation_report.xlsx', index=False)

print('\nSaved projector evaluation report.')
