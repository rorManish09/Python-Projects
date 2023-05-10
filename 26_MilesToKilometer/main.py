from tkinter import *

def miles_to_km():
    miles = float(mile_input.get())
    km = miles*1.609
    kilometer_result_label.config(text=f"{km}")


window = Tk()

window.title("Miles to kilometer Converter")

window.config(padx=20,pady=20)

mile_input = Entry(width=7)
mile_input.grid(column=1,row=2)

miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)

is_equals_Label = Label(text= "is equals to ")
is_equals_Label.grid(column=0,row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1,row=1)

kilometer_label = Label(text="km")
kilometer_label.grid(column = 2, row=2)

calculate_button = Button(text = "Calculate" , command=miles_to_km)
calculate_button.grid(column=1,row=2)

window.mainloop()