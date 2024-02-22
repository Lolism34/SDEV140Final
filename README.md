This Python application utilizes the tkinter library to create a graphical user interface (GUI) for managing product data including inputting product information, searching for products by SKU, and displaying search results.
Prerequisites

    Python 3.x installed on your system.
    tkinter library should be available. It is typically included with Python installations.

Usage

    Clone or download the repository containing the GUI FINAL.py file.
    Run the GUI FINAL.py file using Python.

    python GUI FINAL.py

    The application window will appear with the main window initially displayed.

Features

    Main Window: Provides options to navigate to product input or search SKU functionalities.
    Product Input Window: Allows users to input item name and SKU (6 digits). Users can save the input data, continue inputting SKU for the same item, view the last 10 entered data points, and navigate back to the previous window.
    Search SKU Window: Enables users to search for products by SKU. Results are displayed in a listbox. If no results are found, an appropriate message is displayed.

Functionality Highlights

    Data Persistence: Entered product data is stored in a file named products.txt.
    Input Validation: Checks the length of the SKU to ensure it is 6 digits long.
    Dynamic Display: The application dynamically updates the last 10 entered data points and search results.

File Structure

    GUI FINAL.py: Contains the main code for the tkinter application.
    products.txt: Stores the product data entered by the user.

Important Notes

    Make sure to handle file permissions appropriately if running the application in a restricted environment.
    Ensure that the tkinter library is installed and available in your Python environment.

Contributors

    This application was developed by Sean Kennedy .
