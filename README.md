# Breast-Cancer-Patient-Dashboard

This **interactive Streamlit dashboard** visualizes insights from the **SEER Breast Cancer Dataset (2006-2010)**.


## Features
- **Interactive Filters:** Age, Race, Marital Status, Tumor Size
- **Key Metrics:** Total Patients, Average Survival, Survival Rate
- **Data Visualizations:**
  - **Survival Distribution**
  - **Tumor Size Impact on Survival**
  - **Race-wise Survival Trends**
- **Modern UI/UX:** Improved design with custom colors and enhanced readability.

## How to Run
1. Install dependencies:
   ```bash
   pip install streamlit pandas plotly
   ```
2. Place your dataset (breast_cancer_data.csv) in the project folder.
3. Run the Streamlit app:
```bash
streamlit run app.py
```
## Dataset Information

Source: SEER Breast Cancer Dataset
Timeframe: 2006-2010
Key Features:
Patient Details: Age, Race, Marital Status
Cancer Staging: T Stage, N Stage, Grade, Tumor Size
Treatment Response: Estrogen Status, Progesterone Status
Survival Metrics: Survival Months, Status (Alive/Deceased)

## Insights & Takeaways

- Tumor Size & Survival: Smaller tumors correlate with longer survival.
- Race Impact: Some racial groups have better survival trends.
- Age Factor: Younger patients tend to have longer survival.

## Future Enhancements

- Add Machine Learning Predictions for survival
- More Advanced Filters & Charts for deeper insights
- Built with Streamlit & Plotly | Empowering Data Science for Healthcare


---

### **Next Steps & Enhancements**
- **Modernized UI with better colors & layout**
- **Smoother filters & improved metric display**
- **Enhanced readability with custom themes**
- **Add a ML survival predictor?**
- **More advanced filters (e.g., Cancer Grade, Node Analysis)?**
  
Would you like me to **add predictive modeling** for survival rates? 😃