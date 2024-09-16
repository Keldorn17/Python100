import tkinter

window: tkinter.Tk = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label: tkinter.Label = tkinter.Label(text="I Am a Label.", font=("Arial", 24, "bold"))
# my_label.pack()
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# my_label["text"] = "New Text."
# my_label.config(text="New Text.")


# Button
def button_clicked() -> None:
    my_label.config(text=input_entry.get())


button: tkinter.Button = tkinter.Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button: tkinter.Button = tkinter.Button(text="New Button", command=button_clicked)
# button.pack()
new_button.grid(column=2, row=0)

# Entry
input_entry: tkinter.Entry = tkinter.Entry(width=30)
# input_entry.pack()
input_entry.grid(column=3, row=2)

window.mainloop()

# def add(*args) -> int:
#     sum_ = 0
#     for number in args:
#         sum_ += number
#     return sum_
#
#
# print(add(1, 2, 3, 4, 5))
#
#
# def calculate(n, **kwargs):
#     print(kwargs)
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
#
# calculate(2, add=3, multiply=5)


# class Car:
#
#     def __init__(self, **kw):
#         self.make = kw.get("make")
#         self.model = kw.get("model")
#         self.color = kw.get("color")
#         self.seats = kw.get("seats")
#
#
# my_car = Car(make="Nissan", model="GT-R")
# print(my_car.model)
