import pandas as pd
import matplotlib.pyplot as plt


def main():
    df = pd.read_csv('data/sales.csv')

    print('Dataset Preview:')
    print(df.head())

    df['revenue'] = df['units_sold'] * df['unit_price']

    print('\nSummary Statistics:')
    print(df.describe())

    revenue_by_region = df.groupby('region')['revenue'].sum()

    print('\nRevenue by Region:')
    print(revenue_by_region)

    revenue_by_region.plot(kind='bar')
    plt.title('Revenue by Region')
    plt.xlabel('Region')
    plt.ylabel('Revenue')

    plt.tight_layout()
    plt.savefig('outputs/revenue_by_region.png')

    cleaned = df.dropna()
    cleaned.to_csv('outputs/cleaned_sales.csv', index=False)

    print('\nAnalysis complete.')


if __name__ == '__main__':
    main()
