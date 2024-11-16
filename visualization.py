"""
visualization.py

This module visualizes normalized data for two columns in the Apple App Store dataset.
It includes:
- Histograms for distribution analysis.
- Box plots for outlier detection.
- Line plots for trends over data indices.
- Scatter plots for relationship visualization.

Functions:
- plot_histogram(df): Create histograms for normalized columns.
- plot_boxplot(df): Create box plots for normalized columns.
- plot_lineplot(df): Create line plots to show value trends.
- plot_scatterplot(df): Create scatter plots for relationships.
"""

import pandas as pd
import matplotlib.pyplot as plt

def normalize_data(df, columns):
    """
    Normalize the selected columns using Max-Abs Scaling.

    Args:
        df (pd.DataFrame): Original dataset.
        columns (list): List of columns to normalize.

    Returns:
        pd.DataFrame: DataFrame with normalized columns.
    """
    df_normalized = df[columns].copy()
    for column in columns:
        df_normalized[column] = df_normalized[column] / df_normalized[column].abs().max()
    return df_normalized

def plot_histogram(df):
    """
    Plot histograms for normalized columns.

    Args:
        df (pd.DataFrame): DataFrame containing normalized data.
    """
    df.hist(bins=20, figsize=(10, 5), edgecolor='black', color='skyblue')  # Single color
    plt.suptitle('Histograms of Normalized Data', fontsize=16)
    plt.show()

def plot_boxplot(df):
    """
    Plot box plots for normalized columns.

    Args:
        df (pd.DataFrame): DataFrame containing normalized data.
    """
    df.plot(kind='box', figsize=(8, 6), patch_artist=True, color=dict(boxes="skyblue", whiskers="black"))
    plt.title('Box Plot of Normalized Data', fontsize=16)
    plt.ylabel('Normalized Values', fontsize=12)
    plt.show()

def plot_lineplot(df):
    """
    Plot line plots for normalized columns.

    Args:
        df (pd.DataFrame): DataFrame containing normalized data.
    """
    df.plot(kind='line', figsize=(10, 6), marker='o', linestyle='-', alpha=0.7)
    plt.title('Line Plot of Normalized Data', fontsize=16)
    plt.ylabel('Normalized Values', fontsize=12)
    plt.xlabel('Data Index', fontsize=12)
    plt.legend(title="Columns", fontsize=10)
    plt.show()

def plot_scatterplot(df):
    """
    Plot scatter plots for relationships between two normalized columns.

    Args:
        df (pd.DataFrame): DataFrame containing normalized data.
    """
    plt.figure(figsize=(8, 6))
    plt.scatter(df['rating_count_tot'], df['rating_count_ver'], alpha=0.7, color='blue', edgecolors='black')
    plt.title('Scatter Plot: Rating Count Tot vs Rating Count Ver', fontsize=16)
    plt.xlabel('Rating Count Tot (Normalized)', fontsize=12)
    plt.ylabel('Rating Count Ver (Normalized)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

if __name__ == "__main__":
    # Load the dataset
    df = pd.read_csv("AppleStore.csv")

    # Columns to normalize
    columns_to_normalize = ["rating_count_tot", "rating_count_ver"]

    # Normalize the data
    df_normalized = normalize_data(df, columns_to_normalize)

    # Visualize normalized data
    print("Plotting histograms...")
    plot_histogram(df_normalized)

    print("Plotting box plots...")
    plot_boxplot(df_normalized)

    print("Plotting line plots...")
    plot_lineplot(df_normalized)

    print("Plotting scatter plots...")
    plot_scatterplot(df_normalized)
