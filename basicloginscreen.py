import tkinter as tk
from tkinter import messagebox

from demo_access import normalise_display_name


def continue_demo() -> None:
    display_name = normalise_display_name(display_name_entry.get())
    if display_name is None:
        messagebox.showerror("Name required", "Enter a display name to continue.")
        return
    messagebox.showinfo("Demo access", f"Welcome {display_name}! This is an educational GUI demo.")


def create_demo_access_page() -> None:
    global display_name_entry

    window = tk.Tk()
    window.title("Demo Access Screen")

    tk.Label(window, text="Educational GUI demo — no authentication is performed.").grid(
        row=0, column=0, columnspan=2, padx=10, pady=(10, 4)
    )
    tk.Label(window, text="Display name").grid(row=1, column=0, padx=10, pady=10)
    display_name_entry = tk.Entry(window)
    display_name_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Button(window, text="Continue to demo", command=continue_demo).grid(
        row=2, columnspan=2, pady=10
    )
    window.mainloop()


if __name__ == "__main__":
    create_demo_access_page()
