# Телефонный справочник

import tkinter as tk
import phonebook as pb

root = tk.Tk()
root.title('phonebook')
root.geometry('300x130')

def show_enter_window(event):
    enter_window = tk.Toplevel(root, padx=10, pady=10)
    tk.Label(enter_window, text='First name').pack()
    first_name_entry = tk.Entry(enter_window)
    first_name_entry.pack()
    tk.Label(enter_window, text='Second name').pack()
    second_name_entry = tk.Entry(enter_window)
    second_name_entry.pack()
    tk.Label(enter_window, text='Phone').pack()
    phone_entry = tk.Entry(enter_window)
    phone_entry.pack()
    tk.Label(enter_window, text='Description').pack()
    description_entry = tk.Entry(enter_window)
    description_entry.pack()
    save_button = tk.Button(enter_window, text='Save')
    save_button.pack()

    def save(e):
        pb.save_contact(
            first_name_entry.get(),
            second_name_entry.get(),
            phone_entry.get(),
            description_entry.get(),
        )
        enter_window.destroy()

    save_button.bind('<Button-1>', save)

def show_list_window(event):
    list_window = tk.Toplevel(root, padx=10, pady=10)
    contacts = pb.get_contacts()
    if contacts:
        for contact in contacts:
            tk.Label(list_window, text=' | '.join(contact)).pack()
    else:
        tk.Label(list_window, text='No contacts', fg='red').pack()

add_button = tk.Button(root, text='Add contact')
add_button.bind('<Button-1>', show_enter_window)
add_button.pack(fill='x', padx=10, pady=10)
list_button = tk.Button(root, text='List contacts')
list_button.bind('<Button-1>', show_list_window)
list_button.pack(fill='x',  padx=10, pady=0)

tk.mainloop()
