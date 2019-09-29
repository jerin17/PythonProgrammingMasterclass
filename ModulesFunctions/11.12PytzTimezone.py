import  pytz
import datetime

country = "Europe/Moscow"

tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)

print("\nThe time in {} is {}".format(country, local_time))
print("UTC is {}".format(datetime.datetime.utcnow()))

# for i in pytz.all_timezones:
#     print(i, end=' ')
# print("\n\n")
#
# for i in sorted(pytz.country_names):
#     print(i + ": " + pytz.country_names[i])
# print("\n\n")
#
# for i in sorted(pytz.country_names):
#     print("{} : {} : {}".format(i, pytz.country_names[i], pytz.country_timezones.get(i)))

for i in sorted(pytz.country_names):
    print("{} : {}".format(i, pytz.country_names[i]), end=': ')
    if i in pytz.country_timezones:
        for j in sorted(pytz.country_timezones[i]):
            tz_to_display = pytz.timezone(j)
            local_time = datetime.datetime.now(tz= tz_to_display)
            print("\t{} :{}".format(j, local_time))
    else:
        print("\tNo Time-zone defined")
