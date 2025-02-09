import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Function to calculate age and display personalized message
def calculate_age():
    try:
        name = entry_name.get()  # Get the name entered by the user
        day = entry_day.get()  # Get the day input
        month = entry_month.get()  # Get the month input
        year = entry_year.get()  # Get the year input

        # Validate if inputs are integers and form a valid date
        birth_date_str = f"{year}-{month}-{day}"
        birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")  # Convert string to datetime object
        
        # Get today's date
        today = datetime.today()

        # Calculate age
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        
        # Display personalized result
        label_result.config(text=f"Hello {name}, your age is: {age} years", fg="green")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid date in day, month, year format.")

# Create main window
root = tk.Tk()
root.title("Age Calculator")
root.geometry("500x400")
root.config(bg="#f0f8ff")  # Background color for the window

# Create widgets
label_title = tk.Label(root, text="Age Calculator", font=("Arial", 20), fg="blue", bg="#f0f8ff")
label_title.pack(pady=20)

label_name = tk.Label(root, text="Enter your name:", font=("Arial", 14), bg="#f0f8ff")
label_name.pack(pady=5)

entry_name = tk.Entry(root, font=("Arial", 14), bg="lightyellow")
entry_name.pack(pady=5)

label_day = tk.Label(root, text="Enter your birth day (DD):", font=("Arial", 14), bg="#f0f8ff")
label_day.pack(pady=5)

entry_day = tk.Entry(root, font=("Arial", 14), bg="lightyellow")
entry_day.pack(pady=5)

label_month = tk.Label(root, text="Enter your birth month (MM):", font=("Arial", 14), bg="#f0f8ff")
label_month.pack(pady=5)

entry_month = tk.Entry(root, font=("Arial", 14), bg="lightyellow")
entry_month.pack(pady=5)

label_year = tk.Label(root, text="Enter your birth year (YYYY):", font=("Arial", 14), bg="#f0f8ff")
label_year.pack(pady=5)

entry_year = tk.Entry(root, font=("Arial", 14), bg="lightyellow")
entry_year.pack(pady=10)

button_calculate = tk.Button(root, text="Calculate Age", font=("Arial", 14), command=calculate_age, bg="#4CAF50", fg="white")
button_calculate.pack(pady=10)

label_result = tk.Label(root, text="", font=("Arial", 14), bg="#f0f8ff")
label_result.pack(pady=20)

# Run the application
root.mainloop()
