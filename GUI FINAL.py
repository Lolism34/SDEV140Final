# Date: 2024-03-02 REV 2024-9-3
# Name: Sean Kennedy
# IDE: Visual Studio Code

# This is a GUI program to allow the input of product into a data base
# Allow the input of custom name and SKU number
# The database will store these values in an array for easy access later on.

 
import tkinter as tk
from tkinter import PhotoImage
import tkinter.messagebox as messagebox
import sys

class SampleApp(tk.Tk):
# A simple GUI application with multiple windows for product input, SKU search, and main window.
    def __init__(self):
        super().__init__()
        self.configure(borderwidth=2, relief="solid")
        self.configure(bg="red")
        self.banner = PhotoImage(file="conke1.gif")
        tk.Label(self, image=self.banner).pack()
        self.current_window = None
        self.window_list = [self.product_input, self.search_sku, self.main_window]
        self.current_window_index = 1
        self.geometry("400x600")
        self.main_window()
        self.product_data = []

# Destroy the current window and create the main window with options to go to product input and SKU search windows.
    def main_window(self):
        if self.current_window:
            self.current_window.destroy()
        self.current_window = tk.Frame(self)
        self.current_window.pack()
        tk.Label(self.current_window, text="Welcome to the Inventory Management system").pack()
        tk.Button(self.current_window, text="Product Input", command=self.product_input).pack(pady=20)
        tk.Button(self.current_window, text="Search SKU", command=self.search_sku).pack(pady=20)
        tk.Button(self.current_window, text="Close", command=self.close_app).pack(pady=20)

        self.image = PhotoImage(file="Pour.gif")  # replace with your image file
        tk.Label(self.current_window, image=self.image).pack(side="bottom")

# Destroy the current window and create the product input window with options to save, continue inputting SKU, and go back to the previous window.
    def product_input(self):
        if self.current_window:
            self.current_window.destroy()
        self.current_window = tk.Frame(self)
        self.current_window.pack()
        tk.Label(self.current_window, text="Please Enter the Name and the desired SKU  of the Product.").pack()
        tk.Label(self.current_window, text="Item Name:").pack()
        self.item_name = tk.StringVar()
        tk.Entry(self.current_window, textvariable=self.item_name).pack()
        tk.Label(self.current_window, text="SKU (6 digits):").pack()
        self.sku = tk.StringVar()
        tk.Entry(self.current_window, textvariable=self.sku).pack()
        
        tk.Button(self.current_window, text="Continue Inputting SKU", command=self.continue_inputting_sku).pack()
        tk.Label(self.current_window, text="Last 10 Entered Data Points:").pack()
        self.product_listbox = tk.Listbox(self.current_window, height=10)
        self.product_listbox.pack()
        for data in self.product_data[-10:]:
            self.product_listbox.insert(tk.END, f"{data[0]} ({data[1]})")
        tk.Button(self.current_window, text="Back", command=self.previous_window).pack()
        tk.Button(self.current_window, text="Save", command=self.save_and_return).pack()
# Save the entered item name and SKU to a text file and go back to the previous window.

    def save_and_return(self):
        item_name = self.item_name.get()
        sku = self.sku.get()
        self.product_data.append((item_name, sku))
        with open("products.txt", "a") as f:
            f.write(f"{item_name},{sku}\n")
        self.item_name.set("")
        self.sku.set("")

# Save the entered item name and SKU to the product data list and clear the entry fields for item name and SKU.

    def continue_inputting_sku(self):
        item_name = self.item_name.get()
        sku = self.sku.get()
        if not item_name or not sku:
            messagebox.showerror("Error", "Name and SKU fields cannot be blank.")
        if len(sku) != 6:
            messagebox.showerror("Error", "SKU must be 6 digits long.")
            return
        self.product_data.append((item_name, sku))
        self.item_name.set("")
        self.sku.set("")
        self.product_listbox.insert(tk.END, f"{item_name} ({sku})")

# Allows the user to search inputted data
    def search_sku(self):
        if self.current_window:
            self.current_window.destroy()
        self.current_window = tk.Frame(self)
        self.current_window.pack()
        tk.Label(self.current_window, text="Search SKU:").pack()
        self.search_sku_entry = tk.StringVar()
        tk.Entry(self.current_window, textvariable=self.search_sku_entry).pack()
        tk.Button(self.current_window, text="Search", command=self.search_sku_button).pack()
        self.results = tk.Listbox(self.current_window, height=10)
        self.results.pack()
        tk.Button(self.current_window, text="Back", command=self.previous_window).pack()
        self.search_sku_button()

# Search Button 
    def search_sku_button(self):
        sku = self.search_sku_entry.get()
        self.results.delete(0, tk.END)
        found = False
        for data in self.product_data:
            if sku in data[1]:
                self.results.insert(tk.END, f"{data[0]} ({data[1]})")
                found = True
        if not found:
            self.results.insert(tk.END, "No results found.")

    def next_window(self):
        self.current_window_index += 1
        if self.current_window_index >= len(self.window_list):
            self.current_window_index = 0
        self.window_list[self.current_window_index]()

    def previous_window(self):
        self.current_window_index -= 1
        if self.current_window_index < 0:
            self.current_window_index = len(self.window_list) - 1
        self.window_list[self.current_window_index]()

    def close_app(self): #Exits Program 
        self.destroy()
        sys.exit()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()