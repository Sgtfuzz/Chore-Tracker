import tkinter as tk
from tkinter import messagebox
import datetime

from chore_tracker import get_today_chore
from activity_logger import calculate_reward
from storage import save_log
from email_sender import send_email

#Setup
today = datetime.date.today()
today_str = today.isoformat()
today_chore = get_today_chore()

#GUI setup
root = tk.Tk()
root.title("Finns Chore Tracker")
root.geometry("400x350")

#Title and Chore Display
tk.Label(root, text=f"Today's Date: {today_str}", font=('Helvetica', 12, 'bold')).pack(pady=5)

if today_chore:
    tk.Label(root, text=f"Today's chore: {today_chore}", font=('Helvetica', 11)).pack(pady=5)
else:
    tk.Label(root, text="No chore assigned for today!", font=('Helvetica', 11, 'italic')).pack(pady=5)

#Checkboxes
chore_completed = tk.BooleanVar()
read = tk.BooleanVar()
math = tk.BooleanVar()
good_deed = tk.BooleanVar()

if today_chore:
    tk.Checkbutton(root, text="Chore completed", variable=chore_completed).pack(anchor='w', padx=20)

tk.Label(root, text="Activity Log:", font=('Helvetica', 11, 'underline')).pack(pady=(10, 0))
    
tk.Checkbutton(root, text="Read for at least 1 hour", variable=read).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Practiced math for 1 hour", variable=math).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Did a good deed", variable=good_deed).pack(anchor='w', padx=20)

#Submit
def submit_log():
    full_log = {}
    
    if today_chore:
        full_log["chore"] = {
            "name": today_chore,
            "completed": chore_completed.get()
        }
    
    reward_total = calculate_reward(read.get(), math.get(), good_deed.get())
    
    full_log["activities"] = {
        "read": read.get(),
        "math": math.get(),
        "good deed": good_deed.get(),
        "reward total": reward_total
    }

    #Save to data.json
    save_log(today_str, full_log)
    
    #Email summary
    subject = f"Finn's daily chore report - {today_str}"
    body = (
        f"Chore: {full_log['chore']['name']}\n"
        f"Completed: {'Yes' if full_log['chore']['completed'] else 'No'}\n\n"
        f"Read for 1 hour: {'Yes' if full_log['activities']['read'] else 'No'}\n"
        f"Did math practice: {'Yes' if full_log['activities']['math'] else 'No'}\n"
        f"Did a good deed: {'Yes' if full_log['activities']['good deed'] else 'No'}\n"
        f"Total reward earned for today: ${full_log['activities']['reward total']}"
    )
    
    #Email recipients
    recipients = [#recipent email goes here]
    
    #Send email
    try:    
        send_email(subject, body, recipients)
        messagebox.showinfo("Success", "Log saved and email sent!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email: {e}")

#Submit button
tk.Button(root, text="Submit", command=submit_log).pack(pady=10)

#Start GUI
root.mainloop()