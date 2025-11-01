# 🧠 Brain Stroke Analysis

## 🌟 Overview  
This project analyzes a healthcare dataset to identify **key medical and lifestyle factors** contributing to brain-stroke occurrences.  
It combines **Python-based exploratory data analysis (EDA)** with an **interactive Tableau dashboard** to visualize risk indicators and uncover insights for preventive healthcare.

> 💡 *Goal:* Use data storytelling to highlight patterns that inform stroke prevention strategies.

---

## 📊 Interactive Tableau Dashboard  
Explore the full interactive dashboard here:  
🔗 [**View Dashboard on Tableau Public**](https://tinyurl.com/BrainStrokeDashboard)  

The dashboard reveals:  
- Stroke-risk distribution by **Age**, **BMI**, and **Glucose Level**  
- Lifestyle and demographic analysis (Gender, Smoking Status, Residence Type)  
- Key health variables influencing **stroke occurrence probability**


![Dashboard Preview](visuals/tableau_dashboard_preview.png)


---

## 🧩 Data Workflow  
### 1️⃣ **Data Cleaning & Preparation**
- Handled missing **BMI** values using median imputation.  
- Standardized data types and renamed inconsistent columns.  
- Removed duplicates and ensured column consistency.  

### 2️⃣ **Exploratory Data Analysis (EDA)**
- Conducted EDA using **Pandas, Seaborn, and Matplotlib**.  
- Visualized variable relationships using heatmaps and pairplots.  
- Identified correlations between **hypertension, glucose, and age** with stroke incidence.  

### 3️⃣ **Visualization & Storytelling**
- Designed an **interactive Tableau dashboard** for user-friendly exploration.  
- Built visual layers highlighting **risk segmentation** and **demographic drivers**.

---

## 🧠 Key Insights  
| Factor | Observation |
|--------|--------------|
| **Age** | Stroke likelihood rises significantly after 50 years. |
| **Hypertension & Heart Disease** | Strongly correlated with past stroke history. |
| **Average Glucose Level** | High glucose values increase stroke probability. |
| **BMI** | Moderate correlation — higher BMI linked to higher risk. |

---

## 🧰 Tools & Technologies  
- **Languages:** Python  
- **Libraries:** pandas, numpy, seaborn, matplotlib  
- **Visualization:** Tableau Public  
- **Environment:** Jupyter Notebook / VS Code  
- **Dataset:** Healthcare Stroke Prediction Dataset (Kaggle)

---
## 📁 Repository Structure

```
brain-stroke-analysis/
│
├── Stroke_Data_analysis.py
├── stroke_data_only.csv
├── visuals/
│   ├── correlation_heatmap.png
│   ├── feature_correlation_bar.png
│   └── tableau_dashboard_preview.png
├── README.md
└── requirements.txt
```


