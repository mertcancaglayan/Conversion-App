import tkinter as tk
from tkinter.font import *
from tkinter import ttk
from tkinter import *

#lenght options

options = [
    "centimeter",
    "inch",
    "meter",
    "feet",
    "kilometer",
    "mile",
    "millimeter",
    "yard"
]

#lenght convert values
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



#root window
root = tk.Tk()

#setting window title and size
root.title("Conversion App")
canvas = Canvas(root, width=300,height=200)
canvas.pack()

root.resizable(width=False, height=False)

def convert():
    # get the input value and unit
    value = float(input_field.get())
    unit = choosingcombo.get()
    

    # convert the value to meters (the base unit)
    if unit == "centimeter":
        meters = value / 100
    elif unit == "inch":
        meters = inches_to_cm(value) / 100
    elif unit == "meter":
        meters = value
    elif unit == "feet":
        meters = feet_to_meter(value)
    elif unit == "kilometer":
        meters = value * 1000
    elif unit == "mile":
        meters = miles_to_km(value) * 1000
    elif unit == "millimeter":
        meters = mm_to_cm(value) / 100
    elif unit == "yard":
        meters = yard_to_meter(value) / 100
    
    # convert the meters to the output unit
    output_unit = convertedcombo.get()
    output_value = 0.0
    if output_unit == "centimeter":
        output_value = meters * 100
    elif output_unit == "inch":
        output_value = cm_to_inches(meters * 100)
    elif output_unit == "meter":
        output_value = meters
    elif output_unit == "feet":
        output_value = meter_to_feet(meters)
    elif output_unit == "kilometer":
        output_value = meters / 1000
    elif output_unit == "mile":
        output_value = km_to_miles(meters / 1000)
    elif output_unit == "millimeter":
        output_value = meters * 1000
    elif output_unit == "yard":
        output_value = meters * 1.09361
    
    # update the output entry widget
    output_field.delete(0, tk.END)
    output_field.insert(0, str(output_value))


#create label
label = Label(root, text="Please choose", font=("Helvetica",15), fg= "blue", anchor="n")
canvas.create_window(150,25,window=label)

#create combobox for option
choosingcombo = ttk.Combobox(root,value=options,width=10)
canvas.create_window(250,80,window=choosingcombo)

convertedcombo = ttk.Combobox(root,value=options,width=10)
canvas.create_window(250,110,window=convertedcombo)

#create entry
input_label = tk.Label(root, text="Enter a value:")
input_field = Entry(root,width=10)
canvas.create_window(150,80,window=input_field)
canvas.create_window(80,80,window=input_label)

#create output
output_label = tk.Label(root, text="Converted value:")
output_field = Entry(root,width=10)
canvas.create_window(150,110,window=output_field)
canvas.create_window(70,110,window=output_label)

#create button for func to work
button = tk.Button(root,text="Convert",command=convert)
button.pack()

#run
root.mainloop()
