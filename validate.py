from tkinter import messagebox 
import re

def validate_full_name_input(P):
    if not P:
        return True  
    if len(P) <= 60:
        return True
    messagebox.showerror("Invalid Full Name", "Please enter a maximum of 60 characters for Full Name.")
    return False

def validate_address_input(P):
    if not P:
        return True
    if len(P) <= 200:
        return True
    messagebox.showerror("Invalid Address", "Please enter a maximum of 200 characters for Address.")
    return False

def validate_contact_input(P):
    if len(P) == 0 or P.isdigit() and len(P) <= 10:
        return True
    messagebox.showerror("Invalid! Contact No", "Please Enter A 10 Digit Number.")
    return False

def validate_dob_input(event, dob_var):
    dob_value = dob_var.get()  # Get the selected date as string
    
    # Regular expression to match DD-MM-YYYY format
    dob_pattern = r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(\d{4})$"
    
    if not re.fullmatch(dob_pattern, dob_value):
        messagebox.showerror("Invalid Date of Birth", "Please enter DOB in DD-MM-YYYY format (e.g., 25-12-2000).")
        dob_var.set("")  # Clear invalid input