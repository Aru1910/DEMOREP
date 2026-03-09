import tkinter as tk
                                                                                  # 4L=400000 12XT=1200000 12X1=120001  50L = 5000000
class taxCalculator:
    def __init__(self): 
        self.window = tk.Tk()
        self.window.title("Tax Flow - Group 24")
        self.window.geometry("450x550")
        self.window.resizable(False, False)

        # Income Field
        tk.Label(self.window, text="Enter your income:").grid(row=0, column=0, padx=20, pady=20)
        self.taxableincome_field = tk.Entry(self.window, width=30)
        self.taxableincome_field.grid(row=0, column=1, padx=20, pady=20)

        # Radiobuttons for Salaried
        self.is_salaried = tk.StringVar(value="n") 
        tk.Radiobutton(self.window, text="Yes (Salaried)", variable=self.is_salaried, value="y").grid(row=1, column=0)
        tk.Radiobutton(self.window, text="No (Other)", variable=self.is_salaried, value="n").grid(row=1, column=1)

        # Tax Result Field
        tk.Label(self.window, text="Final Tax (Incl. Cess):").grid(row=5, column=0, padx=20, pady=20)
        self.tax_field = tk.Entry(self.window, width=30)
        self.tax_field.grid(row=5, column=1, padx=20, pady=20)

        button = tk.Button(self.window, text="Calculate Tax", command=self.calculate_tax)
        button.grid(row=3, column=0, columnspan=2, pady=20)

    def calculate_tax(self):
        income = float(self.taxableincome_field.get())
        
        # Apply 75k deduction if 'y' is selected
        if self.is_salaried.get() == "y":
            salary = income - 75000
        else:
            salary = income
        
        # Base Slab Logic
        tax = 0
        if salary <= 400000: tax = 0
        elif salary <= 800000: tax = (salary - 400000) * 0.05
        elif salary <= 1200000: tax = 20000 + (salary - 800000) * 0.10
        elif salary <= 1600000: tax = 60000 + (salary - 1200000) * 0.15
        elif salary <= 2000000: tax = 120000 + (salary - 1600000) * 0.20
        elif salary <= 2400000: tax = 200000 + (salary - 2000000) * 0.25
        else: tax = 300000 + (salary - 2400000) * 0.30

        # Rebate & Surcharge
        if salary <= 1200000: tax = 0
        
        surcharge = 0
        if salary > 5000000:
            if salary <= 10000000: surcharge = tax * 0.10
            elif salary <= 20000000: surcharge = tax * 0.15
            else: surcharge = tax * 0.25

        # --- SYNCED: Added 4% Cess ---
        total_before_cess = tax + surcharge
        cess = total_before_cess * 0.04
        final_total = total_before_cess + cess
        
        # Display Result
        self.tax_field.delete(0, tk.END)
        self.tax_field.insert(0, round(final_total, 2))

    def run(self):  
        self.window.mainloop()

if __name__ == '__main__':
    obj = taxCalculator()
    obj.run()