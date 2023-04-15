import tkinter as tk

main = tk.Tk ( className = "emi calculator" )

main.geometry("400x400")

label1 = tk.Label(main,text="Python")
txt1 = tk.Entry(main)
btn1 = tk.Button(main,text="Submit")

label1.grid(row=0,column=0)
txt1.grid(row=0,column=1)
btn1.grid(row=1,column=1)

main.mainloop()