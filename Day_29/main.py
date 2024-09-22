import json
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
    website_text = website.get()
    email_text = email.get()
    password_text = password.get()
    new_data = {
        website_text: {
            "email": email_text,
            "password": password_text
        }
    }

    if website_text == "" or email_text == "" or password_text == "":
        tkinter.messagebox.showerror(title="Field error", message="Incomplete fields found. All fields must be filled.")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                # JSON Write: json.dump(), JSON Read: json.load(), JSON Update: json.update()
                # Reading old data
                data: dict = json.load(data_file)
                # Updating old data with new data
                data.update(new_data)
        except (FileNotFoundError, json.JSONDecodeError):
            data: dict = new_data

        with open("data.json", mode="w") as data_file:
            # Saving updated data
            json.dump(data, data_file, indent=4)
            website.delete(0, tkinter.END)
            password.delete(0, tkinter.END)

        website.delete(0, tkinter.END)
        password.delete(0, tkinter.END)


def search(website: tkinter.Entry) -> None:
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            tkinter.messagebox.showinfo(title=f"{website.get()}",
                                        message=f"Email: {data[website.get()]["email"]}"
                                                f"\nPassword: {data[website.get()]["password"]}")
    except (FileNotFoundError, KeyError, json.JSONDecodeError):
        tkinter.messagebox.showerror(title="Data Error", message=f"No data found as '{website.get()}'.")


def main() -> None:
    window: tkinter.Tk = tkinter.Tk()
    window.title("Password Manager")
    window.config(pady=20, padx=20)

    canvas: tkinter.Canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
    image: tkinter.PhotoImage = tkinter.PhotoImage(file="logo.png")
    canvas.create_image(100, 95, image=image)

    label_text: list[str] = ["Website:", "Email/Username:", "Password:"]
    placeholder_label: list[tkinter.Label] = [tkinter.Label(text=text) for text in label_text]
    website_entry: tkinter.Entry = tkinter.Entry(width=32)
    email_entry: tkinter.Entry = tkinter.Entry(width=50)
    password_entry: tkinter.Entry = tkinter.Entry(width=32)
    search_button: tkinter.Button = tkinter.Button(text="Search", highlightthickness=0, width=14,
                                                   command=lambda: search(website_entry))
    generate_button: tkinter.Button = tkinter.Button(text="Generate Password", highlightthickness=0,
                                                     command=lambda: generate_password(password_entry))
    add_button: tkinter.Button = tkinter.Button(text="Add", width=43, highlightthickness=0,
                                                command=lambda: save_data(website_entry, email_entry, password_entry))

    canvas.grid(column=1, row=0)
    placeholder_label[0].grid(column=0, row=1)
    placeholder_label[1].grid(column=0, row=2)
    placeholder_label[2].grid(column=0, row=3)
    website_entry.grid(column=1, row=1)
    email_entry.grid(column=1, row=2, columnspan=2)
    password_entry.grid(column=1, row=3)
    search_button.grid(column=2, row=1)
    generate_button.grid(column=2, row=3)
    add_button.grid(column=1, row=4, columnspan=2)

    website_entry.focus()
    email_entry.insert(0, "example@gmail.com")

    window.mainloop()


if __name__ == '__main__':
    main()
