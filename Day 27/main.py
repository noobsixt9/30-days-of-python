from tkinter import *

def miles_to_km():
    miles = int(input.get())
    km = round(miles * 1.609)
    kilometer_label.config(text=f"{km}")

window = Tk()
window.title("Mile to KM converter")
window.config(padx=10, pady=10)


input = Entry(width=5)
input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_to_label = Label(text="is equals to")
is_equal_to_label.grid(row=1, column=0)

kilometer_label = Label(text="0")
kilometer_label.grid(row=1, column=1)

km_label = Label(text="KM")
km_label.grid(row=1, column=2)

calculate_button = Button(text="calculate", command=miles_to_km)
calculate_button.grid(row=2, column=1)


window.mainloop()
