# Python-project
# Mental Health in Tech Survey Analytics – Exploratory Data Analysis

## Project Overview
This project performs Exploratory Data Analysis (EDA) on the Mental Health in Tech Survey dataset from Kaggle using Python, Pandas, NumPy, Matplotlib, and Seaborn.
The main objective is to analyze respondent profiles, treatment-seeking, work interference, and employer support through data cleaning and visualization, handling the data responsibly as it relates to a sensitive topic.

## Dataset
**Source:** [Mental Health in Tech Survey – Kaggle (OSMI)](https://www.kaggle.com/datasets/osmi/mental-health-in-tech-survey)

The dataset contains about 1,250 responses to a 2014 survey on mental health in the tech workplace, with around 27 attributes:

* `Age`, `Gender`, `Country`, `state`: Respondent profile.
* `self_employed`, `tech_company`: Employment details.
* `family_history`: Family history of mental illness.
* `treatment`: Whether treatment was sought.
* `work_interfere`: How often mental health affects work.
* `no_employees`, `remote_work`: Company size and remote work status.
* `benefits`, `care_options`, `wellness_program`, `seek_help`, `anonymity`, `leave`: Employer support.
* Perceived consequences of discussing health, willingness to discuss in an interview, and free-text comments.

## Objectives

1. Clean the data (unrealistic ages, inconsistent gender spellings, missing values in `self_employed` and `work_interfere`).
2. Drop low-value columns (timestamp, state, free-text comments).
3. Analyze the respondent profile by age, gender, and country.
4. Find the share of respondents who sought treatment.
5. Study the link between family history and treatment-seeking.
6. Analyze how often mental health interferes with work.
7. Compare employer support (benefits, care options, wellness programs).
8. Study differences by company size, remote work, and tech vs non-tech companies.
9. Create seven visualizations.

## Graphs Included

1. Respondent Age Distribution: Histogram.
2. Gender Distribution: Bar / Pie chart.
3. Top Countries by Respondents: Bar chart.
4. Treatment Sought: Count plot / Pie chart.
5. Family History vs Treatment: Grouped bar chart.
6. Mental Health Interference with Work: Bar chart.
7. Employer Support (Benefits, Care Options, Wellness Programs): Grouped bar chart.

## Technologies Used

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* Google Colab / Jupyter Notebook
* Git & GitHub

## Analysis and Expected Outcomes
The analysis explores the following questions:

* What is the typical age, gender, and country profile of respondents?
* What share of respondents have sought treatment?
* Are people with a family history of mental illness more likely to seek treatment?
* How often does mental health interfere with work?
* How many employers provide benefits, care options, and wellness programs?
* How do results differ by company size, remote work, and tech vs non-tech companies?

The actual findings will be determined after running the analysis on the dataset.

## Limitations
The data is from a 2014 survey, and findings describe the respondents only, not the wider tech industry.

## Conclusion
This project demonstrates how Python and its data libraries can be used to turn raw survey responses into meaningful insights on mental health, treatment-seeking, and workplace support in tech.

## Dataset Credit
OSMI (Open Sourcing Mental Illness), Mental Health in Tech Survey, Kaggle.
https://www.kaggle.com/datasets/osmi/mental-health-in-tech-survey
