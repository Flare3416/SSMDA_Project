# Stock Market Statistical Modeling and Data Analytics

## Project Information

**Institution:** Maharaja Agrasen Institute of Technology  
**Subject:** Statistics, Statistical Modelling and Data Analytics (DA-304T)  
**Semester:** 6  
**Year of Study:** 2025-26  
**Classes:** MLDA II (ABC)

### Team Members
| Name | Enrollment Number |
|------|-------------------|
| Ujjwal Kumar | 02114803123 |
| Harshit Tiwar | 02614803123 |

---

## Project Overview

This project applies statistical modeling, linear algebra, and exploratory data analysis techniques to perform comprehensive analysis on historical stock price data. The objective is to understand market behavior, reduce dimensionality through eigenvector analysis, and build predictive models for future price actions.

---

## Problem Statement

You have been provided with a historical daily stock dataset for a major publicly traded company in CSV format. The objective is to:

1. Perform **Exploratory Data Analysis** to understand stock behavior and volatility
2. Apply **Linear Algebra** to reduce dimensionality of highly correlated price features
3. Build **Statistical Models** to predict future price actions
4. Identify distinct "market factors" through linear independence analysis for diversified portfolio building

---

## Dataset Overview

**Source:** [Kaggle Stock Market Dataset](https://www.kaggle.com/datasets/jacksoncrow/stock-market-dataset)

### Data Fields
- **Date:** Trading date
- **Open:** Opening price
- **High:** Maximum price during the day
- **Low:** Minimum price during the day
- **Close:** Closing price (adjusted for splits)
- **Adj Close:** Adjusted close price (adjusted for dividends and splits)
- **Volume:** Number of shares traded during the day

---

## Project Phases and Deliverables

### Phase 1: Exploratory Data Analysis & Hypothesis Testing (Unit I)

**Objective:** Understand historical behavior and volatility of the stock

**Tasks:**
- ✅ **Data Preparation**
  - Create `Daily_Return` column: percentage change in Adj Close from previous day
  - Create `Target_Next_Day_Close` column: Adj Close shifted backward by one row

- ✅ **Descriptive Statistics**
  - Calculate mean, variance, and standard deviation of Volume and Daily_Return
  
- ✅ **Visualization**
  - Generate time-series plot of Adj Close over Date

- ✅ **Hypothesis Testing**
  - **Hypothesis:** Is trading volume significantly different on days when stock goes up vs. down?
  - **Null Hypothesis (H₀):** Trading volume is the same regardless of price movement
  - **Alternative Hypothesis (H₁):** Trading volume differs based on price movement
  - Perform appropriate statistical test (t-test, Mann-Whitney U, etc.)

---

### Phase 2: Feature Optimization via Eigenvectors (Unit IV)

**Objective:** Reduce dimensionality using linear algebra concepts

**Tasks:**
- ✅ **Covariance Matrix**
  - Construct covariance matrix using Open, High, Low, and Volume columns
  
- ✅ **Eigenvalues and Eigenvectors**
  - Calculate eigenvalues and eigenvectors of the covariance matrix
  - Analyze variance explained by each component
  
- ✅ **Basis and Dimension Analysis**
  - Identify principal component (eigenvector with largest eigenvalue)
  - Explain how independent basis vectors reduce dataset dimensionality
  - Document application to regression models

---

### Phase 3: Statistical Modelling & Diagnostics (Unit II)

**Objective:** Build and validate predictive models

**Tasks:**
- ✅ **Multiple Linear Regression**
  - Predict `Target_Next_Day_Close` using Open, High, Low, and Volume
  - Compute regression coefficients using least squares geometry
  - Report R², adjusted R², and model statistics
  
- ✅ **Logistic Regression**
  - Create binary target: Next day price up (1) or down (0)
  - Implement logistic regression model
  - Report accuracy, precision, recall, F1-score
  
- ✅ **Regression Diagnostics**
  - Plot residuals and analyze distribution (Q-Q plot, histogram)
  - Calculate influence diagnostics (Cook's distance, leverage)
  - Identify extreme outliers (e.g., market crash days)
  - Assess multicollinearity (VIF values)

---

## Project Structure

```
SSMDA_Project/
├── app.py                          # Main application entry point
├── analysis.py                     # Data analysis and modeling code
├── kaggleimport.py                # Data import utilities (archived)
├── requirements.txt                # Python dependencies
├── .gitignore                      # Git ignore rules
├── README.md                       # This file
└── data/
    ├── symbols_valid_meta.csv      # Stock metadata
    ├── etfs/                       # ETF data files
    └── stocks/                     # Stock data files
```

---

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip package manager

### Step 1: Clone Repository
```bash
git clone <repository-url>
cd SSMDA_Project
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Download Dataset
1. Visit [Kaggle Stock Market Dataset](https://www.kaggle.com/datasets/jacksoncrow/stock-market-dataset)
2. Download the dataset
3. Extract and place CSV files in the `data/` directory

---

## Usage

### Run Analysis
```bash
python app.py
```

### Import Analysis Module
```python
from analysis import *
# Use analysis functions for EDA, modeling, etc.
```

---

## Dependencies

| Package | Purpose |
|---------|---------|
| pandas | Data manipulation and analysis |
| numpy | Numerical computations |
| scipy | Statistical calculations |
| matplotlib | Data visualization |
| seaborn | Advanced visualization |
| scikit-learn | Machine learning models |
| statsmodels | Statistical modeling |

See `requirements.txt` for full list and versions.

---

## Key Findings & Results

### Phase 1: EDA & Hypothesis Testing
- **Mean Daily Return:** [To be populated]
- **Volume Statistics:** Mean = [X], Std Dev = [Y]
- **Hypothesis Test Result:** [Test statistic, p-value, conclusion]

### Phase 2: Eigenvalue Analysis
- **Principal Component:** [Highest eigenvalue]
- **Variance Explained:** [Percentage by top components]
- **Effective Dimensionality:** [Reduced dimensions]

### Phase 3: Model Performance
- **Linear Regression:** R² = [X], RMSE = [Y]
- **Logistic Regression:** Accuracy = [X]%, F1-Score = [Y]

---

## Methodology

### Statistical Techniques Used
1. **Descriptive Statistics:** Mean, variance, standard deviation
2. **Hypothesis Testing:** T-tests, Mann-Whitney U test
3. **Linear Algebra:** Eigenvalue decomposition, Principal Component Analysis
4. **Regression Analysis:** OLS regression, logistic regression
5. **Diagnostics:** Residual analysis, influence diagnostics

### Assumptions & Limitations
- Assumes historical patterns may indicate future trends (not guaranteed)
- Linear models may not capture non-linear market dynamics
- External factors (news, events) not captured in price data
- Data is historical and subject to survivorship bias

---

## References

1. Walpole, R. E., Myers, R. H., & Myers, S. L. (2012). *Probability and Statistics for Engineers and Scientists*
2. Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning*
3. [Kaggle Stock Market Dataset Documentation](https://www.kaggle.com/datasets/jacksoncrow/stock-market-dataset)

---

## Submission Guidelines

- **Format:** Jupyter Notebook + Python scripts
- **Documentation:** Inline comments and docstrings
- **Results:** Summary report with visualizations
- **Code Quality:** PEP 8 compliant, well-structured

---

## Contact

For questions or collaboration:
- **Ujjwal Kumar** (02114803123)
- **Harshit Tiwar** (02614803123)

---

**Last Updated:** March 31, 2026  
**Subject Code:** DA-304T | **Institution:** MAIT
