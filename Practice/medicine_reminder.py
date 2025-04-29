import time

def system_time():
    # Get the current local time
    now = time.localtime()
    return now.tm_hour, now.tm_min

def reminder():
    size = int(input("How many medicines do you need to be reminded of? "))
    medicines = []
    quantities = []
    reminder_hours = []
    reminder_minutes = []

    # Collect user input for reminders
    for i in range(size):
        name = input(f"Enter the name of your Medicine {i + 1}: ")
        medicines.append(name)
        qty = int(input("Enter the quantity of your Medicine: "))
        quantities.append(qty)
        r_hour = int(input("Enter the hour (24-hour format) at which you need to take your medicine: "))
        reminder_hours.append(r_hour)
        r_minute = int(input("Enter the minute at which you need to take your medicine: "))
        reminder_minutes.append(r_minute)

    print("Your reminders are set!")

    while True:
        h, m = system_time()
        for i in range(size):
            if h == reminder_hours[i] and m == reminder_minutes[i]:
                print("\n\tReminder!")
                print(f"{h:02}:{m:02} - Time to take your {medicines[i]}. Quantity: {quantities[i]}")
                # Pause for 60 seconds to avoid repeated reminders in the same minute
                time.sleep(60)
        # Check time every 10 seconds
        time.sleep(10)

print("\t----------Medicine Reminder----------")
reminder()
