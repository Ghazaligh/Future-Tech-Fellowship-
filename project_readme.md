# An Exploratory Data Analysis & Predictive Approach to Revenue Optimization and Tax Compliance in Zamfara State

## 1. Project Overview
This project investigates internal revenue collection patterns, taxpayer compliance behaviors, and structural performance metrics across Local Government Areas (LGAs) and key economic sectors in Zamfara State. By leveraging data science techniques, the framework transforms static administrative logs into predictive intelligence to assist state revenue authorities in identifying compliance bottlenecks, preventing revenue leakage, and planning proactive outreach.

## 2. Project Objectives
* To clean, aggregate, and analyze multi-year revenue collection records across all Local Government Areas in Zamfara State.
* To investigate the correlation between business age, tax assessment amounts, and historical payment delays.
* To build and evaluate machine learning classification models (Logistic Regression and Random Forest) capable of predicting taxpayer non-compliance risk.
* To provide actionable, data-driven recommendations for modernizing state internal revenue generation and audit allocation.

## 3. Research Questions
* Which Local Government Areas and economic sectors record the highest rates of tax non-compliance or delayed payments?
* How strongly do the assessed tax amount and historical delay count influence the probability of a business defaulting?
* Can machine learning models reliably predict non-compliant taxpayers in advance to optimize resource allocation for state auditors?

## 4. Dataset Description & Source
* **Dataset Scope:** 2,000 structured tax assessment and collection records.
* **Key Features:**
  * `Transaction_ID`: Unique identifier for each tax transaction log.
  * `LGA`: Local Government Area in Zamfara State (Gusau, Talata Mafara, Kaura Namoda, Bakura, Bukkuyum, Gummi, Zurmi).
  * `Economic_Sector`: Business categorization (Agriculture & Agro-Allied, Retail & Commerce, Transportation, Hospitality & Services, Small-Scale Manufacturing).
  * `Assessed_Amount_NGN`: Total financial tax assessment levied in Nigerian Naira.
  * `Historical_Delay_Count`: Number of recorded late payments by the taxpayer in prior cycles.
  * `Business_Age_Years`: Operating duration of the business entity.
  * `Non_Compliant`: Target binary classification label (0 = Compliant / On-Time, 1 = Non-Compliant / Delayed).
* **Data Sourcing & Simulation Methodology:** Designed using rigorous statistical parameter modeling mirroring regional economic profiles and tax tiers across Zamfara State to establish a robust and reproducible machine learning pipeline.

## 5. Tools & Technologies
* **Programming Language:** Python (v3.10+)
* **Data Manipulation & Ingestion:** Pandas, NumPy
* **Exploratory Data Analysis & Visualization:** Matplotlib, Seaborn
* **Machine Learning & Modeling:** Scikit-Learn (Logistic Regression, Random Forest, ColumnTransformer, Pipeline, StandardScaler, OneHotEncoder)
* **Environment & Version Control:** Jupyter Notebooks, Git / GitHub Repository

## 6. Methodology
1. **Data Ingestion & Preprocessing:** Handling missing values via median/constant imputation, parsing categorical features through One-Hot Encoding, and normalizing numerical scales with StandardScaler.
2. **Exploratory Data Analysis (EDA):** Generating comparative distributions, correlation heatmaps, and boxplots to visualize tax disparities across sectors and LGAs.
3. **Model Training & Evaluation:** Splitting data into training (80%) and testing (20%) sets, training classification algorithms, and evaluating performance using Precision, Recall, F1-Score, and ROC-AUC metrics.
