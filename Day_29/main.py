import tkinter
import tkinter.messagebox
import password_generator
import pyperclip


def generate_password(password: tkinter.Entry) -> None:
    password.delete(0, tkinter.END)
    new_password: str = password_generator.generate_password(10, 2, 2)
    password.insert(0, f"{new_password}")
    pyperclip.copy(new_password)


def save_data(website: tkinter.Entry, email: tkinter.Entry, password: tkinter.Entry) -> None:
    if website.get() == "" or email.get() == "" or password.get() == "":
        tkinter.messagebox.showerror(title="Field error", message="Incomplete fields found. All fields must be filled.")
    is_ok = tkinter.messagebox.askokcancel(title=website.get(), message=f"These are the details entered: "
                                                                        f"\nEmail: {email.get()}"
                                                                        f"\nPassword: {password.get()}"
                                                                        f"\nIs it ok to save?")
    if is_ok:
        with open("data.txt", "a") as file:
            file.write(f"{website.get()} | {email.get()} | {password.get()}\n")
            website.delete(0, tkinter.END)
            password.delete(0, tkinter.END)


def main() -> None:
    window: tkinter.Tk = tkinter.Tk()
    window.title("Password Manager")
    window.config(pady=20, padx=20)

    canvas: tkinter.Canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
    image: tkinter.PhotoImage = tkinter.PhotoImage(file="logo.png")
    canvas.create_image(100, 95, image=image)

    label_text: list[str] = ["Website:", "Email/Username:", "Password:"]
    placeholder_label: list[tkinter.Label] = [tkinter.Label(text=text) for text in label_text]
    website_entry: tkinter.Entry = tkinter.Entry(width=50)
    email_entry: tkinter.Entry = tkinter.Entry(width=50)
    password_entry: tkinter.Entry = tkinter.Entry(width=32)
    generate_button: tkinter.Button = tkinter.Button(text="Generate Password",
                                                     command=lambda: generate_password(password_entry))
    add_button: tkinter.Button = tkinter.Button(text="Add", width=43,
                                                command=lambda: save_data(website_entry, email_entry, password_entry))

    canvas.grid(column=1, row=0)
    placeholder_label[0].grid(column=0, row=1)
    placeholder_label[1].grid(column=0, row=2)
    placeholder_label[2].grid(column=0, row=3)
    website_entry.grid(column=1, row=1, columnspan=2)
    email_entry.grid(column=1, row=2, columnspan=2)
    password_entry.grid(column=1, row=3)
    generate_button.grid(column=2, row=3)
    add_button.grid(column=1, row=4, columnspan=2)

    website_entry.focus()
    email_entry.insert(0, "example@gmail.com")

    window.mainloop()


if __name__ == '__main__':
    main()
