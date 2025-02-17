import streamlit as st
import pandas as pd
import plotly.express as px

# Custom theme colors
PRIMARY_COLOR = "#FF4B4B"  # A soft red-pink color
SECONDARY_COLOR = "#2C3E50"  # Dark navy
BACKGROUND_COLOR = "#F8F9FA"  # Light grey

# Apply Modern Styling
st.set_page_config(page_title="Breast Cancer Dashboard", page_icon="🎗️", layout="wide")

# Custom Styling
st.markdown(
    f"""
    <style>
        body {{
            background-color: {BACKGROUND_COLOR};
            color: {SECONDARY_COLOR};
        }}
        .main {{
            background-color: white;
            padding: 20px;
            border-radius: 10px;
        }}
        .stButton>button {{
            background-color: {PRIMARY_COLOR} !important;
            color: white !important;
            border-radius: 5px;
        }}
        .stSidebar {{
            background-color: {SECONDARY_COLOR};
            color: white;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Load dataset
@st.cache_data
def load_data():
    file_path = "breast_cancer_data.csv"  # Update with actual file path
    df = pd.read_csv(file_path)
    return df

df = load_data()

# Sidebar for Filters
st.sidebar.markdown("<h2 style='color:white;'>🔍 Filters</h2>", unsafe_allow_html=True)
age_range = st.sidebar.slider("Select Age Range", int(df["Age"].min()), int(df["Age"].max()), (40, 80))
race_filter = st.sidebar.multiselect("Select Race", df["Race"].unique(), default=df["Race"].unique())
marital_status_filter = st.sidebar.multiselect("Select Marital Status", df["Marital Status"].unique(), default=df["Marital Status"].unique())

# Apply Filters
filtered_df = df[
    (df["Age"].between(age_range[0], age_range[1])) &
    (df["Race"].isin(race_filter)) &
    (df["Marital Status"].isin(marital_status_filter))
]

# Dashboard Title
st.markdown("<h1 style='text-align: center; color:#FF4B4B;'>🎗️ Breast Cancer Patient Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# Key Metrics in Columns
st.subheader("📊 Key Insights")
col1, col2, col3 = st.columns(3)

col1.metric("Total Patients", len(filtered_df), "📌 Filtered Dataset")
col2.metric("Avg Survival (Months)", round(filtered_df["Survival Months"].mean(), 1), "⏳ Survival Trend")
survival_rate = round((filtered_df["Status"].value_counts(normalize=True) * 100)["Alive"], 2)
col3.metric("Survival Rate", f"{survival_rate} %", "📈 Survival Probability")

# Modern Visuals
st.subheader("📅 Survival Distribution")
fig1 = px.histogram(filtered_df, x="Survival Months", nbins=20, color_discrete_sequence=[PRIMARY_COLOR])
fig1.update_layout(template="plotly_white", title="Distribution of Survival Months")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("🧪 Tumor Size vs. Survival")
fig2 = px.scatter(filtered_df, x="Tumor Size", y="Survival Months", color="Status", trendline="ols",
                   color_discrete_sequence=[PRIMARY_COLOR, "#3498DB"])
fig2.update_layout(template="plotly_white", title="Tumor Size Impact on Survival")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("🩸 Race-wise Survival Comparison")
fig3 = px.box(filtered_df, x="Race", y="Survival Months", color="Race",
              color_discrete_sequence=px.colors.qualitative.Set1)
fig3.update_layout(template="plotly_white", title="Survival Distribution Across Races")
st.plotly_chart(fig3, use_container_width=True)

# Insights Section
st.markdown("""
### 📌 Key Findings:
- **📊 Survival Months:** Patients with **smaller tumors tend to live longer**.
- **🩸 Race & Survival:** Race impacts survival months significantly.
- **📌 Age & Staging:** Younger patients tend to have longer survival durations.
""")

# Sidebar Footer
st.sidebar.markdown("<hr>", unsafe_allow_html=True)
st.sidebar.info("📌 Data Source: SEER Breast Cancer Dataset (2006-2010)")