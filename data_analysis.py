import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.datasets import load_iris
import warnings
warnings.filterwarnings('ignore')

def load_and_explore_dataset():
    """
    Task 1: Load and Explore the Dataset
    """
    print("=" * 60)
    print("TASK 1: LOADING AND EXPLORING THE DATASET")
    print("=" * 60)
    
    try:
        # Load the Iris dataset
        iris_data = load_iris()
        
        # Create a DataFrame
        df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
        df['species'] = iris_data.target
        df['species_name'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
        
        print("Dataset loaded successfully!")
        print(f"Dataset shape: {df.shape}")
        print("\n1. First few rows of the dataset:")
        print(df.head())
        
        print("\n2. Dataset structure and data types:")
        print(df.info())
        
        print("\n3. Checking for missing values:")
        missing_values = df.isnull().sum()
        print(missing_values)
        
        if missing_values.sum() == 0:
            print("✓ No missing values found in the dataset!")
        else:
            print("⚠ Missing values detected. Cleaning dataset...")
            df = df.dropna()  # or df.fillna() depending on strategy
            
        print(f"\n4. Final dataset shape after cleaning: {df.shape}")
        return df
        
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

def basic_data_analysis(df):
    """
    Task 2: Basic Data Analysis
    """
    print("\n" + "=" * 60)
    print("TASK 2: BASIC DATA ANALYSIS")
    print("=" * 60)
    
    try:
        # Basic statistics for numerical columns
        print("1. Basic statistics for numerical columns:")
        numerical_cols = df.select_dtypes(include=[np.number]).columns
        print(df[numerical_cols].describe())
        
        # Group by species and compute mean
        print("\n2. Mean values grouped by species:")
        species_means = df.groupby('species_name')[numerical_cols].mean()
        print(species_means)
        
        # Additional analysis - correlation matrix
        print("\n3. Correlation matrix between numerical features:")
        correlation_matrix = df[numerical_cols].corr()
        print(correlation_matrix)
        
        # Findings
        print("\n4. Key Findings:")
        print("    Setosa species has the smallest petal dimensions")
        print("    Virginica species has the largest overall dimensions")
        print("    Strong positive correlation between petal length and petal width")
        print("    Sepal length and petal length show moderate correlation")
        
        return species_means, correlation_matrix
        
    except Exception as e:
        print(f"Error in data analysis: {e}")
        return None, None

def create_visualizations(df):
    """
    Task 3: Data Visualization
    """
    print("\n" + "=" * 60)
    print("TASK 3: DATA VISUALIZATION")
    print("=" * 60)
    
    try:
        # Set up the plotting style
        plt.style.use('seaborn-v0_8')
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Iris Dataset Analysis - Four Types of Visualizations', fontsize=16, fontweight='bold')
        
        # 1. Line Chart - Trends across species (using index as pseudo-time)
        ax1 = axes[0, 0]
        for species in df['species_name'].unique():
            species_data = df[df['species_name'] == species]
            ax1.plot(species_data.index, species_data['sepal length (cm)'], 
                    marker='o', label=f'{species.capitalize()}', linewidth=2)
        ax1.set_title('Sepal Length Trends Across Samples', fontweight='bold')
        ax1.set_xlabel('Sample Index')
        ax1.set_ylabel('Sepal Length (cm)')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # 2. Bar Chart - Average petal length per species
        ax2 = axes[0, 1]
        species_avg = df.groupby('species_name')['petal length (cm)'].mean()
        bars = ax2.bar(species_avg.index, species_avg.values, 
                      color=['#FF6B6B', '#4ECDC4', '#45B7D1'], alpha=0.8)
        ax2.set_title('Average Petal Length by Species', fontweight='bold')
        ax2.set_xlabel('Species')
        ax2.set_ylabel('Average Petal Length (cm)')
        ax2.tick_params(axis='x', rotation=45)
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height + 0.05,
                    f'{height:.2f}', ha='center', va='bottom')
        
        # 3. Histogram - Distribution of sepal width
        ax3 = axes[1, 0]
        ax3.hist(df['sepal width (cm)'], bins=20, color='#96CEB4', alpha=0.7, edgecolor='black')
        ax3.set_title('Distribution of Sepal Width', fontweight='bold')
        ax3.set_xlabel('Sepal Width (cm)')
        ax3.set_ylabel('Frequency')
        ax3.grid(True, alpha=0.3)
        
        # Add statistics text
        mean_width = df['sepal width (cm)'].mean()
        std_width = df['sepal width (cm)'].std()
        ax3.axvline(mean_width, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_width:.2f}')
        ax3.legend()
        
        # 4. Scatter Plot - Relationship between sepal length and petal length
        ax4 = axes[1, 1]
        colors = {'setosa': '#FF6B6B', 'versicolor': '#4ECDC4', 'virginica': '#45B7D1'}
        for species in df['species_name'].unique():
            species_data = df[df['species_name'] == species]
            ax4.scatter(species_data['sepal length (cm)'], species_data['petal length (cm)'],
                       c=colors[species], label=species.capitalize(), alpha=0.7, s=60)
        
        ax4.set_title('Sepal Length vs Petal Length', fontweight='bold')
        ax4.set_xlabel('Sepal Length (cm)')
        ax4.set_ylabel('Petal Length (cm)')
        ax4.legend()
        ax4.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('iris_analysis_plots.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        print(" All four visualizations created successfully!")
        print(" Plots saved as 'iris_analysis_plots.png'")
        
    except Exception as e:
        print(f"Error creating visualizations: {e}")

def main():
    """
    Main function to execute the complete data analysis workflow
    """
    print(" IRIS DATASET ANALYSIS PROJECT")
    print(" Analyzing Data with Pandas and Visualizing Results with Matplotlib")
    print("=" * 80)
    
    # Task 1: Load and explore dataset
    df = load_and_explore_dataset()
    
    if df is not None:
        # Task 2: Basic data analysis
        species_means, correlation_matrix = basic_data_analysis(df)
        
        # Task 3: Create visualizations
        create_visualizations(df)
        
        print("\n" + "=" * 80)
        print(" ANALYSIS COMPLETE!")
        print("=" * 80)
        print("Summary of completed tasks:")
        print(" Task 1: Dataset loaded and explored")
        print(" Task 2: Basic statistical analysis performed")
        print(" Task 3: Four types of visualizations created")
        print(" Professional error handling implemented")
        print(" Plots customized with titles, labels, and legends")
        
    else:
        print(" Failed to load dataset. Please check the error messages above.")

if __name__ == "__main__":
    main()
