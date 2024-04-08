from tkinter import *
root = Tk()
root.geometry("550x300")
root.minsize(550, 300)
root.maxsize(550, 300)
root.title("ABC Travels")

Label(text="Welcome to ABC Travels! Fill out the below form.", font=("cosmicsans", 10, "bold"), pady= 10, padx=15).grid(row=0,column=3)

first_name = Label(root, text="First Name")
last_name = Label(root, text="Last Name")
contact = Label(root, text="Phone Number")
address = Label(root, text="Address")

first_name.grid(row=1, column=2)
last_name.grid(row=2, column=2)
contact.grid(row=3, column=2)
address.grid(row=4, column=2)

first_val = StringVar()
last_val = StringVar()
contact_val = StringVar()
address_val = StringVar()
prebookmeal_val = IntVar()

first_entry = Entry(root, textvariable= first_val)
last_entry = Entry(root, textvariable= last_val)
contact_entry = Entry(root, textvariable= contact_val)
address_entry = Entry(root, textvariable= address_val)
prebookmeal_checkbox = Checkbutton(text="Want to pre-book your meal?", variable= prebookmeal_val)

first_entry.grid(row=1, column=3)
last_entry.grid(row=2, column=3)
contact_entry.grid(row=3, column=3)
address_entry.grid(row=4, column=3)
prebookmeal_checkbox.grid(row=5, column=3, pady=10)

def submit():
    print("Thanks for Booking!")
Button(text="Submit", command= submit).grid(row=6, column=2)

root.mainloop()
