import mysql.connector
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt


st.set_page_config(page_title="Kauvery")


conn=mysql.connector.connect(
       host='localhost',
       username='root',
       password='Nir@2003',
       database='code'
     )

my_cursor=conn.cursor()
print("successs")


def main():
     st.title("Kauvery Hospital");
    
     option=st.sidebar.selectbox(
        "Select a Menu",
        ("Register","Update","Read","Visualization")
     )


     if option=="Register":
           st.subheader("")
           Patient_name=st.text_input("Enter The Name")
           Age=st.number_input("Enter The Age",value=0)
           Contact_No=st.text_input("Enter The Number")
           From_Date=st.date_input("Enter The From_Date") 
           To_Date=st.date_input("Enter The To_Date ")
           Bill_Amount=st.text_input("Enter The Amount")
           if st.button("save"):
            sql= "insert into Users(Patient_name,Age,Contact_No,From_Date,To_Date,Bill_Amount) values(%s,%s,%s,%s,%s,%s)"
            val=(Patient_name,Age,Contact_No,From_Date,To_Date,Bill_Amount)
            my_cursor.execute(sql,val)
            conn.commit()
            st.success("record create success")

     if option == "Update":
        st.subheader("Delete Record")
        id = st.number_input("Enter your Patient_id", value=0)
        if st.button("Update"):
        # Delete the row from the database
            sql = "DELETE FROM Users WHERE Patient_id = %s"
            val = (id,)  # Note the comma to make it a tuple
            my_cursor.execute(sql, val)
            conn.commit()
            st.success("Successfully updated")

     if option=="Read":
           st.subheader("Database")
           my_cursor.execute("select * from Users")
           result=my_cursor.fetchall()
           st.table(result)   

           if __name__ =="__main__1":
                 main()

     if option=="Visualization":
          st.subheader("")
          category = st.selectbox("Select Category", ["Patient_name","Age","Contact_No","From_Date","To_Date","Bill_Amount"])
          query = "SELECT Patient_id, COUNT(*) FROM Users WHERE Patient_id= %s GROUP BY Bill_Amount"
          my_cursor.execute(query, (category,))
          data = my_cursor.fetchall()

          conn.close()

          labels = [row[0] for row in data]  # Accessing the first column
          counts = [row[6] for row in data]   # Accessing the second column

               # Create a bar chart
          fig, ax = plt.subplots()
          ax.bar(labels, counts)
          ax.set_xlabel(category)
          ax.set_ylabel('Count')
          ax.set_title('Counts by {}'.format(category))
          plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
          st.pyplot(fig)


if __name__== "__main__":
    main()