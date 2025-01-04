import streamlit as st
import mysql.connector
from mysql.connector import OperationalError, IntegrityError

# MySQL database connection details
host = "82.180.143.66"
user = "u263681140_students"
passwd = "testStudents@123"
db_name = "u263681140_students"

# Function to fetch data from BusPass table
def fetch_data_from_db():
    try:
        # Establishing connection to the database using mysql.connector
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=passwd,
            database=db_name
        )
        cursor = conn.cursor()
        
        # Query to fetch all data from BusPass table
        query = "SELECT * FROM BusPass"
        cursor.execute(query)
        rows = cursor.fetchall()
        
        # Fetching column names
        col_names = [desc[0] for desc in cursor.description]
        
        # Closing the connection
        cursor.close()
        conn.close()
        
        return col_names, rows
    except OperationalError as e:
        st.error(f"Database connection error: {e}")
        return None, None
    except IntegrityError as e:
        st.error(f"Database integrity error: {e}")
        return None, None

# Streamlit app
st.title("BusPass Table Data")

col_names, rows = fetch_data_from_db()

if col_names and rows:
    # Display the data in a table format
    st.subheader("Data Retrieved from BusPass Table")
    st.table([dict(zip(col_names, row)) for row in rows])
else:
    st.warning("No data retrieved or there was an error.")
