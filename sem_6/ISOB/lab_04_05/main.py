import tkinter as tk
from tkinter import messagebox, Toplevel
import sqlite3
import requests
from protected_entry import Protected_entry
from bd_config import *

class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        window_width = 400
        window_height = 200
        self.master.geometry(f"{window_width}x{window_height}")
        self.center_window()
        self.username_label = tk.Label(master, text="Username:")
        self.username_label.pack()
        self.username_entry = Protected_entry(master)
        self.username_entry.insert(0, "admin")
        self.username_entry.pack()

        self.password_label = tk.Label(master, text="Password:")
        self.password_label.pack()
        self.password_entry = Protected_entry(master, show="*")
        self.password_entry.insert(0, "111")
        self.password_entry.pack()
        self.login_button = tk.Button(master, text="Login", command=self.validate_login)
        self.login_button.pack()

    def center_window(self):
        window_width = 400
        window_height = 200
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 8
        self.master.geometry(f"{window_width}x{window_height}+{x}+{y}")
        

    def validate_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        
        c.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
        user = c.fetchone()

        if user:
            self.open_main_window(user)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")


    def open_main_window(self, user):
        url = 'https://api.quotable.io/random'
        response = requests.get(url)
        data = response.json()

        if 'content' in data:
            phrase = data['content']

        welcome_window = Toplevel(self.master)
        welcome_window.title("Welcome")
        window_width = 400
        window_height = 200
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        welcome_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        welcome_label = tk.Label(welcome_window, text=f"Welcome, {user[1]}!\n{phrase}", wraplength=300)
        welcome_label.pack(padx=20, pady=10)

         # the principle of minimizing privileges
        if user[3] == 'Admin':
            add_user_button = tk.Button(welcome_window, text="Add User", command=self.add_user)
            add_user_button.pack()

            show_all_users_button = tk.Button(welcome_window, text="Show All Users", command=self.show_all_users)

            
            def unlock_button():
                show_all_users_button.config(state=tk.NORMAL)

            def button_click():
                all_users_window = tk.Toplevel(self.master)
                all_users_window.title("All Users")
                window_width = 400
                window_height = 200
                screen_width = self.master.winfo_screenwidth()
                screen_height = self.master.winfo_screenheight()
                x = (screen_width - window_width) // 2
                y = (screen_height - window_height) // 2
                all_users_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

                conn = sqlite3.connect('users.db')
                c = conn.cursor()
                c.execute('SELECT * FROM users')
                users = c.fetchall()
                conn.close()

                header_label = tk.Label(all_users_window, text="ИМЯ | ПАРОЛЬ | РОЛЬ")
                header_label.pack()

                users_listbox = tk.Listbox(all_users_window)
                users_listbox.pack(fill=tk.BOTH, expand=True)

                for user in users:
                    user_info = f"{user[1]} | {user[2]} | {user[3]}"
                    users_listbox.insert(tk.END, user_info)
                    
            # DoS attack (denial of service)    
                show_all_users_button.config(state=tk.DISABLED)
                welcome_window.after(5000, unlock_button)

            show_all_users_button.config(command=button_click)
            show_all_users_button.pack()

    def add_user(self):
        def add_button_click():
            new_username = username_entry.get()
            new_password = password_entry.get()
            new_role = role_entry.get()
            
            if new_role not in ['Admin', 'User']:
                add_user_window.destroy()
                messagebox.showerror("Warning!", "Invalid role")
            else:
                conn = sqlite3.connect('users.db')
                c = conn.cursor()
                c.execute('SELECT * FROM users')
                users = c.fetchall()
                flag = True
                for user in users:
                    #An attack that exploits canonicalization errors
                    if new_username in user:
                        add_user_window.destroy()
                        flag = False
                if(flag):
                    c.execute('INSERT INTO users (username, password, role_id) VALUES (?, ?, ?)', (new_username, new_password, new_role))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "New user has been added successfully!")
                    
                    add_user_window.destroy()
                    
                else:
                    messagebox.showerror('Error', 'User already exists!')

        add_user_window = tk.Toplevel(self.master)
        add_user_window.title("Add User")
       
        window_width = 400
        window_height = 200
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        add_user_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        username_label = tk.Label(add_user_window, text="Username:")
        username_label.pack()

        username_entry = Protected_entry(add_user_window)
        username_entry.pack()

        password_label = tk.Label(add_user_window, text="Password:")
        password_label.pack()

        password_entry = Protected_entry(add_user_window, show="*")
        password_entry.pack()

        role_label = tk.Label(add_user_window, text="Role:")
        role_label.pack()

        role_entry = Protected_entry(add_user_window)
        role_entry.pack()

        add_button = tk.Button(add_user_window, text="Add", command=add_button_click)
        add_button.pack()    
        

   
    def show_all_users(self):
        pass


def main():
    config()
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop()
if __name__ == "__main__":
    main()
