import streamlit as st
import plotly.express as px
import pandas as pd

# Load data
df = pd.read_csv('company_esg_financial_dataset.csv')

st.title("Interactive 3D ESG Dashboard")

# Sidebar controls
st.sidebar.header("Controls")
x_axis = st.sidebar.selectbox(
    "X-Axis",
    options=['ESG_Overall', 'ESG_Environmental', 'ProfitMargin', 'Revenue'],
    index=0
)

y_axis = st.sidebar.selectbox(
    "Y-Axis",
    options=['ESG_Social', 'MarketCap', 'GrowthRate'],
    index=1
)

z_axis = st.sidebar.selectbox(
    "Z-Axis",
    options=['ESG_Governance', 'CarbonEmissions', 'EnergyConsumption'],
    index=0
)

year_range = st.sidebar.slider(
    "Year Range",
    min_value=int(df['Year'].min()),
    max_value=int(df['Year'].max()),
    value=(int(df['Year'].min()), int(df['Year'].max()))
)

industries = st.sidebar.multiselect(
    "Filter Industries",
    options=df['Industry'].unique(),
    default=df['Industry'].unique()
)

# Filter data
filtered_df = df[
    (df['Year'] >= year_range[0]) & 
    (df['Year'] <= year_range[1]) & 
    (df['Industry'].isin(industries))
]

# Create 3D plot
fig = px.scatter_3d(
    filtered_df,
    x=x_axis,
    y=y_axis,
    z=z_axis,
    color='Industry',
    size='Revenue',
    hover_name='CompanyName',
    hover_data=['Region', 'ProfitMargin'],
    title=f"3D ESG Analysis: {x_axis} vs {y_axis} vs {z_axis}"
)

fig.update_layout(
    scene=dict(
        xaxis_title=x_axis,
        yaxis_title=y_axis,
        zaxis_title=z_axis
    ),
    height=800,
    margin=dict(l=0, r=0, b=0, t=30)
)

st.plotly_chart(fig, use_container_width=True)