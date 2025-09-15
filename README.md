# Data Analysis Assignment: Iris Dataset Analysis

##  Project Overview

This project demonstrates data analysis and visualization techniques using Python's pandas and matplotlib libraries. The assignment analyzes the famous Iris dataset to showcase data loading, exploration, statistical analysis, and visualization skills.

##  Assignment Objectives

- **Data Loading & Exploration**: Load and inspect a CSV dataset using pandas
- **Statistical Analysis**: Perform basic data analysis and compute statistics
- **Data Visualization**: Create four different types of plots using matplotlib
- **Professional Documentation**: Provide clear code documentation and findings

##  Dataset Information

**Dataset**: Iris Flower Dataset
- **Source**: Scikit-learn's built-in datasets
- **Size**: 150 samples, 4 features
- **Features**: 
  - Sepal Length (cm)
  - Sepal Width (cm)
  - Petal Length (cm)
  - Petal Width (cm)
- **Target**: 3 species (Setosa, Versicolor, Virginica)

##  Requirements

### Python Environment Setup
\`\`\`bash
# Install pipenv if you don't have it
pip install pipenv

# Install project dependencies
pipenv install

# Activate virtual environment
pipenv shell
\`\`\`

### System Requirements
- Python 3.8 or higher
- pipenv (for dependency management)


##  Project Structure

\`\`\`
data-analysis-assignment/
│
├── data_analysis.py          # Main Python script
├── README.md                 # Project documentation
├── iris_analysis_plots.png   # Generated visualization output
├── Pipfile                   # Pipenv dependencies
└── Pipfile.lock             # Locked dependency versions
\`\`\`

##  How to Run

### Setup Environment
\`\`\`bash
# Clone or download the project
# Navigate to project directory
cd data-analysis-assignment

# Install dependencies and create virtual environment
pipenv install

# Activate the virtual environment
pipenv shell
\`\`\`

### Option 1: Python Script
\`\`\`bash
pipenv run python data_analysis.py
\`\`\`

### Option 2: Interactive Execution
\`\`\`python
# Import and run individual functions
from data_analysis import load_and_explore_dataset, basic_data_analysis, create_visualizations

# Load data
df = load_and_explore_dataset()

# Perform analysis
species_means, correlation_matrix = basic_data_analysis(df)

# Create visualizations
create_visualizations(df)
\`\`\`

##  Analysis Tasks Completed

###  Task 1: Load and Explore Dataset
-  Load Iris dataset using scikit-learn
-  Display first few rows with `.head()`
-  Check data types and structure with `.info()`
-  Identify and handle missing values
-  Clean dataset for analysis

###  Task 2: Basic Data Analysis
-  Compute basic statistics using `.describe()`
-  Group data by species and calculate means
-  Generate correlation matrix
-  Identify patterns and insights

###  Task 3: Data Visualization
-  **Line Chart**: Sepal length trends across samples
-  **Bar Chart**: Average petal length comparison by species
-  **Histogram**: Distribution of sepal width measurements
-  **Scatter Plot**: Relationship between sepal and petal length
-  Custom titles, labels, and legends for all plots

##  Key Findings

### Statistical Insights
1. **Species Differentiation**: Setosa species shows distinctly smaller petal dimensions
2. **Size Correlation**: Strong positive correlation (0.87) between petal length and width
3. **Distribution**: Sepal width follows approximately normal distribution
4. **Species Clustering**: Clear separation between species in scatter plot analysis

### Visual Insights
- Setosa species forms a distinct cluster with smaller measurements
- Virginica species generally has the largest overall dimensions
- Linear relationship exists between sepal length and petal length
- Sepal width distribution is relatively uniform across all species

##  Error Handling Features

- **File Loading**: Handles dataset loading errors gracefully
- **Missing Data**: Automatic detection and handling of null values
- **Visualization**: Robust plotting with fallback options
- **Data Types**: Validates data integrity before analysis

##  Output Files

1. **Console Output**: Detailed analysis results and statistics
2. **iris_analysis_plots.png**: High-resolution visualization grid
3. **Statistical Tables**: Formatted data summaries

## Visualization Features

- **Professional Styling**: Uses seaborn styling for enhanced appearance
- **Color Coding**: Consistent color scheme across all plots
- **Interactive Elements**: Grid lines, legends, and annotations
- **High Resolution**: 300 DPI output for presentation quality

##  Learning Outcomes

Upon completion, this project demonstrates:
- Proficiency in pandas for data manipulation
- Matplotlib/seaborn for data visualization
- Statistical analysis and interpretation
- Professional code documentation
- Error handling and robust programming practices

##  Customization Options

### Dataset Alternatives
Replace the Iris dataset with any CSV file:
\`\`\`python
df = pd.read_csv('your_dataset.csv')
\`\`\`

### Visualization Themes
Modify plot styling:
\`\`\`python
plt.style.use('ggplot')  # or 'classic', 'dark_background'
\`\`\`

### Analysis Extensions
Add additional analysis:
- Principal Component Analysis (PCA)
- Classification modeling
- Advanced statistical tests

##  Assignment Submission Checklist

-  Python script (.py) with complete analysis
-  Professional README documentation
-  All four required visualization types
-  Statistical analysis and findings
-  Error handling implementation
-  Customized plots with proper labeling
-  Code comments and documentation
-  Output files and results
-  Pipenv configuration for reproducible environment

##  Development Workflow

### Adding New Dependencies
\`\`\`bash
pipenv install package_name
\`\`\`

### Development Dependencies
\`\`\`bash
pipenv install package_name --dev
\`\`\`

### Environment Management
\`\`\`bash
# Activate environment
pipenv shell

# Run commands in environment
pipenv run python script.py

# Generate requirements.txt (if needed)
pipenv requirements > requirements.txt
\`\`\`




