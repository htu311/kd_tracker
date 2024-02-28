import streamlit as st
import pandas as pd
import requests

from urllib.error import URLError
#st.title('🐟🐦🐍🐢🐹🐰🐷🐮🐑🐴 Veterinary Clinic 🐶🐱🐭🐾🐧🐘🦒🐨🐼🐒')
st.title('🐶🐴 Veterinary Clinic 🐮🐱')
st.header('⚙️ Services')
st.text('🏠 Home Visit')
st.text('🩺 General Health Check up')

st.header('Tracker')

    
def write_to_excel(data):
    # Write data to Excel file
    file_path = "output.xlsx"
    data.to_excel(file_path, index=False)
    return file_path

def main():
    st.title("Data to Excel App")

    # Create a form for user input
    st.subheader("Enter Data")
    Date, Description ,Amount ,Comments = st.columns([1, 16])
    with Date:
        column1_data = st.text_input("Date", "")
    with Description:
        column2_data = st.text_input("Description", "")
    with Amount:
        column3_data = st.text_input("Amount", "")
    with Comments:
        column3_data = st.text_input("Comments", "")
   
    # Create a button to submit the data
    if st.button("Submit"):
        # Create a DataFrame from the user input
        data = pd.DataFrame({
            "Date": [column1_data],
            "Description": [column2_data],
            "Amount": [column3_data],
            "Comments": [column4_data]
        })

        st.dataframe(data)
        
        # Write data to Excel file
        #file_path = write_to_excel(data)

        # Display a link to download the Excel file
        #st.success(f"Data written to Excel file. [Download Excel file]({file_path})")

if __name__ == "__main__":
    main()
