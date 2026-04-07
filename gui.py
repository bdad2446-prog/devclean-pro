import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from devclean import list_files

# --- GUI Functions ---
def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_label.config(text=folder_path)
        list_box.delete(0, tk.END)

def run_preview():
    folder_path = folder_label.cget("text")
    if not folder_path:
        messagebox.showerror("Error", "Please select a folder first!")
        return

    list_box.delete(0, tk.END)
    run_checkbox_var.set(False)  # Preview only
    def add_to_listbox(text):
        list_box.insert(tk.END, text)

    list_files(folder_path, preview_callback=add_to_listbox, organize=False)

def run_organize():
    folder_path = folder_label.cget("text")
    if not folder_path:
        messagebox.showerror("Error", "Please select a folder first!")
        return

    list_box.delete(0, tk.END)
    run_checkbox_var.set(True)  # Organize mode
    def add_to_listbox(text):
        list_box.insert(tk.END, text)

    list_files(folder_path, preview_callback=add_to_listbox, organize=True)
    messagebox.showinfo("Done", "Files organized successfully!")

# --- Build GUI ---
root = tk.Tk()
root.title("DevClean Pro")
root.configure(bg="#1e1e1e")

style_btn = {
    "bg": "#ff9800",
    "fg": "black",
    "font": ("Arial", 10, "bold"),
    "padx": 10,
    "pady": 5
}

title = tk.Label(root, text="DevClean Pro", font=("Arial", 18, "bold"), bg="#1e1e1e", fg="white")
title.pack(pady=10)
root.geometry("700x500")

# Folder selection
select_btn = tk.Button(root, text="Select Folder", command=select_folder, **style_btn)
select_btn.pack(pady=10)

folder_label = tk.Label(root, text="No folder selected")
folder_label.pack(pady=5)

# Buttons
frame_btns = tk.Frame(root)
frame_btns.pack(pady=10)

preview_btn = tk.Button(frame_btns, text="Preview Files", command=run_preview)
preview_btn.grid(row=0, column=0, padx=10)

organize_btn = tk.Button(frame_btns, text="Organize Files", command=run_organize)
organize_btn.grid(row=0, column=1, padx=10)

# Scrollable Listbox
frame_listbox = tk.Frame(root)
frame_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame_listbox)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

list_box = tk.Listbox(frame_listbox, yscrollcommand=scrollbar.set)
list_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.config(command=list_box.yview)

# Checkbox (optional, shows organize mode)
run_checkbox_var = tk.BooleanVar()
run_checkbox = tk.Checkbutton(root, text="Organize Mode", variable=run_checkbox_var, state=tk.DISABLED)
run_checkbox.pack()

root.mainloop()