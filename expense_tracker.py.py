import tkinter as tk
from tkinter import messagebox

expenses = []

def add_expense():
    date = entry_date.get()
    category = entry_category.get()
    description = entry_description.get()
    try:
        amount = float(entry_amount.get())
        expenses.append({"date": date, "category": category, "description": description, "amount": amount})
        entry_date.delete(0, tk.END)
        entry_category.delete(0, tk.END)
        entry_description.delete(0, tk.END)
        entry_amount.delete(0, tk.END)
        messagebox.showinfo("Success", "Expense added successfully!")
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number")

def view_expenses():
    display_text.delete(1.0, tk.END)
    if not expenses:
        display_text.insert(tk.END, "No expenses recorded yet.\n")
    else:
        for exp in expenses:
            display_text.insert(tk.END, f"Date: {exp['date']} | Category: {exp['category']} | Description: {exp['description']} | Amount: {exp['amount']} tk\n")

def view_total():
    total = sum(exp['amount'] for exp in expenses)
    messagebox.showinfo("Total Spending", f"Your total spending is: {total} tk")

root = tk.Tk()
root.title("Expense Tracker")

tk.Label(root, text="Date (dd-mm-yy):").grid(row=0, column=0, padx=5, pady=5)
entry_date = tk.Entry(root)
entry_date.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Category:").grid(row=1, column=0, padx=5, pady=5)
entry_category = tk.Entry(root)
entry_category.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Description:").grid(row=2, column=0, padx=5, pady=5)
entry_description = tk.Entry(root)
entry_description.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Amount:").grid(row=3, column=0, padx=5, pady=5)
entry_amount = tk.Entry(root)
entry_amount.grid(row=3, column=1, padx=5, pady=5)

tk.Button(root, text="Add Expense", command=add_expense).grid(row=4, column=0, columnspan=2, pady=5)
tk.Button(root, text="View All Expenses", command=view_expenses).grid(row=5, column=0, columnspan=2, pady=5)
tk.Button(root, text="View Total Spending", command=view_total).grid(row=6, column=0, columnspan=2, pady=5)

display_text = tk.Text(root, height=10, width=60)
display_text.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()