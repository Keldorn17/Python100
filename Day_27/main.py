import tkinter


def calculate(display_label: tkinter.Label, input_entry: tkinter.Entry) -> None:
    miles = float(input_entry.get())
    km = miles * 1.60934
    display_label.config(text=f"{km:.2f}")


def main() -> None:
    window: tkinter.Tk = tkinter.Tk()
    window.title("Mile to Km Converter")
    window.config(padx=20, pady=20)

    texts: list[str] = ["Miles", "is equal to", "Km"]

    input_entry: tkinter.Entry = tkinter.Entry(width=10)
    labels_const: list[tkinter.Label] = [tkinter.Label(text=text) for text in texts]
    display_label: tkinter.Label = tkinter.Label(text=0)
    button: tkinter.Button = tkinter.Button(text="Calculate", command=lambda: calculate(display_label, input_entry))

    input_entry.grid(column=1, row=0)
    labels_const[0].grid(column=2, row=0)
    labels_const[1].grid(column=0, row=1)
    display_label.grid(column=1, row=1)
    labels_const[2].grid(column=2, row=1)
    button.grid(column=1, row=2)

    window.mainloop()


if __name__ == '__main__':
    main()


