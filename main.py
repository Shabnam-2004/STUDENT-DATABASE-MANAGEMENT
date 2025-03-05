import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import pymysql
from tkcalendar import DateEntry
from validate import validate_contact_input,validate_address_input,validate_full_name_input

def create_database_and_table():
    try:
        # Connect to MySQL server First
        conn = pymysql.connect(host="localhost", user="root", password="")
        curr = conn.cursor()
        
        # Create database if it does not exist
        curr.execute("CREATE DATABASE IF NOT EXISTS sms1")
        
        # Use the newly created database
        curr.execute("USE sms1")
        
        # Create table if it does not exist
        curr.execute("""
            CREATE TABLE IF NOT EXISTS data (
                rollno VARCHAR(20),
                name VARCHAR(100),
                class VARCHAR(20),
                section VARCHAR(10),
                contact VARCHAR(20),
                fathersname VARCHAR(100),
                address TEXT,
                gender VARCHAR(10),
                dob VARCHAR(10)
            )
        """)
        
        # Close the connection
        conn.commit()
        conn.close()
        
    except pymysql.MySQLError as e:
        print(f"Error while creating database or table: {e}")

# Call the function to create the database and table
create_database_and_table()


#==========functions==========#

def fetch_data():
    conn = pymysql.connect(host="localhost", user="root", password="", database="sms1")
    curr = conn.cursor()
    curr.execute("SELECT * FROM data")
    rows = curr.fetchall()
    
    # Clear existing data in the Treeview
    student_table.delete(*student_table.get_children())
    
    # Insert new data into the Treeview
    for row in rows:
        student_table.insert('', tk.END, values=row)

    conn.close()  # Close connection


def add_func():
    if rollno.get() == "" or name.get() == "" or class_var.get() == "":
        messagebox.showerror("Error!","Please fill all the fields!") 
    else:
        conn = pymysql.connect(host="localhost",user="root",password="",database="sms1")    
        curr = conn.cursor()
        curr.execute("INSERT INTO data VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(rollno.get(),name.get(),class_var.get(),section.get(),contact.get(),fathersname.get(),address.get(),gender.get(),dob.get()))  
        conn.commit()
        conn.close() 

        fetch_data()

def get_cursor(event):
    cursor_row = student_table.focus()
    content = student_table.item(cursor_row)
    row = content['values']
    
    if len(row) > 0:  # Ensure there's at least one item in the row
        rollno.set(row[0])
        name.set(row[1])
        class_var.set(row[2])
        section.set(row[3])
        contact.set(row[4])
        fathersname.set(row[5])
        address.set(row[6])
        gender.set(row[7])
        dob.set(row[8])
    else:
        messagebox.showwarning("Selection Error", "No data found for the selected row!")


def clear():
    rollno.set("")
    name.set("") 
    class_var.set("")
    section.set("")
    contact.set("") 
    fathersname.set("")
    address.set("") 
    gender.set("") 
    dob.set("")

 
def update_func():
    selected_item = student_table.selection()
    if selected_item:
        # Get the original roll number (the roll number before update)
        originalId = student_table.item(selected_item, 'values')[0]
        
        # Open the database connection and create a cursor
        conn = pymysql.connect(host="localhost", user="root", password="", database="sms1")
        curr = conn.cursor()
        
        # Check if the new roll number already exists in the database
        curr.execute("""SELECT rollno FROM data WHERE rollno=%s AND rollno!=%s""", (rollno.get(), originalId))
        if curr.fetchone():
            messagebox.showerror("Error", "This Student ID already exists. Please use a different ID.")
        else:
            try:
                # Execute the update querys
                curr.execute("""UPDATE data SET rollno=%s, name=%s, class=%s, section=%s, contact=%s, fathersname=%s, address=%s, gender=%s, dob=%s WHERE rollno=%s""", (
                    rollno.get(),  # New roll number
                    name.get(),
                    class_var.get(),
                    section.get(),
                    contact.get(),
                    fathersname.get(),
                    address.get(),
                    gender.get(),
                    dob.get(),
                    originalId,  # The old roll number for WHERE clause
                ))
                conn.commit()  # Commit the changes
                clear()  # Clear the input fields after update
                fetch_data()  # Refresh the table with updated data
                messagebox.showinfo("Success", "Student information updated successfully.")
            except Exception as e:
                messagebox.showerror("Database Error", f"An error occurred: {str(e)}")
            finally:
                conn.close()  # Close the connection




def delete_func():
    if rollno.get() == "":
        messagebox.showerror("Error", "Please enter a Roll Number to delete!")
    else:
        conn = pymysql.connect(host="localhost", user="root", password="", database="sms1")
        curr = conn.cursor()
        
        # Execute DELETE query
        curr.execute("DELETE FROM data WHERE rollno=%s", (rollno.get(),))
        conn.commit()  # Commit the changes
        conn.close()  # Close connection
        
        fetch_data()  # Refresh Treeview after deletion
        messagebox.showinfo("Success", "Student record deleted successfully!")
        clear()  # Clear form fields

            


def limit_chars(*args):
    value = entry_text.get()
    if len(value) > 50:
        entry_text.set(value[:50])

      #=============================#


win = tk.Tk()
win.geometry("1280x720+0+0")
screen_width = win.winfo_screenwidth()
screen_height=win.winfo_screenheight()

win.title("Student Hub")

win.config(bg="#C0C0C0")

title_label=tk.Label(win,text="STUDENT HUB",font=("Inter",30,"bold"),fg="#ffffff", bg="#15163A")
title_label.pack(side=tk.TOP,fill=tk.X)

frame_height=700 if screen_height > 720 else 590


detail_frame = tk.LabelFrame(win,bg="#D9D9D9",border=0)
detail_frame.place(x=24,y=90,width=369,height=frame_height)

detail_title_container=tk.LabelFrame(detail_frame, bg="#15163A",border=0)
detail_title_container.place(x=0,y=0,width=420,height=50)

detail_title = tk.Label(detail_title_container, text="ENTER DETAILS",font=("Inter",20,"bold"),foreground="#FFFFFF",bg="#15163A",border=0)
detail_title.place(x=80,y=10)

# Set width based on resolution
frame_width = 1070 if screen_width > 1280 else 800


data_frame = tk.Frame(win,bd=0,bg="#D9D9D9") 
data_frame.place(x=435,y=90,width=frame_width,height=frame_height)

#======varibales=============#

rollno = tk.StringVar()
name = tk.StringVar()
class_var = tk.StringVar()
section = tk.StringVar()
contact = tk.StringVar()
fathersname = tk.StringVar()
address = tk.StringVar()
gender = tk.StringVar()
dob = tk.StringVar()

search_by = tk.StringVar()


# Create a validation command that can be used on the Entry widget
validate_contacts = detail_frame.register(validate_contact_input)
validate_name = detail_frame.register(validate_full_name_input)
validate_address = detail_frame.register(validate_address_input)

#=======Entry=======#

rollno_lbl = tk.Label(detail_frame,text="Roll No:",font=("Inter",14,"bold"),bg=detail_frame.cget("bg"),fg="#15163A")
rollno_lbl.place(x=0,y=60)

rollno_ent = tk.Entry(detail_frame,bd=1,font=("Inter",14,"bold"),textvariable=rollno,relief="solid")
rollno_ent.place(x=140,y=60)

name_lbl = tk.Label(detail_frame,text="Name:",font=("Inter",14,"bold"),bg=detail_frame.cget("bg"),fg="#15163A")
name_lbl.place(x=0,y=100)

name_ent = tk.Entry(detail_frame,bd=1,font=("Inter",14,"bold"),textvariable=name,relief="solid",validate="key",validatecommand=(validate_name,"%P"))
name_ent.place(x=140,y=100)

class_lbl = tk.Label(detail_frame,text="Class:",font=("Inter",14,"bold"),bg=detail_frame.cget("bg"),fg="#15163A")
class_lbl.place(x=0,y=140)

class_ent = tk.Entry(detail_frame,bd=1,font=("Inter",14,"bold"),textvariable=class_var,relief="solid")
class_ent.place(x=140,y=140)

section_lbl = tk.Label(detail_frame,text="Section:",font=("Inter",14,"bold"),bg=detail_frame.cget("bg"),fg="#15163A")
section_lbl.place(x=0,y=180)

section_ent = tk.Entry(detail_frame,bd=1,font=("Inter",14,"bold"),textvariable=section,relief="solid")
section_ent.place(x=140,y=180)

contact_lbl = tk.Label(detail_frame,text="Contact:",font=("Inter",14,"bold"),bg=detail_frame.cget("bg"),fg="#15163A")
contact_lbl.place(x=0,y=220)

Contact_ent = tk.Entry(detail_frame,bd=1,font=("Inter",14,"bold"),textvariable=contact,relief="solid",validate="key",validatecommand=(validate_contacts,"%P"))
Contact_ent.place(x=140,y=220)

fathersname_lbl = tk.Label(detail_frame,text="Father Name:",font=("Inter",14,"bold"),bg=detail_frame.cget("bg"),fg="#15163A")
fathersname_lbl.place(x=0,y=260)

fathersname_ent = tk.Entry(detail_frame,bd=1,font=("Inter",14,"bold"),textvariable=fathersname,relief="solid",validate="key",validatecommand=(validate_name,"%P"))
fathersname_ent.place(x=140,y=260)

address_lbl = tk.Label(detail_frame,text="Address:",font=("Inter",14,"bold"),bg=detail_frame.cget("bg"),fg="#15163A")
address_lbl.place(x=0,y=300)

address_ent = tk.Entry(detail_frame,bd=1,font=("Inter",14,"bold"),textvariable=address,relief="solid",validate="key",validatecommand=(validate_address,"%P"))
address_ent.place(x=140,y=300)

gender_lbl = tk.Label(detail_frame,text="Gender:",font=("Inter",14,"bold"),bg=detail_frame.cget("bg"),fg="#15163A")
gender_lbl.place(x=0,y=340)

gender_ent = ttk.Combobox(detail_frame,font=("Inter",14,"bold"),state="readonly",textvariable=gender,width=18)
gender_ent['values'] = ("Male","Female","others")
gender_ent.place(x=140,y=340)

dob_lbl = tk.Label(detail_frame,text="D.O.B:",font=("Inter",14,"bold"),bg=detail_frame.cget("bg"),fg="#15163A")
dob_lbl.place(x=0,y=380)

dob_ent = DateEntry(detail_frame, date_pattern="dd-mm-yyyy", width=18, font=("Inter", 15,"bold"),relief="solid",bd=1, textvariable=dob)
dob_ent.place(x=140,y=380)

#===================#



#=====BUTTONS=====#

btn_frame = tk.Frame(detail_frame,bg="#15163A")
btn_frame.place(x=10,y=450,width=350,height=130)

add_btn = tk.Button(btn_frame,bg="#D9D9D9",text="ADD",font=("Inter", 14,"bold"),width=10,command=add_func,bd=3,relief="sunken")
add_btn.place(x=20,y=10)

update_btn = tk.Button(btn_frame,bg="#D9D9D9",text="UPDATE",font=("Inter", 14,"bold"),width=10,command=update_func,bd=3,relief="sunken")
update_btn.place(x=200,y=10)

delete_btn = tk.Button(btn_frame,bg="#D9D9D9",text="DELETE",font=("Inter", 14,"bold"),width=10,command=delete_func,bd=3,relief="sunken")
delete_btn.place(x=20,y=80)

clear_btn = tk.Button(btn_frame,bg="#D9D9D9",text="CLEAR",font=("Inter", 14,"bold"),width=10,command=clear,bd=3,relief="sunken")
clear_btn.place(x=200,y=80)
#=================#



#=====Search======#

search_frame = tk.Frame(data_frame,bg="#15163A",bd=0,width=frame_width,height=50)
search_frame.place(x=0,y=0)

entry_text = tk.StringVar()
entry_text.trace("w", limit_chars)
search_entry=tk.Entry(search_frame,bg="#FFFFFF",font=("Inter", 20,"bold"),fg="#092B53",textvariable=entry_text)
search_entry.place(x=8,y=6,height=38,width=frame_width-15)

# SEARCH & CLEAR BUTTON FRAME 

button_frame = tk.Frame(search_entry,bg="#D9D9D9",width=100,height=50)
button_frame.place(relx=1.0,x=-100,y=0)

# Search image

search_image = Image.open("icon/search-people.png")
search_image = search_image.resize((35,35))
search_image = ImageTk.PhotoImage(search_image)
search_button = tk.Button(button_frame, image=search_image, bd=0, cursor="hand2",highlightthickness=3,background="#D9D9D9")
search_button.image = search_image
search_button.place(x=55, y=1)

# Clear image

clear_image = Image.open("icon/close.png")
clear_image = clear_image.resize((35,35))
clear_image = ImageTk.PhotoImage(clear_image)
clear_button = tk.Button(button_frame, image=clear_image, bd=0, cursor="hand2",highlightthickness=0,background="#D9D9D9")
clear_button.image = clear_image
clear_button.place(x=10, y=2)







#=======Database Frame===========#

main_frame = tk.Frame(data_frame,bg=detail_frame.cget("bg"),bd=0, width=frame_width,height=frame_height-50)
main_frame.place(x=0,y=50)
style = ttk.Style()
style.configure("Treeview.Heading", font=("Inter", 15, "bold"))  # Set column header font and style
style.configure("Treeview", font=("Inter", 15))


student_table = ttk.Treeview(main_frame,columns=("Roll No.","Name","Class","Section","Contact","Father's Name","Address","Gender","D.O.B"))


student_table.heading("Roll No.",text="Roll No.")
student_table.heading("Name",text="Name")
student_table.heading("Class",text="Class")
student_table.heading("Section",text="Section")
student_table.heading("Contact",text="Contact")
student_table.heading("Father's Name",text="Father's Name")
student_table.heading("Gender",text="Gender")
student_table.heading("D.O.B",text="D.O.B")
student_table.heading("Address",text="Address")

student_table['show'] = 'headings'

student_table.column("Roll No.",width=100)
student_table.column("Name",width=100)
student_table.column("Class",width=100)
student_table.column("Section",width=100)
student_table.column("Contact",width=100)
student_table.column("Father's Name",width=100)
student_table.column("Gender",width=100)
student_table.column("D.O.B",width=100)
student_table.column("Address",width=100)




student_table.place(x=8, y=7, width=frame_width-15, height=frame_height - 65)

fetch_data()

student_table.bind("<ButtonRelease-1>",get_cursor)
#=============================#

win.mainloop()

  
         