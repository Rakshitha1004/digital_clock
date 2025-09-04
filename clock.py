from tkinter import Label, Tk, Button
import time
from datetime import datetime

app = Tk()
app.title("🕒 Digital Clock")
app.geometry("400x200")
app.resizable(False, False)
app.configure(bg="black")

# Time Label
clock_label = Label(app, bg="black", fg="cyan",
                    font=("Helvetica", 48, "bold"), relief='flat')
clock_label.pack(pady=10)

# Date Label
date_label = Label(app, bg="black", fg="lightgreen",
                   font=("Helvetica", 18))
date_label.pack()

# Day Label
day_label = Label(app, bg="black", fg="yellow",
                  font=("Helvetica", 16, "italic"))
day_label.pack()

# 12/24 hr toggle button
time_format = 24  # default format

def toggle_format():
    global time_format
    time_format = 12 if time_format == 24 else 24

toggle_btn = Button(app, text="Switch 12/24 hr ⏱",
                    command=toggle_format, bg="gray", fg="white",
                    font=("Helvetica", 12, "bold"))
toggle_btn.pack(pady=5)

def update_time():
    now = datetime.now()

    if time_format == 12:
        current_time = now.strftime("%I:%M:%S %p")  # 12-hour format
    else:
        current_time = now.strftime("%H:%M:%S")  # 24-hour format

    current_date = now.strftime("%B %d, %Y")
    current_day = now.strftime("%A")

    clock_label.config(text=current_time)
    date_label.config(text=current_date)
    day_label.config(text=current_day)

    clock_label.after(1000, update_time)  # update every second

update_time()
app.mainloop()
