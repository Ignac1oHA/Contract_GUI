import tkinter as tk
from tkinter.ttk import *
from ttkthemes import ThemedTk


def generate():
    pass


def generate_excel():
    pass


def modify_excel():
    pass


def open_contract():
    pass


def delete_contract():
    pass


# just the GUI
window = ThemedTk(screenName="Contract Generator", theme="radiance")


window.title("Generate Docs")
# window.geometry("1400x700")
window.resizable(0, 0)

# with ttk we need to configure styles:
style = Style()
style.configure("TButton", font=("Arial", 12, 'bold'), width=25)
style.configure("TLabel", font=("Arial", 15), anchor=tk.W, width=30, foreground="darkblue")
style.configure("TEntry", font=("Arial", 15), anchor=tk.W)

title_image = tk.PhotoImage(file="IE GENERATOR.gif")
lb = Label(master=window, image=title_image)
lb.grid(row=0, pady=20, columnspan=3)

# Add the lawyer label and textbox
lb_lawyer = Label(master=window, text="Lawyer Name")
lb_lawyer.grid(row=1, column=0, padx=10)

et_lawyer_text = tk.StringVar()
et_lawyer = Entry(master=window, width=30, textvariable=et_lawyer_text)
et_lawyer.grid(row=1, column=1)

# Add the client label and textbox
lb_client = Label(master=window, text="Client Name")
lb_client.grid(row=2, column=0)

et_client_text = tk.StringVar()
et_client = Entry(master=window, width=30, textvariable=et_client_text)
et_client.grid(row=2, column=1)

# Add the service label and textbox
lb_service = Label(master=window, text="Service")
lb_service.grid(row=3, column=0)

et_service_text = tk.StringVar()
et_service = Entry(master=window, width=30, textvariable=et_service_text)
et_service.grid(row=3, column=1)

# compensation_value
lb_compensation = Label(master=window, text="Compensation Value / Hour")
lb_compensation.grid(row=4, column=0)

et_compensation_text = tk.StringVar()
et_compensation = Entry(master=window, width=30, textvariable=et_compensation_text)
et_compensation.grid(row=4, column=1)

# deposit_value
lb_deposit = Label(master=window, text="Deposit Value")
lb_deposit.grid(row=5, column=0)

et_deposit_text = tk.StringVar()
et_deposit = Entry(master=window, width=30, textvariable=et_deposit_text)
et_deposit.grid(row=5, column=1)

# refundable_deposit_value
lb_refundable = Label(master=window, text="Refundable Deposit Value")
lb_refundable.grid(row=6, column=0)

et_refundable_text = tk.StringVar()
et_refundable = Entry(master=window, width=30, textvariable=et_refundable_text)
et_refundable.grid(row=6, column=1)

# nonrefundable_deposit_value
lb_not_refundable = Label(master=window, text="Nonrefundable Deposit Value")
lb_not_refundable.grid(row=7, column=0)

et_non_refundable_text = tk.StringVar()
et_non_refundable = Entry(master=window, width=30, textvariable=et_non_refundable_text)
et_non_refundable.grid(row=7, column=1)

# deposit_date
lb_deposit_date = Label(master=window, text="Deposit Date")
lb_deposit_date.grid(row=8, column=0)

et_deposit_date_text = tk.StringVar()
et_deposit_date = Entry(master=window, width=30, textvariable=et_deposit_date_text)
et_deposit_date.grid(row=8, column=1)

# jurisdiction
lb_jurisdiction = Label(master=window, text="Jurisdiction")
lb_jurisdiction.grid(row=9, column=0)

et_jurisdiction_text = tk.StringVar()
et_jurisdiction = Entry(master=window, width=30, textvariable=et_jurisdiction_text)
et_jurisdiction.grid(row=9, column=1)

# status bar
lb_status = Label(master=window, text="", width=40)
lb_status.grid(row=10, column=0, columnspan=3, pady=20)

# Add the buttons
bt_generate = Button(master=window, text="Generate Contract", command=generate)
bt_generate.grid(row=1, column=2, padx=30)

bt_load_excel = Button(master=window, text="Generate from Excel", command=generate_excel)
bt_load_excel.grid(row=2, column=2, padx=30)

bt_load_excel = Button(master=window, text="Modify the Excel", command=modify_excel)
bt_load_excel.grid(row=3, column=2, padx=30)

bt_open_contract = Button(master=window, text="Open Contract", command=open_contract)
bt_open_contract.grid(row=4, column=2, padx=30)

bt_open_contract = Button(master=window, text="Delete Contract", command=delete_contract)
bt_open_contract.grid(row=5, column=2, padx=30)

bt_exit = Button(master=window, text="Exit", command=tk.sys.exit)
bt_exit.grid(row=11, column=2, pady=20)

# main loop
window.mainloop()
