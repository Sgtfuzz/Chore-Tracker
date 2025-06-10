import datetime


#weekly chore schedule
day_chore = {"Monday": "Vacuum",
             "Tuesday": "Clean room",
             "Wednesday": "Put dirty clothes in washer",
             "Thursday": "Clean up kitchen table",
             "Friday": "Clean livingroom"}

#Get today's chore
def get_today_chore():
    today = datetime.date.today()
    day_of_week = today.strftime("%A")
    return day_chore.get(day_of_week, None)

def chore_assignment():
    chore = get_today_chore()
    
    if not chore:
        print("No chore assigned for today.")
        return None
    
    print("Today's chore is:", chore)
    
    while True:
        response = input("Did you complete today's chore? (yes/no): ").strip().lower()
        if response in ['yes', 'y']:
            completed = True
            break
        elif response in ['no', 'n']:
            completed = False
            break
        else:
            print("Please enter 'yes' or 'no'.")
    
    chore_log = {
        "chore": {
            "name": chore,
            "completed": completed
        }
    }
    
    print("Chore completion recorded:", chore_log)
    return chore_log