import pandas as pd
import numpy as np

def main():
    """
    Main function for data-observer tool.

    This function demonstrates basic data loading and manipulation capabilities.
    """
    # Load sample data
    data = pd.DataFrame({
        'Name': ['John', 'Mary', 'David'],
        'Age': [25, 31, 42],
        'Country': ['USA', 'Canada', 'Mexico']
    })

    # Print raw data
    print("Raw Data:")
    print(data)

    # Perform basic data analysis
    print("\nData Analysis:")
    print("Mean Age:", np.mean(data['Age']))
    print("Data Types:")
    print(data.dtypes)

    # Save data to CSV
    data.to_csv('output.csv', index=False)
    print("\nData saved to output.csv")

if __name__ == "__main__":
    main()