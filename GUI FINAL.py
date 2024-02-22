import tkinter as tk

class SampleApp(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.current_window = None
        self.window_list = [self.product_input, self.search_sku, self.main_window]
        self.current_window_index = 1
        self.geometry("600x600")
        self.main_window()
        self.product_data = []

    def main_window(self):
        if self.current_window:
            self.current_window.destroy()
        self.current_window = tk.Frame(self)
        self.current_window.pack()
        tk.Label(self.current_window, text="Main Window").pack()
        tk.Button(self.current_window, text="Product Input", command=self.product_input).pack()
        tk.Button(self.current_window, text="Search SKU", command=self.search_sku).pack()

    def product_input(self):
        if self.current_window:
            self.current_window.destroy()
        self.current_window = tk.Frame(self)
        self.current_window.pack()
        tk.Label(self.current_window, text="Item Name:").pack()
        self.item_name = tk.StringVar()
        tk.Entry(self.current_window, textvariable=self.item_name).pack()
        tk.Label(self.current_window, text="SKU (6 digits):").pack()
        self.sku = tk.StringVar()
        tk.Entry(self.current_window, textvariable=self.sku).pack()
        tk.Button(self.current_window, text="Save", command=self.save_and_return).pack()
        tk.Button(self.current_window, text="Continue Inputting SKU", command=self.continue_inputting_sku).pack()
        tk.Label(self.current_window, text="Last 10 Entered Data Points:").pack()
        self.product_listbox = tk.Listbox(self.current_window, height=10)
        self.product_listbox.pack()
        for data in self.product_data[-10:]:
            self.product_listbox.insert(tk.END, f"{data[0]} ({data[1]})")
        tk.Button(self.current_window, text="Back", command=self.previous_window).pack()

    def save_and_return(self):
        item_name = self.item_name.get()
        sku = self.sku.get()
        if len(sku) != 6:
            print("SKU must be 6 digits long.")
            return
        self.product_data.append((item_name, sku))
        with open("products.txt", "a") as f:
            f.write(f"{item_name},{sku}\n")
        self.item_name.set("")
        self.sku.set("")

    def continue_inputting_sku(self):
        item_name = self.item_name.get()
        sku = self.sku.get()
        if len(sku) != 6:
            print("SKU must be 6 digits long.")
            return
        self.product_data.append((item_name, sku))
        self.item_name.set("")
        self.sku.set("")
        self.product_listbox.insert(tk.END, f"{item_name} ({sku})")

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

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()