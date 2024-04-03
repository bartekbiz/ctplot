# import the tkinter module for GUI
import tkinter as tk
from tkinter import filedialog
import csv

# Function to open a specific .csv file
def open_csv_file():
   file_path = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))
   if file_path:
      try:
         with open(file_path, "r") as csv_file:
            # Read and display the CSV file's contents
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
               print(row)
      except Exception as e:
         print(f"Error: {e}")

# Create a Tkinter window
root = tk.Tk()
root.geometry("720x400")
root.title("Opening a .csv file using button")
# Create a button to open the .csv file
open_button = tk.Button(root, text="Open .csv File", command=open_csv_file)
open_button.pack()
# Start the Tkinter main loop to run the GUI application
root.mainloop()