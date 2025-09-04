import time
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

app = tk.Tk()
app.title("⏰ Digital Clock - Time Manager")
app.geometry("500x400")
app.resizable(False, False)
app.configure(bg="black")

# ---------------- Clock ----------------
clock_label = tk.Label(app, bg="black", fg="cyan",
                       font=("Helvetica", 48, "bold"))
clock_label.pack(pady=10)

date_label = tk.Label(app, bg="black", fg="lightgreen",
                      font=("Helvetica", 18))
date_label.pack()

day_label = tk.Label(app, bg="black", fg="yellow",
                     font=("Helvetica", 16, "italic"))
day_label.pack()


def update_time():
    now = datetime.now()
    clock_label.config(text=now.strftime("%H:%M:%S"))
    date_label.config(text=now.strftime("%B %d, %Y"))
    day_label.config(text=now.strftime("%A"))
    app.after(1000, update_time)


# ---------------- Alarm ----------------
alarm_frame = tk.LabelFrame(app, text="🔔 Set Alarm", bg="black", fg="white",
                            font=("Helvetica", 12, "bold"), padx=10, pady=10)
alarm_frame.pack(pady=10)

alarm_time = tk.StringVar()
tk.Entry(alarm_frame, textvariable=alarm_time, font=("Helvetica", 14),
         width=10, justify="center").pack(side="left", padx=5)
tk.Label(alarm_frame, text="Format: HH:MM:SS", bg="black",
         fg="gray").pack(side="left")


def check_alarm():
    now = datetime.now().strftime("%H:%M:%S")
    if alarm_time.get() == now:
        messagebox.showinfo("Alarm", "⏰ Wake up! Time’s up!")
    app.after(1000, check_alarm)


# ---------------- Stopwatch ----------------
stopwatch_frame = tk.LabelFrame(app, text="⏱ Stopwatch", bg="black", fg="white",
                                font=("Helvetica", 12, "bold"), padx=10, pady=10)
stopwatch_frame.pack(pady=10)

stopwatch_label = tk.Label(stopwatch_frame, text="00:00:00",
                           font=("Helvetica", 20), bg="black", fg="orange")
stopwatch_label.pack()

stopwatch_running = False
stopwatch_seconds = 0


def update_stopwatch():
    global stopwatch_seconds
    if stopwatch_running:
        stopwatch_seconds += 1
        mins, secs = divmod(stopwatch_seconds, 60)
        hrs, mins = divmod(mins, 60)
        stopwatch_label.config(text=f"{hrs:02}:{mins:02}:{secs:02}")
    app.after(1000, update_stopwatch)


def start_stopwatch():
    global stopwatch_running
    stopwatch_running = True


def stop_stopwatch():
    global stopwatch_running
    stopwatch_running = False


def reset_stopwatch():
    global stopwatch_seconds
    stopwatch_seconds = 0
    stopwatch_label.config(text="00:00:00")


tk.Button(stopwatch_frame, text="Start", command=start_stopwatch).pack(side="left", padx=5)
tk.Button(stopwatch_frame, text="Stop", command=stop_stopwatch).pack(side="left", padx=5)
tk.Button(stopwatch_frame, text="Reset", command=reset_stopwatch).pack(side="left", padx=5)


# ---------------- Timer ----------------
timer_frame = tk.LabelFrame(app, text="⏳ Timer", bg="black", fg="white",
                            font=("Helvetica", 12, "bold"), padx=10, pady=10)
timer_frame.pack(pady=10)

timer_label = tk.Label(timer_frame, text="00:00", font=("Helvetica", 20),
                       bg="black", fg="lightblue")
timer_label.pack()

timer_running = False
timer_seconds = 0


def update_timer():
    global timer_seconds, timer_running
    if timer_running and timer_seconds > 0:
        timer_seconds -= 1
        mins, secs = divmod(timer_seconds, 60)
        timer_label.config(text=f"{mins:02}:{secs:02}")
        if timer_seconds == 0:
            messagebox.showinfo("Timer", "⏳ Time’s up!")
    app.after(1000, update_timer)


def start_timer():
    global timer_seconds, timer_running
    try:
        mins = int(timer_entry.get())
        timer_seconds = mins * 60
        timer_running = True
    except:
        messagebox.showerror("Error", "Enter valid number of minutes!")


def stop_timer():
    global timer_running
    timer_running = False


def reset_timer():
    global timer_seconds
    timer_seconds = 0
    timer_label.config(text="00:00")


timer_entry = tk.Entry(timer_frame, font=("Helvetica", 14), width=5, justify="center")
timer_entry.pack(side="left", padx=5)

tk.Button(timer_frame, text="Start", command=start_timer).pack(side="left", padx=5)
tk.Button(timer_frame, text="Stop", command=stop_timer).pack(side="left", padx=5)
tk.Button(timer_frame, text="Reset", command=reset_timer).pack(side="left", padx=5)


# ---------------- Run App ----------------
update_time()
check_alarm()
update_stopwatch()
update_timer()
app.mainloop()
