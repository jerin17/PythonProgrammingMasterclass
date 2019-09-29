# import time
# print(time.gmtime())
# print(time.localtime(time.time()))
# print(time.time())

# time_here = time.localtime()
# print(time_here)
# print()
# print("Year : ", time_here[0], time_here.tm_year)
# print("Month : ", time_here[1], time_here.tm_mon)
# print("Day : ", time_here[2], time_here.tm_mday)


# import time
# from time import time as my_timer
# import random
# input("Press enter to start ")
# wait_time = random.randint(1, 6)
# time.sleep(wait_time)
# start_time = my_timer()
# input("Press enter to stop ")
# end_time = my_timer()
# print("\nStarted at " + time.strftime("%X", time.localtime(start_time)))
# print("Ended at " + time.strftime("%X", time.localtime(end_time)))
# print("\nYour reaction time was {} seconds".format(end_time - start_time))

import time
print("time()\n", time.get_clock_info('time'))
print("\nperf_counter()\n", time.get_clock_info('perf_counter'))
print("\nmonotonic()\n", time.get_clock_info('monotonic'))
print("\n   process_time()\n", time.get_clock_info('process_time'))

