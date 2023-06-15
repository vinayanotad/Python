import tkinter as tk
import pandas as pd

def save_data():
    #  Get the input values
    customer_id = id_entry.get()
    customer_name = name_entry.get()
    product_name = product_entry.get()
    product_price = float(price_entry.get())
    phone_number = phone_entry.get()
    
    # Create a DataFrame with the data
    data = {
        'ID': [customer_id],
        'Customer Name': [customer_name],
        'Product Name': [product_name],
        'Product Price': [product_price],
        'Phone Number': [phone_number]
    }
    df = pd.DataFrame(data)
    
    # Append the data to the Excel file
    with pd.ExcelWriter('customer_data.xlsx', mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
    
    # Clear the input fields
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    product_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    
def calculate_insights():
    # Read the data from the Excel file
    df = pd.read_excel('customer_data.xlsx', sheet_name='Sheet1')
    
    # Perform operations to aggregate data values
    total_sales = df['Product Price'].sum()
    average_price = df['Product Price'].mean()
    highest_price = df['Product Price'].max()
    lowest_price = df['Product Price'].min()
    
    # Display the insights in a message box
    message = f"Total Sales: {total_sales}\nAverage Price: {average_price}\nHighest Price: {highest_price}\nLowest Price: {lowest_price}"
    tk.messagebox.showinfo("Insights", message)
    
# Create the main Tkinter window
window = tk.Tk()
window.title("Customer Data Recorder")

# Create labels and entry fields for each data field
id_label = tk.Label(window, text="ID:")
id_label.pack()
id_entry = tk.Entry(window)
id_entry.pack()

name_label = tk.Label(window, text="Customer Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

product_label = tk.Label(window, text="Product Name:")
product_label.pack()
product_entry = tk.Entry(window)
product_entry.pack()

price_label = tk.Label(window, text="Product Price:")
price_label.pack()
price_entry = tk.Entry(window)
price_entry.pack()

phone_label = tk.Label(window, text="Phone Number:")
phone_label.pack()
phone_entry = tk.Entry(window)
phone_entry.pack()

# Create buttons to save data and calculate insights
save_button = tk.Button(window, text="Save Data", command=save_data)
save_button.pack()

insights_button = tk.Button(window, text="Calculate Insights", command=calculate_insights)
insights_button.pack()

# Start the Tkinter event loop
window.mainloop()
