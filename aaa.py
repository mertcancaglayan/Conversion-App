import tkinter as tk

def cm_to_inches(cm):
    return cm * 0.393701

def inches_to_cm(inches):
    return inches * 2.54

def meter_to_feet(meter):
    return meter * 3.28084

def feet_to_meter(feet):
    return feet * 0.3048

def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles * 1.60934

def mm_to_cm(mm):
    return mm * 0.1

def yard_to_meter(yard):
    return yard * 0.9144

# create the main window
root = tk.Tk()
root.title("Unit Converter")

# create the input and output widgets
input_label = tk.Label(root, text="Enter a value:")
input_entry = tk.Entry(root, width=20)
output_label = tk.Label(root, text="Converted value:")
output_entry = tk.Entry(root, width=20)

# create the conversion function
def convert():
    # get the input value and unit
    value = float(input_entry.get())
    unit = unit_var.get()
    
    # convert the value to meters (the base unit)
    if unit == "cm":
        meters = value / 100
    elif unit == "inches":
        meters = inches_to_cm(value) / 100
    elif unit == "m":
        meters = value
    elif unit == "ft":
        meters = feet_to_meter(value)
    elif unit == "km":
        meters = value * 1000
    elif unit == "miles":
        meters = miles_to_km(value) * 1000
    elif unit == "mm":
        meters = mm_to_cm(value) / 100
    elif unit == "yard":
        meters = yard_to_meter(value) / 100
    
    # convert the meters to the output unit
    output_unit = output_var.get()
    if output_unit == "cm":
        output_value = meters * 100
    elif output_unit == "inches":
        output_value = cm_to_inches(meters * 100)
    elif output_unit == "m":
        output_value = meters
    elif output_unit == "ft":
        output_value = meter_to_feet(meters)
    elif output_unit == "km":
        output_value = meters / 1000
    elif output_unit == "miles":
        output_value = km_to_miles(meters / 1000)
    elif output_unit == "mm":
        output_value = meters * 1000
    elif output_unit == "yard":
        output_value = meters * 1.09361
    
    # update the output entry widget
    output_entry.delete(0, tk.END)
    output_entry.insert(0, str(output_value))

# create the unit selection widgets
units = ["cm", "inches", "m", "ft", "km", "miles", "mm", "yard"]
unit_var = tk.StringVar(value=units[0])
unit_menu = tk.OptionMenu(root, unit_var, *units)
unit_menu.config(width=8)

output_var = tk.StringVar(value=units[2])
output_menu = tk.OptionMenu(root, output_var, *units)
output_menu.config(width=8)

# create the conversion button
convert_button = tk.Button(root, text="Convert", command=convert)

# grid the widgets
input_label.grid(row=0, column=0, padx=5, pady=5)
input_entry.grid(row=0, column=1, padx=5, pady=5)
unit_menu.grid(row=0, column=2, padx=5, pady=5)
output_label.grid(row=1, column=0, padx=5, pady=5)
output_entry.grid(row=1, column=1, padx=5, pady=5)
output_menu.grid(row=1, column=2, padx=5, pady=5)
convert_button.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
