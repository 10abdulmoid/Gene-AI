import streamlit as st
import numpy as np

# Load the .npy file
file_path = "resultgene_1.npy"
data = np.load(file_path)

# Display the data
st.title("Display Data from resultgene_1.npy")

st.write("Here is the data loaded from the .npy file:")

# Display the data as a table
st.write(data)

# Display summary statistics
st.write("Summary Statistics:")
st.write(f"Shape of data: {data.shape}")
st.write(f"Data type: {data.dtype}")
if np.issubdtype(data.dtype, np.number):
    st.write(f"Mean: {np.mean(data)}")
    st.write(f"Standard Deviation: {np.std(data)}")
    st.write(f"Min: {np.min(data)}")
    st.write(f"Max: {np.max(data)}")
else:
    st.write("Data is not numeric, summary statistics not available.")
