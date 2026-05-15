import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    """
    Main function of the data-observer tool.

    This script provides basic data analysis functionality, including data loading, 
    summary statistics, and data visualization.

    Parameters:
    None

    Returns:
    None
    """
    # Load sample data
    data = pd.DataFrame({
        'A': np.random.rand(100),
        'B': np.random.rand(100)
    })

    # Display summary statistics
    print("Summary Statistics:")
    print(data.describe())

    # Plot histograms
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.hist(data['A'], bins=20)
    plt.title('Histogram of A')
    plt.subplot(1, 2, 2)
    plt.hist(data['B'], bins=20)
    plt.title('Histogram of B')
    plt.tight_layout()
    plt.show()

    # Save data to CSV
    data.to_csv('sample_data.csv', index=False)

if __name__ == "__main__":
    main()