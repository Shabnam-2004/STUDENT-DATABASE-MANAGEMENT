from tkinter import messagebox 

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