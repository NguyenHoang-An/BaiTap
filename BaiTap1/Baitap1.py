import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Exit application function
def _quit():
    win.quit()
    win.destroy()
    exit()

# Xử lý các phép tính 
def cong():
    try:
        a = float(name_entry1.get())
        b = float(name_entry2.get())
        ketqua = a + b 
        label_ketqua.config(text=f"Kết quả : {ketqua}")
    except ValueError:
        messagebox.showerror ("Input Error", "Please enter valid number.")
        
def tru():
    try:
        a = float(name_entry1.get())
        b = float(name_entry2.get())
        ketqua = a - b 
        label_ketqua.config(text=f"Kết quả : {ketqua}")
    except ValueError:
        messagebox.showerror("Input Error", "please enter valid number.")

def nhan():
    try:
        a = float(name_entry1.get())
        b = float(name_entry2.get())
        ketqua = a * b 
        label_ketqua.config(text=f"Kết quả : {ketqua}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

def chia():
    try:
        a = float(name_entry1.get())
        b = float(name_entry2.get())
        if b == 0:
            messagebox.showerror("Math Error", "Cannot divide by zero")
        else:
            ketqua = a / b
            label_ketqua.config(text=f"Kết quả : {ketqua}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

def chia_lay_du():
    try:
        a = float(name_entry1.get())
        b = float(name_entry2.get())
        if b == 0:
            messagebox.showerror("Math Error", "Cannot divide by zero")
        else:
            ketqua = a % b
            label_ketqua.config(text=f"Kết quả : {ketqua}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")
        
# Create main window
win = tk.Tk()
win.title("App Tính Toán")

# Create menu bar
menu_bar = tk.Menu(win)
win.config(menu=menu_bar)

# Add file menu without separators
file_menu = tk.Menu(menu_bar, takefocus=0, tearoff=0)  # Add 'tearoff=0' to prevent the dashed line
menu_bar.add_cascade(label="File", menu=file_menu, underline=-1)

# Add "Exit" command to file menu
file_menu.add_command(label="Exit", command=_quit)

# Create Label and entry widgets for number input
a = ttk.Label(text="Nhập số a").grid(column=0, row=0, sticky='W')
name_entry1 = ttk.Entry(win, width=20)
name_entry1.grid(column=1, row=0, padx=10, pady=10)

b = ttk.Label(text="Nhập số b").grid(column=0, row=1, sticky='W')
name_entry2 = ttk.Entry(win, width=20)
name_entry2.grid(column=1, row=1, padx=10, pady=10)

# Create buttons and align them with proper padding
btn_frame = ttk.Frame(win)  # Create a frame to hold buttons
btn_frame.grid(column=0, row=2, columnspan=2, pady=10)

btn_cong = tk.Button(btn_frame, text="+", command=cong, width=5)
btn_tru = tk.Button(btn_frame, text="-", command=tru, width=5)
btn_nhan = tk.Button(btn_frame, text="*", command=nhan, width=5)
btn_chia = tk.Button(btn_frame, text="/", command=chia, width=5)
btn_chia_du = tk.Button(btn_frame, text="%", command=chia_lay_du, width=5)

# Use grid inside the frame to arrange buttons in a row
btn_cong.grid(column=0, row=0, padx=5)
btn_tru.grid(column=1, row=0, padx=5)
btn_nhan.grid(column=2, row=0, padx=5)
btn_chia.grid(column=3, row=0, padx=5)
btn_chia_du.grid(column=4, row=0, padx=5)  # Add button for modulus

# Create label for displaying result
label_ketqua = ttk.Label(win, text="Kết quả :", font=('Arial', 14))
label_ketqua.grid(column=0, row=3, columnspan=2, pady=10)

# Start the GUI
win.mainloop()
