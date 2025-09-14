import streamlit as st
import mysql.connector

# Database connection function
def get_connection():
    return mysql.connector.connect(
        host="82.180.143.66",
        user="u263681140_AttendanceInt",
        password="SagarAtten@12345",
        database="u263681140_Attendance"
    )

# Streamlit App
st.set_page_config(page_title="Farmer Login", page_icon="🌾", layout="centered")

st.title("🌾 Farmer Login")

userid = st.text_input("Enter RFID No or Mobile No")
password = st.text_input("Enter Password", type="password")

if st.button("Login"):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """SELECT * FROM Farmers_data 
                   WHERE (RFID_No = %s OR mobile_no = %s) AND password = %s"""
        cursor.execute(query, (userid, userid, password))
        result = cursor.fetchone()

        if result:
            st.success(f"✅ Login Successful! Welcome, {result['farmer_name']}")
            
            # Display farmer details
            st.subheader("Farmer Details:")
            st.write(f"👤 Name: {result['farmer_name']}")
            st.write(f"📞 Mobile: {result['mobile_no']}")
            st.write(f"🏠 Address: {result['address']}")
            st.write(f"🏦 Bank: {result['bank']}")
            st.write(f"💳 Account No: {result['account_no']}")
            st.write(f"🐄 Cattle Type: {result['cattle_type']}")
        else:
            st.error("❌ Invalid RFID/Mobile No or Password")

        cursor.close()
        conn.close()
    except Exception as e:
        st.error(f"Database connection error: {e}")
