import tkinter as tk
from tkinter import ttk

class PharmacyGUI:
    def __init__(self, pharmacy):
        self.pharmacy = pharmacy

        # Create the main window
        self.root = tk.Tk()
        self.root.title('Pharmacy Store Management System')

        # Set the theme to 'clam'
        ttk.Style().theme_use('vista')

        # Create the frames
        self.input_frame = ttk.Frame(self.root)
        self.button_frame = ttk.Frame(self.root)
        self.output_frame = ttk.Frame(self.root)

         # Create the widgets
        self.name_label = ttk.Label(self.input_frame, text='Name:')
        self.name_entry = ttk.Entry(self.input_frame)
        self.price_label = ttk.Label(self.input_frame, text='Price:')
        self.price_entry = ttk.Entry(self.input_frame)
        self.quantity_label = ttk.Label(self.input_frame, text='Quantity:')
        self.quantity_entry = ttk.Entry(self.input_frame)
        self.manu_label = ttk.Label(self.input_frame, text='Manufacture date: ')
        self.manu_entry = ttk.Entry(self.input_frame)
        self.expire_Label = ttk.Label(self.input_frame, text='Expire date: ')
        self.expire_entry = ttk.Entry(self.input_frame)
        self.supp_Label = ttk.Label(self.input_frame, text='Supplier: ')
        self.supp_entry = ttk.Entry(self.input_frame)
        self.create_button = ttk.Button(self.button_frame, text='Create', command=self.create_medicine)
        self.read_button = ttk.Button(self.button_frame, text='Search', command=self.read_medicine)
        self.update_button = ttk.Button(self.button_frame, text='Update', command=self.update_medicine)
        self.delete_button = ttk.Button(self.button_frame, text='Delete', command=self.delete_medicine)
        self.output_label = ttk.Label(self.output_frame, text='')

       # Add the widgets to the frames
        self.name_label.pack(side='left')
        self.name_entry.pack(side='left')
        self.price_label.pack(side='left')
        self.price_entry.pack(side='left')
        self.quantity_label.pack(side='left')
        self.quantity_entry.pack(side='left')
        self.manu_label.pack(side='left')
        self.manu_entry.pack(side='left')
        self.expire_Label.pack(side='left')
        self.expire_entry.pack(side='left')
        self.supp_Label.pack(side='left')
        self.supp_entry.pack(side='left')
        self.create_button.pack(side='left')
        self.read_button.pack(side='left')
        self.update_button.pack(side='left')
        self.delete_button.pack(side='left')
        self.output_label.pack(side='left')

        # Add the frames to the main window
        self.input_frame.pack()
        self.button_frame.pack()
        self.output_frame.pack()
    
        # Create the listbox
        self.medicine_list = tk.Listbox(self.root)

        # Populate the listbox with the medicine records
        self.populate_list()

        # Add the listbox to the main window
        self.medicine_list.pack()


    def create_medicine(self):
        # Get the values from the entries
        name = self.name_entry.get()
        price = self.price_entry.get()
        quantity = self.quantity_entry.get()

        # Create the medicine
        self.pharmacy.create_medicine(name, price, quantity)

        # Clear the entries
        self.name_entry.delete(0, 'end')
        self.price_entry.delete(0, 'end')
        self.quantity_entry.delete(0, 'end')

        # Update the output label
        self.output_label.config(text='Medicine created successfully!')
        self.populate_list()

    def read_medicine(self):
        # Get the name from the entry
        name = self.name_entry.get()

        # Read the medicine
        medicine = self.pharmacy.read_medicine(name)

        # Clear the entries
        self.name_entry.delete(0, 'end')
        self.price_entry.delete(0, 'end')
        self.quantity_entry.delete(0, 'end')

        # Update the output label
        if medicine:
            name, price, quantity = medicine
            self.output_label.config(text=f'Medicine: {name} ${price} x{quantity}')
        else:
            self.output_label.config(text='Medicine not found!')

    def update_medicine(self):
            # Get the values from the entries
            name = self.name_entry.get()
            price = self.price_entry.get()
            quantity = self.quantity_entry.get()

            # Update the medicine
            self.pharmacy.update_medicine(name, price, quantity)

            # Clear the entries
            self.name_entry.delete(0, 'end')
            self.price_entry.delete(0, 'end')
            self.quantity_entry.delete(0, 'end')

            # Update the output label
            self.output_label.config(text='Medicine updated successfully!')
            self.populate_list()

    def delete_medicine(self):
            # Get the name from the entry
            name = self.name_entry.get()

            # Delete the medicine
            self.pharmacy.delete_medicine(name)

            # Clear the entries
            self.name_entry.delete(0, 'end')
            self.price_entry.delete(0, 'end')
            self.quantity_entry.delete(0, 'end')
            self.populate_list()

    def populate_list(self):
        # Clear the listbox
        self.medicine_list.delete(0, tk.END)

        # Add each medicine record to the listbox
        for name, medicine in self.pharmacy.medicines.items():
            price = medicine['price']
            quantity = medicine['quantity']
            record = f'{name}  ${price}  x{quantity}'
            self.medicine_list.insert(tk.END, record)

