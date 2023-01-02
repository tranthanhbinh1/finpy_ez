import csv
from gui import PharmacyGUI
import tkinter as tk

class Pharmacy:
    def __init__(self):
        self.medicines = {}
        self.filename = 'medicines.csv'

        # Load the medicine records from the file
        self.load_medicines()

    def create_medicine(self, name, price, quantity, manu_date, exp_date, supp):
        self.medicines[name] = {'price': price, 'quantity': quantity, 'manufacture date': manu_date, 'expiry date': exp_date, 'supplier': supp}
        self.save_medicines() 

    def read_medicine(self, name): # search
        if name in self.medicines:
            medicine = self.medicines[name]
            price = medicine['price']
            quantity = medicine['quantity']
            manu_date = medicine['manu_date']
            exp_date = medicine['exp_date']
            supp = medicine['supp']
            return (name, price, quantity, manu_date, exp_date, supp)
        else:
            return None

    def update_medicine(self, name, price, quantity, manu_date, exp_date, supp):
        if name in self.medicines:
            self.medicines[name] = {'price': price, 'quantity': quantity, 'manufacture date': manu_date, 'expiry date': exp_date, 'supplier': supp}
            self.save_medicines()
            return True
        else:
            return False

    def delete_medicine(self, name):
        if name in self.medicines:
            del self.medicines[name]
            self.save_medicines()
            return True
        else:
            return False


    def load_medicines(self):
        with open(self.filename, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                try:
                    name, price, quantity = row
                except ValueError:
                    # Skip rows with fewer than 3 values
                    continue
                self.medicines[name] = {'price': price, 'quantity': quantity}

    def save_medicines(self):
        with open(self.filename, 'w') as f:
            writer = csv.writer(f)
            for name, medicine in self.medicines.items():
                price = medicine['price']
                quantity = medicine['quantity']
                manu_date = medicine['manu_date']
                exp_date = medicine['exp_date']
                supp = medicine['supp']
                writer.writerow([name, price, quantity, manu_date, exp_date, supp])

    def show_all_medicines(self):
        # Print the header
        print('Name\tPrice\tQuantity')
        print('------------------------')

        # Print each medicine record
        for name, medicine in self.medicines.items():
            price = medicine['price']
            quantity = medicine['quantity']
            manu_date = medicine['manu_date']
            exp_date = medicine['exp_date']
            supp = medicine['supp']
            print(f'{name}\t{price}\t{quantity}\t{manu_date}\t{exp_date}\t{supp}')




