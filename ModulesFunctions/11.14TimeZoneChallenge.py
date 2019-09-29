# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.

import datetime
import pytz

available_zones = {'1': 'Africa/Tunis',
                   '2': 'Asia/Kolkata',
                   '3': 'Australia/Adelaide',
                   '4': 'Europe/Brussels',
                   '5': 'Europe/London',
                   '6': 'Japan',
                   '7': 'Pacific/Tahiti',
                   '8': 'US/Hawaii',
                   '9': 'Zulu'}

print("Please enter a Time zone (or 0 to quit): ")
for i in sorted(available_zones):
    print("{}. {}".format(i, available_zones[i]))

while True:
    choice = input()

    if choice == 0:
        break

    if choice in available_zones.keys():
        tz_to_display = pytz.timezone(available_zones[choice])
        t = datetime.datetime.now(tz=tz_to_display)
        print("Time in {} : {}, {}".format(available_zones[choice], t.strftime("%A %x %X %z"), t.tzname()))
        print("Local time : {}".format(datetime.datetime.now().strftime("%A %x %X")))
        print("UTC Time   : {}".format(datetime.datetime.utcnow().strftime("%A %x %X")))
        print()

