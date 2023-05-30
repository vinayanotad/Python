import tkinter as tk
import csv

def save_data():
    customer_id = id_entry.get()
    customer_name = name_entry.get()
    product_name = product_entry.get()
    product_price = price_entry.get()
    phone_number = phone_entry.get()

    with open('customer_data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([customer_id, customer_name, product_name, product_price, phone_number])

    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    product_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

def aggregate_data():
    with open('customer_data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        total_price = 0
        total_entries = 0

        for row in reader:
            price = float(row[3])
            total_price += price
            total_entries += 1

        avg_price = total_price / total_entries
        result_label.config(text=f"Total entries: {total_entries}\nAverage price: {avg_price:.2f}")

# Create the main window
window = tk.Tk()
window.title("Customer Data Application")

# Create labels
id_label = tk.Label(window, text="ID:")
name_label = tk.Label(window, text="Name:")
product_label = tk.Label(window, text="Product:")
price_label = tk.Label(window, text="Price:")
phone_label = tk.Label(window, text="Phone:")

# Create entry fields
id_entry = tk.Entry(window)
name_entry = tk.Entry(window)
product_entry = tk.Entry(window)
price_entry = tk.Entry(window)
phone_entry = tk.Entry(window)

# Create save button
save_button = tk.Button(window, text="Save", command=save_data)

# Create aggregate button
aggregate_button = tk.Button(window, text="Aggregate", command=aggregate_data)

# Create result label
result_label = tk.Label(window, text="")

# Grid layout
id_label.grid(row=0, column=0, sticky="e")
name_label.grid(row=1, column=0, sticky="e")
product_label.grid(row=2, column=0, sticky="e")
price_label.grid(row=3, column=0, sticky="e")
phone_label.grid(row=4, column=0, sticky="e")

id_entry.grid(row=0, column=1)
name_entry.grid(row=1, column=1)
product_entry.grid(row=2, column=1)
price_entry.grid(row=3, column=1)
phone_entry.grid(row=4, column=1)

save_button.grid(row=5, column=1, pady=10)
aggregate_button.grid(row=6, column=1, pady=10)
result_label.grid(row=7, column=1)

# Start the main loop
window.mainloop()
