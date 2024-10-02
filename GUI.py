import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="crm_db"
)
cursor = db.cursor()

# Function to add a customer
def add_customer():
    first_name = entry_fname.get()
    last_name = entry_lname.get()
    email = entry_email.get()
    phone = entry_phone.get()
    address = entry_address.get()

    if first_name and last_name and email and phone:
        sql = "INSERT INTO customers (first_name, last_name, email, phone, address) VALUES (%s, %s, %s, %s, %s)"
        values = (first_name, last_name, email, phone, address)
        cursor.execute(sql, values)
        db.commit()
        messagebox.showinfo("Success", "Customer added successfully!")
    else:
        messagebox.showwarning("Input Error", "Please fill all fields.")

# Function to view customer details
def view_customer():
    customer_id = entry_cust_id.get()
    if customer_id:
        cursor.execute("SELECT * FROM customers WHERE customer_id = %s", (customer_id,))
        result = cursor.fetchone()
        if result:
            details = f"ID: {result[0]}\nName: {result[1]} {result[2]}\nEmail: {result[3]}\nPhone: {result[4]}\nAddress: {result[5]}"
            messagebox.showinfo("Customer Details", details)
        else:
            messagebox.showerror("Not Found", "Customer not found!")
    else:
        messagebox.showwarning("Input Error", "Please enter a Customer ID.")

# Function to log interaction
def log_interaction():
    customer_id = entry_cust_id.get()
    interaction_type = entry_interaction.get()
    notes = entry_notes.get()

    if customer_id and interaction_type:
        sql = "INSERT INTO interactions (customer_id, interaction_type, interaction_date, notes) VALUES (%s, %s, CURDATE(), %s)"
        values = (customer_id, interaction_type, notes)
        cursor.execute(sql, values)
        db.commit()
        messagebox.showinfo("Success", "Interaction logged successfully!")
    else:
        messagebox.showwarning("Input Error", "Please fill all required fields.")

# Function to track sales
def track_sales():
    customer_id = entry_cust_id.get()
    product = entry_product.get()
    amount = entry_amount.get()

    if customer_id and product and amount:
        sql = "INSERT INTO sales (customer_id, product, amount, sale_date) VALUES (%s, %s, %s, CURDATE())"
        values = (customer_id, product, amount)
        cursor.execute(sql, values)
        db.commit()
        messagebox.showinfo("Success", "Sale tracked successfully!")
    else:
        messagebox.showwarning("Input Error", "Please fill all required fields.")

# Create the main window
root = tk.Tk()
root.title("CRM System")
root.geometry("400x500")

# Add Customer Section
tk.Label(root, text="Add New Customer").pack(pady=10)
tk.Label(root, text="First Name").pack()
entry_fname = tk.Entry(root)
entry_fname.pack()

tk.Label(root, text="Last Name").pack()
entry_lname = tk.Entry(root)
entry_lname.pack()

tk.Label(root, text="Email").pack()
entry_email = tk.Entry(root)
entry_email.pack()

tk.Label(root, text="Phone").pack()
entry_phone = tk.Entry(root)
entry_phone.pack()

tk.Label(root, text="Address").pack()
entry_address = tk.Entry(root)
entry_address.pack()

tk.Button(root, text="Add Customer", command=add_customer).pack(pady=10)

# View Customer Section
tk.Label(root, text="View Customer Details").pack(pady=10)
tk.Label(root, text="Customer ID").pack()
entry_cust_id = tk.Entry(root)
entry_cust_id.pack()

tk.Button(root, text="View Customer", command=view_customer).pack(pady=10)

# Log Interaction Section
tk.Label(root, text="Log Interaction").pack(pady=10)
tk.Label(root, text="Interaction Type").pack()
entry_interaction = tk.Entry(root)
entry_interaction.pack()

tk.Label(root, text="Notes").pack()
entry_notes = tk.Entry(root)
entry_notes.pack()

tk.Button(root, text="Log Interaction", command=log_interaction).pack(pady=10)

# Track Sales Section
tk.Label(root, text="Track Sales").pack(pady=10)
tk.Label(root, text="Product").pack()
entry_product = tk.Entry(root)
entry_product.pack()

tk.Label(root, text="Amount").pack()
entry_amount = tk.Entry(root)
entry_amount.pack()

tk.Button(root, text="Track Sale", command=track_sales).pack(pady=10)

# Start the GUI loop
root.mainloop()
