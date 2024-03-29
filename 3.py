import tkinter as tk

def calculate():
    principal = float(principal_entry.get())
    interest = float(interest_entry.get())
    tenure = float(tenure_entry.get())
    down_payment=float(down_payment_entry.get())
    
    
    #Calculating loan amount
    loan_amount = principal - down_payment
    
    
    #  Calculating interest and profit
    interest_rate = (loan_amount * interest * tenure) / 100
    tenure_months = interest_rate / 2


    # calculate monthly interest rate and tenure in months
    # interest_rate = interest / (12 * 100)
    # tenure_months = tenure * 12
    
    
    # Calculating EMI
    # numerator = (interest / 100) * pow(1 + (interest / 100), tenure)
    # denominator = pow(1 + (interest / 100), tenure) - 1
    # emi = loan_amount * (numerator / denominator)

    
    #  calculate EMI
      
    emi = (principal * interest_rate * ((1 + interest_rate) ** tenure_months)) / (((1 + interest_rate) ** tenure_months) - 1)
    

    # update EMI label
    emi_label.config(text="EMI: Rs. {:.2f}".format(emi))

# create a window
window = tk.Tk()
window.title("EMI Calculator")


# adding a label to the root window
lbl = tk.Label(window, text = "EMI calculator",fg='blue')
lbl.pack()


# create input fields
principal_label = tk.Label(window, text="Principal (Rs.):")
principal_label.pack()
principal_entry = tk.Entry(window)
principal_entry.pack()

interest_label = tk.Label(window, text="Interest Rate (% p.a.):")
interest_label.pack()
interest_entry = tk.Entry(window)
interest_entry.pack()

tenure_label = tk.Label(window, text="Tenure (years):")
tenure_label.pack()
tenure_entry = tk.Entry(window)
tenure_entry.pack()


down_payment_label = tk.Label(window, text="Down Payment(mention if 0):")
down_payment_label.pack()
down_payment_entry = tk.Entry(window)
down_payment_entry.pack()


# create a button to calculate EMI
calculate_button = tk.Button(window, text="Calculate EMI",fg='Green',command=calculate)
calculate_button.pack()

# create a label to display EMI
emi_label = tk.Label(window)
emi_label.pack()

# start the window
window.mainloop()
