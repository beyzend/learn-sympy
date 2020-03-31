days = ["sunday", "monday", "tuesday", "wednesday", "thursday",
        "friday", "saturday"]
startDay = 0
whichDay = 0
startDay = int(input("What day is the start of your trip?\n"))
totalDays = int(input("How many days is you trip?\n"))
whichDay = startDay + totalDays
print("The day is: {}".format(days[whichDay % len(days)]))
