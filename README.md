# Exploratory Data Analysis (EDA) on Titanic Dataset

## Project Overview
This project performs **Exploratory Data Analysis (EDA)** on the Titanic dataset using Python. The objective is to understand the dataset through descriptive statistics and visualizations, identify patterns and relationships, detect missing values and outliers, and make meaningful inferences from the data.

## Objective
- Understand the dataset using statistical analysis.
- Visualize the distribution of features.
- Explore relationships between variables.
- Identify patterns, trends, and anomalies.
- Draw basic insights from the data.

## Tools and Technologies
- Python 3
- Pandas
- Matplotlib
- Seaborn
- Plotly (Optional)
- VS Code / Jupyter Notebook

## Dataset
**Dataset:** Titanic Dataset

Place the dataset file (`Titanic-Dataset.csv`) in the project folder before running the program.

## Project Structure

```
EDA_Titanic/
│── eda_titanic.py
│── Titanic-Dataset.csv
│── README.md
```

## Features
- Load and inspect the dataset
- Display dataset information
- Generate summary statistics
- Check missing values
- Handle missing values
- Plot histogram for Age
- Plot boxplot for Fare
- Plot survival count
- Generate pairplot
- Create correlation heatmap
- Visualize survival by gender
- Visualize survival by passenger class
- Display basic data insights

## Installation

Install the required libraries using:

```bash
pip install pandas matplotlib seaborn plotly
```

## How to Run

1. Download the Titanic dataset.
2. Place `Titanic-Dataset.csv` in the project folder.
3. Open the project in VS Code or any Python IDE.
4. Run the program:

```bash
python eda_titanic.py
```

or

```bash
python3 eda_titanic.py
```

## Visualizations Generated

The project creates the following visualizations:

- Histogram of Age Distribution
- Boxplot of Fare
- Survival Count Plot
- Pair Plot of Numerical Features
- Correlation Heatmap
- Survival by Gender
- Survival by Passenger Class

## Data Cleaning Performed

- Filled missing values in the **Age** column using the median.
- Filled missing values in the **Embarked** column using the mode.
- Removed the **Cabin** column because it contains many missing values.

## Key Observations

- Female passengers had a higher survival rate than male passengers.
- First-class passengers survived more frequently than second- and third-class passengers.
- Most passengers were between 20 and 40 years of age.
- The Fare feature contains several outliers.
- Passenger class has a noticeable relationship with survival.

## Learning Outcomes

After completing this project, you will understand:

- Exploratory Data Analysis (EDA)
- Data visualization techniques
- Descriptive statistics
- Correlation analysis
- Missing value handling
- Outlier detection
- Pattern recognition in datasets

## Libraries Used

- pandas
- matplotlib
- seaborn
- plotly

## Future Enhancements

- Interactive visualizations using Plotly
- Feature engineering
- Outlier treatment
- Machine Learning prediction model
- Dashboard creation

## Author

Rakshita

## License

This project is developed for educational and learning purposes only.
