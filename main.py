from app import Pharmacy
from gui import PharmacyGUI


if __name__ == '__main__':
    pharmacy = Pharmacy()
    gui=PharmacyGUI(pharmacy)
    gui.root.mainloop()