import tkinter as tk

def calculate():
    principal = float(principal_entry.get())
    interest = float(interest_entry.get())
    tenure = float(tenure_entry.get())
    downpayment=float(downpayment_entry.get())
    
    
    # calculate principal,monthly interest rate and tenure in months
    principal = principal-downpayment
    interest_rate = interest / (12 * 100)
    tenure_months = tenure 
    
    #   calculate EMI

    emi = (principal * interest_rate * ((1 + interest_rate) ** tenure_months)) / (((1 + interest_rate) ** tenure_months) - 1)
    
    
    # update EMI label
    emi_label.config(text="EMI: Rs. {:.2f}".format(emi))
    

    
    # paymentvalue = emi* tenure
    # totalinterest_value = paymentvalue - principal
    
    # totalinterest_value_label.config(text="Total Interest: {:.2f}".format(totalinterest_value ))
    
    

# create a window
window = tk.Tk()
window.title("EMI Calculator")
window.geometry("500x500")
window.configure(bg='lightyellow')


# adding a label to the root window
lbl = tk.Label(window, text = "EMI calculator",fg='blue',font=('bold',30))
lbl.pack()

#  create input fields

principal_label = tk.Label(window, text="Principal (Rs.):",font=('arial',17))
principal_label.pack()
principal_entry = tk.Entry(window)
principal_entry.pack()

interest_label = tk.Label(window, text="Interest Rate (% p.a.):",font=('arial',17))
interest_label.pack()
interest_entry = tk.Entry(window)
interest_entry.pack()

downpayment_label = tk.Label(window, text="Down Payment(Mention if 0):",font=('arial',17))
downpayment_label.pack()
downpayment_entry = tk.Entry(window)
downpayment_entry.pack()

tenure_label = tk.Label(window, text="Time Period (months):",font=('arial',17))
tenure_label.pack()
tenure_entry = tk.Entry(window)
tenure_entry.pack()

# clear=exit(calculate)


# create a button to calculate EMI
calculate_button = tk.Button(window, text="Calculate EMI",fg='Green',font=('bold',20),command=calculate)
calculate_button.pack()


# clear_button = tk.Button(window, text="CLEAR",fg='red',command=clear)
# clear_button.pack()

# create a label to display EMI
emi_label = tk.Label(window,bg='orange',font=('arial',19))
emi_label.pack()


#create a label to display total_interest_value
# totalinterest_value_label = tk.Label(window,bg='orange',font=('arial',17))
# totalinterest_value_label.pack()


# start the window
window.mainloop()



