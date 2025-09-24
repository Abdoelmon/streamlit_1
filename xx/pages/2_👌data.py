import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Data Visualization App")
@st.cache_data
def load_data(file):
    return pd.read_csv(file)

data = st.file_uploader("Upload a CSV file", type=["csv"])
st.write("This is a simple data visualization app built with Streamlit.")

if data is not None:
    df = load_data(data)
    n_rows = st.slider("Select number of rows to display", min_value=5, max_value=len(df))
    num_of_cols = st.multiselect("Select columns to plot", df.columns.tolist(), default=df.columns.tolist())
    
    st.write(df[:n_rows][num_of_cols])

    tab1, tab2 = st.tabs(["Scatter Plot", "Histogram"])

    with tab1:
        col1,col2,col3 = st.columns(3)
        with col1:
            x_col = st.selectbox("Select X-axis", df.select_dtypes(include='number').columns.tolist())
        with col2:
            y_col = st.selectbox("Select Y-axis", df.select_dtypes(include='number').columns.tolist())
        with col3:
            color = st.selectbox("Select Color (optional)", [None] + df.columns.tolist())
        fig = px.scatter(df, x=x_col, y=y_col, color=color)
        st.plotly_chart(fig)
    
    with tab2:
        x_col_hist = st.selectbox("Select column for histogram", df.columns.tolist(), key='hist')
        fig_hist = px.histogram(df, x=x_col_hist)
        st.plotly_chart(fig_hist)