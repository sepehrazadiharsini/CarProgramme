"""Apps R Us, Car Sales Programme
Programming Assignment
Sepehr Azadi-Harsini"""

#Import necessary modules. By doing so we'll be able to create a GUI and display message boxes.
import tkinter as tk
from tkinter import messagebox

"""Define the main function to calculate the amount due for the vehicle purchase.
 By using the "try" and "except" method, we're able to run this block of code by keeping the potential errors in mind
 and using "except" to handle them by showing an wrror message.
"""
def calculate_amount_due():
    try:
        #Get user input from entry fields and check buttons.
        #Use get() to retrieve the current value of tkinter variables associated with check buttons.
        basic_price = float(entry_basic_price.get())
        trade_in_allowance = float(entry_trade_in_allowance.get() or 0)

        # Check for negative values
        if basic_price < 0 or trade_in_allowance < 0:
            raise ValueError("Negative values not allowed")

        stereo_system = var_stereo_system.get()
        leather_interior = var_leather_interior.get()
        gps = var_gps.get()
        finish_option = var_finish_option.get()

        #Calculate accessory and finish prices
        accessory_price = 0
        if stereo_system:
            accessory_price += 30.50
        if leather_interior:
            accessory_price += 530.99
        if gps:
            accessory_price += 301.90

        #Define a dictionary finish_prices containing prices for different finish options.
        #Retrieve the price of the selected finish option from the dictionary.
        finish_prices = {"Standard": 0, "Modified": 370.50, "Customized": 1257.99}
        finish_price = finish_prices.get(finish_option, 0)

        #Calculate subtotal, sales tax, and amount due. Tax rate is 6%
        subtotal = basic_price + accessory_price + finish_price
        sales_tax_rate = 0.06
        sales_tax = subtotal * sales_tax_rate
        amount_due = subtotal + sales_tax - trade_in_allowance

        #Display results with appropriate format and label texts.
        label_subtotal.config(text=f"Subtotal: ${subtotal:.2f}")
        label_sales_tax.config(text=f"Sales Tax: ${sales_tax:.2f}")
        label_amount_due.config(text=f"Amount Due: ${amount_due:.2f}")

    #Handle the ValueError exception that may occur if the user enters non-numeric values.
    #This is done by using the showerror() method from the messagebox module imported.
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter numeric values.")

"""
Define a function clear_inputs() to clear the input fields and reset the check buttons and radio buttons.
Use the delete() method to clear the contents of the entry fields.
Use the set() method to set the boolean variables associated with check buttons to False.
Use the set() method to clear the selected option for the finish option radio buttons.
"""
def clear_inputs():
    entry_basic_price.delete(0, tk.END)
    entry_trade_in_allowance.delete(0, tk.END)
    var_stereo_system.set(False)
    var_leather_interior.set(False)
    var_gps.set(False)
    var_finish_option.set("")


#Define a function exit_program() to close the tkinter window. Use the destroy() method to close the programme.
def exit_program():
    root.destroy()


"""
Define a function reset_values() to reset the label texts and clear the input fields and selection options.
Use the config() method to clear the text displayed in the labels and 
call the clear_inputs() function to clear the input fields and selection options.
"""
def reset_values():
    label_subtotal.config(text="")
    label_sales_tax.config(text="")
    label_amount_due.config(text="")
    clear_inputs()


#Create window, GUI
root = tk.Tk()
root.title("Vehicle Purchase Calculator")

#Create input fields and placing them in the GUI window.
label_basic_price = tk.Label(root, text="Basic Price:")
label_basic_price.grid(row=0, column=0)
entry_basic_price = tk.Entry(root)
entry_basic_price.grid(row=0, column=1)

label_trade_in_allowance = tk.Label(root, text="Trade-In Allowance:")
label_trade_in_allowance.grid(row=1, column=0)
entry_trade_in_allowance = tk.Entry(root)
entry_trade_in_allowance.grid(row=1, column=1)

#Create Accessory Checkboxes
var_stereo_system = tk.BooleanVar()
check_stereo_system = tk.Checkbutton(root, text="Stereo System", variable=var_stereo_system)
check_stereo_system.grid(row=2, column=0, sticky="w")

var_leather_interior = tk.BooleanVar()
check_leather_interior = tk.Checkbutton(root, text="Leather Interior", variable=var_leather_interior)
check_leather_interior.grid(row=3, column=0, sticky="w")

var_gps = tk.BooleanVar()
check_gps = tk.Checkbutton(root, text="GPS", variable=var_gps)
check_gps.grid(row=4, column=0, sticky="w")

#Create radio buttons for finish options
var_finish_option = tk.StringVar()
label_finish_options = tk.Label(root, text="Finish Options:")
label_finish_options.grid(row=5, column=0, sticky="w")
radio_standard = tk.Radiobutton(root, text="Standard", variable=var_finish_option, value="Standard")
radio_standard.grid(row=6, column=0, sticky="w")
radio_modified = tk.Radiobutton(root, text="Modified", variable=var_finish_option, value="Modified")
radio_modified.grid(row=7, column=0, sticky="w")
radio_customized = tk.Radiobutton(root, text="Customized", variable=var_finish_option, value="Customized")
radio_customized.grid(row=8, column=0, sticky="w")

#Create buttons for Calculation, Clear, Exit and Reset
button_calculate = tk.Button(root, text="Calculate", command=calculate_amount_due)
button_calculate.grid(row=9, column=0)

button_clear = tk.Button(root, text="Clear", command=clear_inputs)
button_clear.grid(row=9, column=1)

button_exit = tk.Button(root, text="Exit", command=exit_program)
button_exit.grid(row=9, column=2)

button_reset = tk.Button(root, text="Reset", command=reset_values)
button_reset.grid(row=9, column=3)

#Create labels for displaying results and placing them at the bottom of the window.
label_subtotal = tk.Label(root, text="")
label_subtotal.grid(row=10, column=0, columnspan=2)
label_sales_tax = tk.Label(root, text="")
label_sales_tax.grid(row=11, column=0, columnspan=2)
label_amount_due = tk.Label(root, text="")
label_amount_due.grid(row=12, column=0, columnspan=2)

#Run the programme by starting the tkinter event loop to display the GUI and recieve user inputs.
root.mainloop()
