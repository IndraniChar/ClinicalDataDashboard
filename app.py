import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Clinical Dashboard", layout="wide")

st.title("🏥 Clinical Data Dashboard")
st.write("Upload and analyze clinical trial data")

# File upload
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    # Show data
    st.write("### Data Preview")
    st.dataframe(df)
    
    # Basic stats
    st.write("### Statistics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Patients", len(df))
    col2.metric("Columns", len(df.columns))
    col3.metric("Total Cells", df.size)
    
    # Show column info
    if st.checkbox("Show Column Details"):
        st.write(df.dtypes)
    
    # Simple visualization
    if len(df) > 0:
        numeric_cols = df.select_dtypes(include=['number']).columns
        if len(numeric_cols) > 0:
            st.write("### Distribution")
            col_to_plot = st.selectbox("Select column to plot", numeric_cols)
            fig = px.histogram(df, x=col_to_plot)
            st.plotly_chart(fig)
    
    # Download button
    csv = df.to_csv(index=False)
    st.download_button(
        "📥 Download Processed Data",
        csv,
        "clinical_data_processed.csv"
    )
else:
    st.info("👆 Please upload a CSV file to begin")
    st.write("Sample CSV format:")
    st.code("""PatientID,Age,Gender,Treatment,Site
1,42,F,Drug,Site1
2,35,M,Placebo,Site2
3,56,F,Drug,Site1
4,48,M,Drug,Site3""")
