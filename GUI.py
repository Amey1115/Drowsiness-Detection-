# Amey custom GUI
import tkinter as tk
from tkinter import messagebox
import subprocess
import webbrowser


def start_clicked():
    messagebox.showinfo("Hello", "Please wait while the system loads...")
    subprocess.call(["python", "drowsiness detection.py"])


def exit_clicked():
    window.destroy()


url = "https://docs.google.com/document/d/1TOK77Ao5AElFciglAmuCnGrsT4Ozjz1KgQLS8VE1YfM/edit?usp=sharing"
new = 1


def openweb():
    webbrowser.open(url, new=new)


# Create the main window
window = tk.Tk()
window.title("Homepage")
window.geometry("700x500")  # Set window size to 700x500

# Create a label for "Welcome" text
welcome_label = tk.Label(
    window, text="Welcome to the Drowsiness Detection System", font=("Helvetica", 24)
)
welcome_label.pack(pady=20)

# Create a frame to center the buttons
button_frame = tk.Frame(window)
button_frame.pack()

# Create a "Start" button
start_button = tk.Button(
    button_frame, text="Start Monitoring", command=start_clicked, font=("Helvetica", 16)
)
start_button.pack(pady=20)

# Read about drowsiness detection system button
DD_Working = tk.Button(
    button_frame, text="Working of this system", command=openweb, font=("Helvetica", 16)
)
DD_Working.pack(pady=20)

# Create an "Exit" button
exit_button = tk.Button(
    button_frame, text="Exit", command=exit_clicked, font=("Helvetica", 16)
)
exit_button.pack(pady=10)

# Set background and foreground colors
# window.configure()
welcome_label.configure(bg="lightgray", fg="blue")
start_button.configure(bg="green", fg="white")
DD_Working.configure(bg="purple", fg="white")
exit_button.configure(bg="red", fg="white")

# Run the Tkinter event loop
window.mainloop()
