import streamlit as st
import pandas as pd
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from urllib.error import URLError
#st.title('🐟🐦🐍🐢🐹🐰🐷🐮🐑🐴 Veterinary Clinic 🐶🐱🐭🐾🐧🐘🦒🐨🐼🐒')
st.title('🐶🐴 Veterinary Clinic 🐮🐱')
st.header('⚙️ Services')
st.text('🏠 Home Visit')
st.text('🩺 General Health Check up')

st.header('🍌🥭 Appointment Slots 🥝🍇')

def authenticate_google_sheets():
    # Define the scope for Google Sheets API
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    # Load credentials from a service account JSON file
    credentials = ServiceAccountCredentials.from_json_keyfile_name('your_service_account_credentials.json', scope)

    # Authenticate with Google Sheets API
    gc = gspread.authorize(credentials)
    
    return gc

def write_to_google_sheets(data):
    # Authenticate with Google Sheets
    gc = authenticate_google_sheets()

    # Open the Google Sheets spreadsheet by its URL
    # Replace 'YOUR_SPREADSHEET_URL' with the URL of your Google Sheets spreadsheet
    sh = gc.open_by_url('YOUR_SPREADSHEET_URL')

    # Select the first worksheet
    worksheet = sh.get_worksheet(0)

    # Clear existing content in the worksheet (optional)
    # worksheet.clear()

    # Convert DataFrame to a list of lists (values)
    values = data.values.tolist()

    # Append the data to the worksheet
    worksheet.append_rows(values)
    
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
