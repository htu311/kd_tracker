import streamlit as st
import pandas as pd
import requests
from urllib.error import URLError
#st.title('🐟🐦🐍🐢🐹🐰🐷🐮🐑🐴 Veterinary Clinic 🐶🐱🐭🐾🐧🐘🦒🐨🐼🐒')
st.title('🐟🐦🐮🐑🐴 Veterinary Clinic 🐶🐱🐭🐾🐒')
st.header('Vet Services')
st.text('🥗 Home Visit')
st.text('🥗 General Health Check up')

st.header('🍌🥭 Appointment Slots 🥝🍇')


def write_to_excel(data):
    # Write data to Excel file
    file_path = "output.xlsx"
    data.to_excel(file_path, index=False)
    return file_path

def main():
    st.title("Data to Excel App")

    # Create a form for user input
    st.subheader("Enter Data")
    col1, col2 = st.columns([1, 4])
    with col1:
        column1_data = st.text_input("Column 1", "")
    with col2:
        column2_data = st.text_input("Column 2", "")

    # Create a button to submit the data
    if st.button("Submit"):
        # Create a DataFrame from the user input
        data = pd.DataFrame({
            "Column 1": [column1_data],
            "Column 2": [column2_data]
        })

        st.dataframe(data)
        
        # Write data to Excel file
        #file_path = write_to_excel(data)

        # Display a link to download the Excel file
        #st.success(f"Data written to Excel file. [Download Excel file]({file_path})")

if __name__ == "__main__":
    main()
