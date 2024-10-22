import os
import platform
import tkinter as tk
from tkinter import messagebox

# Function to restart the computer
def restart_computer():
    # Show a confirmation dialog
    confirm = messagebox.askyesno("Confirm", "Are you sure?")
    if confirm:
        if platform.system() == "Windows":
            os.system("shutdown /r /t 0")  # Restart Windows immediately
        elif platform.system() == "Linux" or platform.system() == "Darwin":  # Darwin is macOS
            os.system("sudo reboot")  # Requires sudo on Linux/macOS
    
# Create the main window
root = tk.Tk()
root.title("Restart Computer")
root.geometry("300x200")  # Set the size of the window

# Create the button
button = tk.Button(root, text="Click Me", bg="red", fg="white", font=("Helvetica", 16), command=restart_computer)
button.pack(expand=True)  # Center the button

# Start the GUI event loop
root.mainloop()
