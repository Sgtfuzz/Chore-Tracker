def log_activities():
    def get_boolean_input(prompt):
        while True:
            response = input(prompt).strip().lower()
            if response in ["yes", "y"]:
                return True
            elif response in ["no", "n"]:
                return False
            else:
                print("Please enter 'yes' or 'no'.")

    #Ask user about each bonus activity
    read = get_boolean_input("Did Finn read for at least 1 hour today? (yes/no): ")
    math = get_boolean_input("Did Finn practice any math problems today? (yes/no): ")
    good_deed = get_boolean_input("Was Finn helpful today? (yes/no): ")
    
    #Calculate total reward
    reward_total = 0
    if read:
        reward_total += 5
    if math:
        reward_total += 5
    if good_deed:
        reward_total += 5

    #Build activity log
    activity_log = {
        "read": read,
        "math": math,
        "good deed": good_deed,
        "reward total": reward_total
    }
    
    print("Activity log recorded:", activity_log)
    return activity_log

def calculate_reward(read: bool, math: bool, good_deed: bool) -> int:
    return (5 if read else 0) + (5 if math else 0) + (5 if good_deed else 0)